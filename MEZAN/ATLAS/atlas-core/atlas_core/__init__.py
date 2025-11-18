"""
MEZAN / ATLAS - Multi-Agent AI Research & Optimization Orchestration System

MEZAN = Meta-Equilibrium Zero-regret Assignment Network

Provides:
- MEZAN dual-solver balancing engine
- DeepThink 3+1 agent system (optimized: 3 parallel + 1 sequential deep)
- Intelligent solver selection with deep reasoning
- 40+ ATLAS research agents
- Dialectical workflows
- Integration with Libria optimization solvers

Version 3.0: Optimized for depth over breadth
- Reduced parallel agents from 5 to 3
- Added deep sequential synthesizer
- Maximum intelligence per token
- Focused, high-value analysis
"""

__version__ = "3.0.0"  # Updated for Intelligent MEZAN
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

# DeepThink agents (optimized: 3 parallel + 1 sequential)
from atlas_core.deepthink_agents import (
    DeepThinkOrchestrator,
    DeepTask,
    DeepResult,
    AnalysisDepth,
    AgentRole,
)

# Intelligent MEZAN (with deep reasoning)
from atlas_core.intelligent_mezan import (
    IntelligentMezanEngine,
    IntelligentSolverPair,
    create_intelligent_mezan,
)

# Causal Reasoning Engine (opus-level intelligence)
from atlas_core.causal_engine import (
    CausalReasoningEngine,
    CausalNode,
    CausalEdge,
    create_causal_engine,
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
    # Ultrathink agents (legacy - 5 teams)
    "UltrathinkOrchestrator",
    "AgentTask",
    "AgentResult",
    "TeamRole",
    "TaskPriority",
    "TaskStatus",
    # DeepThink agents (optimized - 3 parallel + 1 sequential)
    "DeepThinkOrchestrator",
    "DeepTask",
    "DeepResult",
    "AnalysisDepth",
    "AgentRole",
    # Intelligent MEZAN (with deep reasoning)
    "IntelligentMezanEngine",
    "IntelligentSolverPair",
    "create_intelligent_mezan",
    # Causal Reasoning Engine (opus-level)
    "CausalReasoningEngine",
    "CausalNode",
    "CausalEdge",
    "create_causal_engine",
    # MEZAN orchestrator
    "MezanOrchestrator",
    "OrchestratorConfig",
    "OrchestratorMode",
    "OrchestrationResult",
    "create_default_orchestrator",
]
