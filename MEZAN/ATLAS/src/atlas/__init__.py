"""
ATLAS Hypothesis Evaluation Platform

A comprehensive AI-powered platform for evaluating research hypotheses
through multiple evaluation modes including adversarial testing, cross-domain
collision, evolutionary simulation, multiverse analysis, and prediction markets.
"""

__version__ = "0.1.0"
__author__ = "ATLAS Team"
__email__ = "meshal@berkeley.edu"

# Core components
# Advanced systems
from atlas.advanced_systems import (
    AdaptiveScheduler,
    BootstrapCI,
    ComparativeAnalyzer,
    MetaEvaluator,
    MLTaskRouter,
    TenantQuotaManager,
)
from atlas.pii_redactor import PIIPipeline
from atlas.quality_gates import GateResult, GateStatus, QualityGates
from atlas.results_store import (
    DistributedCache,
    DynamicConfig,
    PreSalesArtifacts,
    ResultsAPI,
    ResultsStore,
)
from atlas.shadow_eval import BudgetMonitor, ShadowEvaluator
from atlas.tracing_logger import ATLASTracer, StructuredLogger

__all__ = [
    # Version info
    "__version__",
    "__author__",
    "__email__",
    # Quality gates
    "QualityGates",
    "GateStatus",
    "GateResult",
    # PII handling
    "PIIPipeline",
    # Tracing
    "ATLASTracer",
    "StructuredLogger",
    # Shadow evaluation
    "ShadowEvaluator",
    "BudgetMonitor",
    # Results storage
    "ResultsStore",
    "ResultsAPI",
    "DistributedCache",
    "DynamicConfig",
    "PreSalesArtifacts",
    # Advanced systems
    "MetaEvaluator",
    "BootstrapCI",
    "ComparativeAnalyzer",
    "AdaptiveScheduler",
    "MLTaskRouter",
    "TenantQuotaManager",
]
