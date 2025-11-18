"""
MEZAN / ATLAS - Multi-Agent AI Research & Optimization Orchestration System

MEZAN = Meta-Equilibrium Zero-regret Assignment Network

Provides:
- MEZAN dual-solver balancing engine
- Ultrathink 5-team parallel agent system
- 40+ ATLAS research agents
- Dialectical workflows
- Integration with Libria optimization solvers
"""

__version__ = "0.2.0"  # Updated for MEZAN implementation
__author__ = "MEZAN Research Team"

# ATLAS core components
from atlas_core.agent import ResearchAgent, AgentConfig
from atlas_core.engine import ATLASEngine
from atlas_core.blackboard import ATLASBlackboard

# MEZAN engine components
from atlas_core.mezan_engine import (
    MezanEngine,
    BaseSolver,
    SolverConfig,
    SolverResult,
    SolverType,
    MezanState,
)

# Ultrathink parallel agents
from atlas_core.ultrathink_agents import (
    UltrathinkOrchestrator,
    AgentTask,
    AgentResult,
    TeamRole,
    TaskPriority,
    TaskStatus,
)

# MEZAN orchestrator
from atlas_core.mezan_orchestrator import (
    MezanOrchestrator,
    OrchestratorConfig,
    OrchestratorMode,
    OrchestrationResult,
    create_default_orchestrator,
)

__all__ = [
    # Version info
    "__version__",
    # ATLAS core
    "ResearchAgent",
    "AgentConfig",
    "ATLASEngine",
    "ATLASBlackboard",
    # MEZAN engine
    "MezanEngine",
    "BaseSolver",
    "SolverConfig",
    "SolverResult",
    "SolverType",
    "MezanState",
    # Ultrathink agents
    "UltrathinkOrchestrator",
    "AgentTask",
    "AgentResult",
    "TeamRole",
    "TaskPriority",
    "TaskStatus",
    # MEZAN orchestrator
    "MezanOrchestrator",
    "OrchestratorConfig",
    "OrchestratorMode",
    "OrchestrationResult",
    "create_default_orchestrator",
]
