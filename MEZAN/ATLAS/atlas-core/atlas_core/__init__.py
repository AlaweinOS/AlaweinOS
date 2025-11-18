"""
ATLAS Core - Multi-Agent AI Research Orchestration System

Provides core functionality for orchestrating 40+ research agents
with dialectical workflows and Libria solver integration.
"""

__version__ = "0.1.0"
__author__ = "ATLAS Team"

from atlas_core.agent import ResearchAgent, AgentConfig
from atlas_core.engine import ATLASEngine
from atlas_core.blackboard import ATLASBlackboard

__all__ = [
    "ResearchAgent",
    "AgentConfig",
    "ATLASEngine",
    "ATLASBlackboard",
    "__version__",
]
