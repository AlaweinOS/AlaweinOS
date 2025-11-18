"""
ATLAS-Optilibria Integration Layer

Enables MEZAN/ATLAS to leverage Optilibria's optimization capabilities through
Redis-based async task management and the ATLAS agent protocol.
"""

from optilibria.integrations.atlas.adapter import ATLASOptimizationAdapter
from optilibria.integrations.atlas.agent import OptilibriaAgent
from optilibria.integrations.atlas.config import ATLASConfig
from optilibria.integrations.atlas.task_queue import OptimizationTaskQueue

__all__ = [
    "ATLASOptimizationAdapter",
    "OptilibriaAgent",
    "ATLASConfig",
    "OptimizationTaskQueue",
]