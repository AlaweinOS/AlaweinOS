"""
MEZAN Performance Monitoring and Telemetry System.

This module provides comprehensive observability capabilities including:
- Prometheus-compatible metrics collection
- Performance tracking (latency, throughput, errors)
- Resource monitoring (CPU, memory, disk, network)
- Custom metrics with histograms and summaries
- Real-time anomaly detection
- Alert management and thresholds
- Time-series data storage and export
"""

import json
import psutil
import threading
import time
import logging
from collections import defaultdict, deque
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Optional, Any, Callable, Tuple
from pathlib import Path
import numpy as np
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class MetricType(Enum):
    """Types of metrics supported by the telemetry system."""
    COUNTER = "counter"
    GAUGE = "gauge"
    HISTOGRAM = "histogram"
    SUMMARY = "summary"


@dataclass
class AlertRule:
    """Configuration for metric alert thresholds."""
    metric_name: str
    threshold: float
    condition: str  # 'above', 'below', 'equals'
    duration_seconds: int = 60
    callback: Optional[Callable] = None
    severity: str = "warning"  # 'info', 'warning', 'critical'


@dataclass
class MetricSnapshot:
    """Point-in-time snapshot of a metric."""
    name: str
    type: MetricType
    value: float
    timestamp: float
    labels: Dict[str, str] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)


class Metric(ABC):
    """Abstract base class for all metric types."""

    def __init__(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None):
        self.name = name
        self.description = description
        self.labels = labels or {}
        self._lock = threading.RLock()
        self._last_updated = time.time()

    @abstractmethod
    def get_value(self) -> float:
        """Get current metric value."""
        pass

    @abstractmethod
    def to_prometheus(self) -> str:
        """Export metric in Prometheus format."""
        pass


class Counter(Metric):
    """Monotonically increasing counter metric."""

    def __init__(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None):
        super().__init__(name, description, labels)
        self._value = 0.0

    def inc(self, value: float = 1.0):
        """Increment counter by value."""
        if value < 0:
            raise ValueError("Counter can only be incremented with positive values")
        with self._lock:
            self._value += value
            self._last_updated = time.time()

    def get_value(self) -> float:
        with self._lock:
            return self._value

    def to_prometheus(self) -> str:
        labels_str = ",".join(f'{k}="{v}"' for k, v in self.labels.items())
        labels_part = f"{{{labels_str}}}" if labels_str else ""
        return f"# HELP {self.name} {self.description}\n# TYPE {self.name} counter\n{self.name}{labels_part} {self._value}"


class Gauge(Metric):
    """Gauge metric that can go up and down."""

    def __init__(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None):
        super().__init__(name, description, labels)
        self._value = 0.0

    def set(self, value: float):
        """Set gauge to specific value."""
        with self._lock:
            self._value = value
            self._last_updated = time.time()

    def inc(self, value: float = 1.0):
        """Increment gauge by value."""
        with self._lock:
            self._value += value
            self._last_updated = time.time()

    def dec(self, value: float = 1.0):
        """Decrement gauge by value."""
        with self._lock:
            self._value -= value
            self._last_updated = time.time()

    def get_value(self) -> float:
        with self._lock:
            return self._value

    def to_prometheus(self) -> str:
        labels_str = ",".join(f'{k}="{v}"' for k, v in self.labels.items())
        labels_part = f"{{{labels_str}}}" if labels_str else ""
        return f"# HELP {self.name} {self.description}\n# TYPE {self.name} gauge\n{self.name}{labels_part} {self._value}"


class Histogram(Metric):
    """Histogram metric for tracking value distributions."""

    DEFAULT_BUCKETS = [0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0, float('inf')]

    def __init__(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None,
                 buckets: Optional[List[float]] = None):
        super().__init__(name, description, labels)
        self.buckets = sorted(buckets or self.DEFAULT_BUCKETS)
        self._observations = []
        self._bucket_counts = {b: 0 for b in self.buckets}
        self._sum = 0.0
        self._count = 0

    def observe(self, value: float):
        """Record an observation."""
        with self._lock:
            self._observations.append(value)
            self._sum += value
            self._count += 1
            for bucket in self.buckets:
                if value <= bucket:
                    self._bucket_counts[bucket] += 1
            self._last_updated = time.time()

    def get_value(self) -> float:
        """Return mean value."""
        with self._lock:
            return self._sum / self._count if self._count > 0 else 0.0

    def get_percentile(self, percentile: float) -> float:
        """Calculate percentile value."""
        with self._lock:
            if not self._observations:
                return 0.0
            sorted_obs = sorted(self._observations)
            index = int(len(sorted_obs) * percentile / 100.0)
            return sorted_obs[min(index, len(sorted_obs) - 1)]

    def to_prometheus(self) -> str:
        labels_str = ",".join(f'{k}="{v}"' for k, v in self.labels.items())
        result = [f"# HELP {self.name} {self.description}", f"# TYPE {self.name} histogram"]

        for bucket, count in self._bucket_counts.items():
            bucket_labels = f'{labels_str},le="{bucket}"' if labels_str else f'le="{bucket}"'
            result.append(f"{self.name}_bucket{{{bucket_labels}}} {count}")

        labels_part = f"{{{labels_str}}}" if labels_str else ""
        result.append(f"{self.name}_sum{labels_part} {self._sum}")
        result.append(f"{self.name}_count{labels_part} {self._count}")

        return "\n".join(result)


class ResourceMonitor:
    """System resource monitoring capabilities."""

    def __init__(self, interval_seconds: int = 10):
        self.interval = interval_seconds
        self._running = False
        self._thread = None
        self._metrics = {}
        self._history = defaultdict(lambda: deque(maxlen=1000))

    def start(self):
        """Start resource monitoring."""
        if self._running:
            return

        self._running = True
        self._thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._thread.start()
        logger.info("Resource monitoring started")

    def stop(self):
        """Stop resource monitoring."""
        self._running = False
        if self._thread:
            self._thread.join(timeout=5)
        logger.info("Resource monitoring stopped")

    def _monitor_loop(self):
        """Main monitoring loop."""
        while self._running:
            try:
                timestamp = time.time()

                # CPU metrics
                cpu_percent = psutil.cpu_percent(interval=1)
                cpu_count = psutil.cpu_count()
                cpu_freq = psutil.cpu_freq()

                # Memory metrics
                memory = psutil.virtual_memory()
                swap = psutil.swap_memory()

                # Disk metrics
                disk = psutil.disk_usage('/')
                disk_io = psutil.disk_io_counters()

                # Network metrics
                net_io = psutil.net_io_counters()

                # Process-specific metrics
                process = psutil.Process()
                process_memory = process.memory_info()
                process_cpu = process.cpu_percent()

                # Store metrics
                metrics = {
                    'cpu_percent': cpu_percent,
                    'cpu_count': cpu_count,
                    'cpu_freq_current': cpu_freq.current if cpu_freq else 0,
                    'memory_percent': memory.percent,
                    'memory_available_gb': memory.available / (1024**3),
                    'memory_used_gb': memory.used / (1024**3),
                    'swap_percent': swap.percent,
                    'disk_percent': disk.percent,
                    'disk_free_gb': disk.free / (1024**3),
                    'disk_read_mb': disk_io.read_bytes / (1024**2) if disk_io else 0,
                    'disk_write_mb': disk_io.write_bytes / (1024**2) if disk_io else 0,
                    'network_sent_mb': net_io.bytes_sent / (1024**2),
                    'network_recv_mb': net_io.bytes_recv / (1024**2),
                    'process_memory_mb': process_memory.rss / (1024**2),
                    'process_cpu_percent': process_cpu
                }

                self._metrics = metrics

                # Store history
                for key, value in metrics.items():
                    self._history[key].append((timestamp, value))

            except Exception as e:
                logger.error(f"Resource monitoring error: {e}")

            time.sleep(self.interval)

    def get_metrics(self) -> Dict[str, float]:
        """Get current resource metrics."""
        return self._metrics.copy()

    def get_history(self, metric_name: str, duration_seconds: int = 300) -> List[Tuple[float, float]]:
        """Get metric history for specified duration."""
        if metric_name not in self._history:
            return []

        cutoff_time = time.time() - duration_seconds
        return [(t, v) for t, v in self._history[metric_name] if t >= cutoff_time]


class AnomalyDetector:
    """Real-time anomaly detection for metrics."""

    def __init__(self, window_size: int = 100, z_threshold: float = 3.0):
        self.window_size = window_size
        self.z_threshold = z_threshold
        self._windows = defaultdict(lambda: deque(maxlen=window_size))
        self._anomalies = []

    def update(self, metric_name: str, value: float) -> bool:
        """Update detector with new value and check for anomaly."""
        window = self._windows[metric_name]
        window.append(value)

        if len(window) < 10:  # Need minimum samples
            return False

        # Calculate z-score
        values = np.array(window)
        mean = np.mean(values)
        std = np.std(values)

        if std == 0:
            return False

        z_score = abs((value - mean) / std)

        if z_score > self.z_threshold:
            anomaly = {
                'metric': metric_name,
                'value': value,
                'mean': mean,
                'std': std,
                'z_score': z_score,
                'timestamp': time.time()
            }
            self._anomalies.append(anomaly)
            logger.warning(f"Anomaly detected: {anomaly}")
            return True

        return False

    def get_anomalies(self, since: Optional[float] = None) -> List[Dict]:
        """Get detected anomalies since timestamp."""
        if since is None:
            return self._anomalies.copy()
        return [a for a in self._anomalies if a['timestamp'] >= since]


class AlertManager:
    """Manages metric alerts and notifications."""

    def __init__(self):
        self.rules = []
        self._active_alerts = {}
        self._alert_history = []
        self._lock = threading.Lock()

    def add_rule(self, rule: AlertRule):
        """Add alert rule."""
        with self._lock:
            self.rules.append(rule)

    def check_alerts(self, metrics: Dict[str, float]):
        """Check metrics against alert rules."""
        with self._lock:
            for rule in self.rules:
                if rule.metric_name not in metrics:
                    continue

                value = metrics[rule.metric_name]
                triggered = False

                if rule.condition == 'above' and value > rule.threshold:
                    triggered = True
                elif rule.condition == 'below' and value < rule.threshold:
                    triggered = True
                elif rule.condition == 'equals' and value == rule.threshold:
                    triggered = True

                alert_key = f"{rule.metric_name}_{rule.condition}_{rule.threshold}"

                if triggered:
                    if alert_key not in self._active_alerts:
                        # New alert
                        alert = {
                            'rule': rule,
                            'value': value,
                            'start_time': time.time(),
                            'severity': rule.severity
                        }
                        self._active_alerts[alert_key] = alert
                        self._alert_history.append(alert)

                        if rule.callback:
                            try:
                                rule.callback(rule, value)
                            except Exception as e:
                                logger.error(f"Alert callback error: {e}")

                        logger.warning(f"Alert triggered: {rule.metric_name} {rule.condition} {rule.threshold}, value: {value}")
                else:
                    # Alert resolved
                    if alert_key in self._active_alerts:
                        del self._active_alerts[alert_key]
                        logger.info(f"Alert resolved: {rule.metric_name}")

    def get_active_alerts(self) -> List[Dict]:
        """Get currently active alerts."""
        with self._lock:
            return list(self._active_alerts.values())


class MetricsCollector:
    """Central metrics collection and management system."""

    def __init__(self, export_interval: int = 60):
        self.metrics = {}
        self.export_interval = export_interval
        self.resource_monitor = ResourceMonitor()
        self.anomaly_detector = AnomalyDetector()
        self.alert_manager = AlertManager()
        self._lock = threading.RLock()
        self._export_thread = None
        self._running = False
        self._time_series_data = defaultdict(list)

    def register_metric(self, metric: Metric):
        """Register a metric for collection."""
        with self._lock:
            self.metrics[metric.name] = metric
            logger.debug(f"Registered metric: {metric.name}")

    def counter(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None) -> Counter:
        """Create and register a counter metric."""
        counter = Counter(name, description, labels)
        self.register_metric(counter)
        return counter

    def gauge(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None) -> Gauge:
        """Create and register a gauge metric."""
        gauge = Gauge(name, description, labels)
        self.register_metric(gauge)
        return gauge

    def histogram(self, name: str, description: str = "", labels: Optional[Dict[str, str]] = None,
                  buckets: Optional[List[float]] = None) -> Histogram:
        """Create and register a histogram metric."""
        histogram = Histogram(name, description, labels, buckets)
        self.register_metric(histogram)
        return histogram

    @contextmanager
    def timer(self, metric_name: str):
        """Context manager for timing operations."""
        if metric_name not in self.metrics:
            self.histogram(metric_name, f"Timing for {metric_name}")

        start = time.time()
        try:
            yield
        finally:
            duration = time.time() - start
            if isinstance(self.metrics[metric_name], Histogram):
                self.metrics[metric_name].observe(duration)

    def start(self):
        """Start metrics collection."""
        self._running = True
        self.resource_monitor.start()
        self._export_thread = threading.Thread(target=self._export_loop, daemon=True)
        self._export_thread.start()
        logger.info("Metrics collector started")

    def stop(self):
        """Stop metrics collection."""
        self._running = False
        self.resource_monitor.stop()
        if self._export_thread:
            self._export_thread.join(timeout=5)
        logger.info("Metrics collector stopped")

    def _export_loop(self):
        """Periodic export loop."""
        while self._running:
            try:
                self._collect_and_export()
            except Exception as e:
                logger.error(f"Export error: {e}")
            time.sleep(self.export_interval)

    def _collect_and_export(self):
        """Collect metrics and export."""
        timestamp = time.time()

        # Collect custom metrics
        snapshots = []
        with self._lock:
            for metric in self.metrics.values():
                snapshot = MetricSnapshot(
                    name=metric.name,
                    type=MetricType.COUNTER if isinstance(metric, Counter) else
                         MetricType.GAUGE if isinstance(metric, Gauge) else
                         MetricType.HISTOGRAM,
                    value=metric.get_value(),
                    timestamp=timestamp,
                    labels=metric.labels
                )
                snapshots.append(snapshot)

                # Store time-series data
                self._time_series_data[metric.name].append((timestamp, metric.get_value()))

                # Check for anomalies
                self.anomaly_detector.update(metric.name, metric.get_value())

        # Collect resource metrics
        resource_metrics = self.resource_monitor.get_metrics()
        for name, value in resource_metrics.items():
            self._time_series_data[f"system_{name}"].append((timestamp, value))
            self.anomaly_detector.update(f"system_{name}", value)

        # Check alerts
        all_metrics = {m.name: m.get_value() for m in self.metrics.values()}
        all_metrics.update({f"system_{k}": v for k, v in resource_metrics.items()})
        self.alert_manager.check_alerts(all_metrics)

        logger.debug(f"Exported {len(snapshots)} metrics")

    def get_metrics_json(self) -> str:
        """Export metrics as JSON."""
        data = {
            'timestamp': time.time(),
            'metrics': {},
            'resources': self.resource_monitor.get_metrics(),
            'active_alerts': self.alert_manager.get_active_alerts(),
            'recent_anomalies': self.anomaly_detector.get_anomalies(time.time() - 300)
        }

        with self._lock:
            for name, metric in self.metrics.items():
                data['metrics'][name] = {
                    'value': metric.get_value(),
                    'type': type(metric).__name__,
                    'labels': metric.labels
                }

        return json.dumps(data, indent=2)

    def get_prometheus_metrics(self) -> str:
        """Export metrics in Prometheus format."""
        lines = []
        with self._lock:
            for metric in self.metrics.values():
                lines.append(metric.to_prometheus())

        # Add resource metrics
        for name, value in self.resource_monitor.get_metrics().items():
            lines.append(f"system_{name} {value}")

        return "\n".join(lines)


# Example instrumentation
def create_example_metrics():
    """Create example metrics setup."""
    collector = MetricsCollector(export_interval=10)

    # Performance metrics
    request_counter = collector.counter("mezan_requests_total", "Total requests processed")
    error_counter = collector.counter("mezan_errors_total", "Total errors")
    active_connections = collector.gauge("mezan_active_connections", "Active connections")
    request_duration = collector.histogram("mezan_request_duration_seconds", "Request duration",
                                          buckets=[0.01, 0.05, 0.1, 0.5, 1.0, 5.0])

    # Alert rules
    collector.alert_manager.add_rule(AlertRule(
        metric_name="system_cpu_percent",
        threshold=80.0,
        condition="above",
        duration_seconds=60,
        severity="warning"
    ))

    collector.alert_manager.add_rule(AlertRule(
        metric_name="system_memory_percent",
        threshold=90.0,
        condition="above",
        duration_seconds=30,
        severity="critical"
    ))

    return collector


if __name__ == "__main__":
    # Example usage
    logging.basicConfig(level=logging.INFO)

    collector = create_example_metrics()
    collector.start()

    try:
        # Simulate some operations
        for i in range(100):
            with collector.timer("operation_duration"):
                time.sleep(0.1)

                # Update metrics
                collector.metrics["mezan_requests_total"].inc()
                if i % 10 == 0:
                    collector.metrics["mezan_errors_total"].inc()
                collector.metrics["mezan_active_connections"].set(i % 20)

                # Get current state
                if i % 20 == 0:
                    print("\n=== Metrics Export ===")
                    print(collector.get_metrics_json())
                    print("\n=== Prometheus Format ===")
                    print(collector.get_prometheus_metrics()[:500])  # First 500 chars

    finally:
        collector.stop()