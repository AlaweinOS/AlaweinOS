"""
Configuration management for ATLAS-Optilibria integration
"""

import os
from dataclasses import dataclass, field
from typing import Dict, Optional, Any


@dataclass
class ATLASConfig:
    """Configuration for ATLAS-Optilibria integration"""

    # Redis connection settings
    redis_url: str = field(
        default_factory=lambda: os.getenv("ATLAS_REDIS_URL", "redis://localhost:6379/0")
    )
    redis_db: int = field(
        default_factory=lambda: int(os.getenv("ATLAS_REDIS_DB", "0"))
    )

    # Task queue settings
    task_queue_name: str = "optilibria:tasks"
    result_queue_name: str = "optilibria:results"
    task_timeout: int = 3600  # 1 hour default timeout
    max_retries: int = 3
    retry_delay: int = 5  # seconds

    # ATLAS integration settings
    agent_id: str = "optilibria-agent"
    agent_type: str = "optimization"
    specialization: str = "combinatorial_and_continuous_optimization"
    skill_level: float = 0.95  # High skill level for optimization tasks
    max_concurrent_tasks: int = 10

    # Optilibria settings
    default_method: str = "auto"  # Use AI selector by default
    enable_gpu: bool = True
    enable_quantum: bool = False

    # Performance settings
    batch_size: int = 100
    cache_results: bool = True
    cache_ttl: int = 3600  # Cache results for 1 hour

    # Monitoring and logging
    enable_metrics: bool = True
    log_level: str = "INFO"
    trace_executions: bool = True

    # Method-specific defaults
    method_configs: Dict[str, Any] = field(default_factory=lambda: {
        "simulated_annealing": {
            "initial_temperature": 1000,
            "cooling_rate": 0.95,
            "max_iterations": 10000
        },
        "genetic_algorithm": {
            "population_size": 100,
            "generations": 500,
            "mutation_rate": 0.01,
            "crossover_rate": 0.8
        },
        "tabu_search": {
            "tabu_tenure": 20,
            "max_iterations": 5000
        }
    })

    @classmethod
    def from_env(cls) -> "ATLASConfig":
        """Create config from environment variables"""
        return cls(
            redis_url=os.getenv("ATLAS_REDIS_URL", cls.__dataclass_fields__["redis_url"].default_factory()),
            task_queue_name=os.getenv("OPTILIBRIA_TASK_QUEUE", "optilibria:tasks"),
            agent_id=os.getenv("OPTILIBRIA_AGENT_ID", "optilibria-agent"),
            default_method=os.getenv("OPTILIBRIA_DEFAULT_METHOD", "auto"),
            enable_gpu=os.getenv("OPTILIBRIA_ENABLE_GPU", "true").lower() == "true",
            max_concurrent_tasks=int(os.getenv("OPTILIBRIA_MAX_TASKS", "10")),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary"""
        return {
            "redis_url": self.redis_url,
            "redis_db": self.redis_db,
            "task_queue_name": self.task_queue_name,
            "result_queue_name": self.result_queue_name,
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "default_method": self.default_method,
            "max_concurrent_tasks": self.max_concurrent_tasks,
            "enable_gpu": self.enable_gpu,
            "enable_quantum": self.enable_quantum,
        }