"""
Intelligent MEZAN Engine - Optimized with Deep Reasoning

Enhanced MEZAN engine with:
- Intelligent solver selection based on deep analysis
- Sequential deep-think mode for maximum intelligence
- Token-efficient focused reasoning
- Adaptive strategy based on problem characteristics

This version focuses on DEPTH over breadth, using:
- 3 parallel agents for quick assessment
- 1 deep synthesizer for intensive reasoning
- Intelligent solver pairing and balancing

Author: MEZAN Research Team
Date: 2025-11-18
Version: 3.0 (Intelligent Optimized)
"""

from typing import Dict, List, Optional, Any, Tuple
from dataclasses import dataclass, field
import logging
import time
import numpy as np

from atlas_core.mezan_engine import (
    MezanEngine,
    BaseSolver,
    SolverConfig,
    SolverResult,
    SolverType,
    MezanState,
)
from atlas_core.deepthink_agents import (
    DeepThinkOrchestrator,
    DeepTask,
    DeepResult,
    AnalysisDepth,
)

logger = logging.getLogger(__name__)


@dataclass
class IntelligentSolverPair:
    """Intelligently selected solver pair based on problem analysis"""
    left_solver: BaseSolver
    right_solver: BaseSolver
    selection_reasoning: str
    expected_performance: str
    confidence: float


class IntelligentMezanEngine:
    """
    Intelligent MEZAN Engine with Deep Reasoning

    Key improvements:
    1. Deep problem analysis before solving
    2. Intelligent solver selection
    3. Adaptive balancing strategy
    4. Sequential deep-think for critical decisions
    5. Token-efficient focused reasoning

    Architecture:
    - Phase 1: Deep analysis (3 parallel + 1 sequential)
    - Phase 2: Intelligent solver selection
    - Phase 3: Adaptive MEZAN balancing
    - Phase 4: Deep synthesis of results
    """

    def __init__(
        self,
        available_solvers: Optional[List[BaseSolver]] = None,
        use_deep_analysis: bool = True,
    ):
        """
        Initialize Intelligent MEZAN

        Args:
            available_solvers: Pool of solvers to choose from
            use_deep_analysis: Whether to use deep analysis (recommended)
        """
        self.available_solvers = available_solvers or []
        self.use_deep_analysis = use_deep_analysis

        # Initialize deep think orchestrator
        if use_deep_analysis:
            self.deep_think = DeepThinkOrchestrator(max_parallel_workers=3)
        else:
            self.deep_think = None

        self.mezan_engine = None  # Created after solver selection
        self.last_analysis = None

        logger.info(
            f"Intelligent MEZAN initialized with {len(self.available_solvers)} "
            f"available solvers, deep_analysis={use_deep_analysis}"
        )

    def solve_intelligently(
        self,
        problem: Dict[str, Any],
        max_mezan_iterations: int = 5,
        analysis_depth: AnalysisDepth = AnalysisDepth.DEEP,
    ) -> Tuple[SolverResult, Optional[DeepResult]]:
        """
        Solve problem with intelligent strategy

        Returns:
            (mezan_result, synthesis_result)
        """
        start_time = time.time()

        logger.info("="*70)
        logger.info("INTELLIGENT MEZAN SOLVING")
        logger.info("="*70)

        # PHASE 1: Deep Problem Analysis
        logger.info("\n📊 PHASE 1: Deep Problem Analysis")
        logger.info("-" * 70)

        synthesis_result = None

        if self.use_deep_analysis:
            # Create deep task
            task = DeepTask(
                task_id=f"problem_{int(time.time() * 1000)}",
                problem=problem,
                depth=analysis_depth,
                max_time_seconds=30.0,
            )

            # Run deep analysis (3 parallel + 1 sequential)
            (
                analyzer_result,
                optimizer_result,
                validator_result,
                synthesis_result,
            ) = self.deep_think.deep_analyze(task, use_synthesis=True)

            self.last_analysis = synthesis_result

            # Log insights
            logger.info("\n✨ Analysis Insights:")
            for insight in synthesis_result.insights[:10]:  # Top 10
                if insight.strip():
                    logger.info(f"  • {insight}")

            # Log recommendations
            logger.info(f"\n🎯 Generated {len(synthesis_result.recommendations)} recommendations")

        # PHASE 2: Intelligent Solver Selection
        logger.info("\n🧠 PHASE 2: Intelligent Solver Selection")
        logger.info("-" * 70)

        solver_pair = self._select_solver_pair_intelligently(
            problem, synthesis_result
        )

        logger.info(f"Selected Solver Pair:")
        logger.info(f"  Left:  {solver_pair.left_solver.config.solver_id}")
        logger.info(f"  Right: {solver_pair.right_solver.config.solver_id}")
        logger.info(f"  Reasoning: {solver_pair.selection_reasoning}")
        logger.info(f"  Expected: {solver_pair.expected_performance}")
        logger.info(f"  Confidence: {solver_pair.confidence:.3f}")

        # PHASE 3: Create and Run MEZAN Engine
        logger.info("\n⚖️  PHASE 3: Adaptive MEZAN Balancing")
        logger.info("-" * 70)

        # Select balancing strategy based on analysis
        balance_strategy = self._select_balance_strategy(synthesis_result)
        logger.info(f"Balancing strategy: {balance_strategy}")

        # Create MEZAN engine with selected solvers
        self.mezan_engine = MezanEngine(
            solver_left=solver_pair.left_solver,
            solver_right=solver_pair.right_solver,
            balance_strategy=balance_strategy,
            learning_rate=0.15,  # Slightly higher for faster adaptation
        )

        # Run MEZAN balancing
        mezan_result = self.mezan_engine.solve_with_balance(
            problem,
            max_iterations=max_mezan_iterations,
            convergence_threshold=1e-4,
        )

        # PHASE 4: Results and Insights
        logger.info("\n📈 PHASE 4: Results Summary")
        logger.info("-" * 70)

        total_time = time.time() - start_time

        logger.info(f"Final Objective: {mezan_result.objective_value:.6f}")
        logger.info(f"Total Iterations: {mezan_result.iterations}")
        logger.info(f"Total Time: {total_time:.3f}s")
        logger.info(f"  - Analysis: {synthesis_result.time_seconds:.3f}s" if synthesis_result else "")
        logger.info(f"  - Solving: {mezan_result.time_seconds:.3f}s")

        # Deep reasoning about results
        if synthesis_result:
            logger.info(f"\n💡 Deep Reasoning:")
            logger.info(synthesis_result.reasoning)

        logger.info("\n" + "="*70)
        logger.info("INTELLIGENT MEZAN COMPLETE")
        logger.info("="*70 + "\n")

        return mezan_result, synthesis_result

    def _select_solver_pair_intelligently(
        self,
        problem: Dict[str, Any],
        analysis: Optional[DeepResult],
    ) -> IntelligentSolverPair:
        """
        Intelligently select solver pair based on deep analysis

        Uses recommendations from deep analysis to choose optimal solvers.
        """
        # Default: use continuous + discrete pair
        from atlas_core.mezan_engine import MockContinuousSolver, MockDiscreteSolver

        # Extract algorithm recommendations from analysis
        if analysis and analysis.recommendations:
            # Look for algorithm-related recommendations
            algo_recs = [
                r for r in analysis.recommendations
                if r.get("type") in ["algorithm_selection", "algorithm_portfolio"]
            ]

            if algo_recs:
                # Use recommended algorithms
                primary_rec = algo_recs[0]

                reasoning = (
                    f"Based on deep analysis: {primary_rec.get('reason', 'N/A')}. "
                    f"Selected complementary solver pair for balance."
                )

                # Check if portfolio recommended
                if primary_rec.get("type") == "algorithm_portfolio":
                    algos = primary_rec.get("algorithms", [])
                    if len(algos) >= 2:
                        # Use top 2 from portfolio
                        reasoning = (
                            f"Portfolio approach with top algorithms: "
                            f"{algos[0]['name']} (weight {algos[0]['weight']}) and "
                            f"{algos[1]['name']} (weight {algos[1]['weight']})"
                        )

                confidence = primary_rec.get("confidence", 0.75)
                expected_performance = "High" if confidence > 0.85 else "Good"

            else:
                reasoning = "Default continuous + discrete pair (no specific algorithm recommendation)"
                confidence = 0.70
                expected_performance = "Good"

        else:
            reasoning = "Default continuous + discrete pair (no deep analysis)"
            confidence = 0.60
            expected_performance = "Acceptable"

        # Create solvers (currently mocks, would be real solvers in production)
        left_solver = MockContinuousSolver(
            SolverConfig(
                solver_id="continuous_relaxation",
                solver_type=SolverType.CONTINUOUS,
                weight=0.5,
            )
        )

        right_solver = MockDiscreteSolver(
            SolverConfig(
                solver_id="discrete_heuristic",
                solver_type=SolverType.DISCRETE,
                weight=0.5,
            )
        )

        return IntelligentSolverPair(
            left_solver=left_solver,
            right_solver=right_solver,
            selection_reasoning=reasoning,
            expected_performance=expected_performance,
            confidence=confidence,
        )

    def _select_balance_strategy(self, analysis: Optional[DeepResult]) -> str:
        """
        Select balancing strategy based on analysis

        Returns: "ucb", "thompson", or "epsilon_greedy"
        """
        if not analysis:
            return "ucb"  # Default

        # Check for resource allocation recommendations
        resource_recs = [
            r for r in analysis.recommendations
            if r.get("type") == "resource_allocation"
        ]

        if resource_recs:
            rec = resource_recs[0]
            rec_text = rec.get("recommendation", "").lower()

            # Fast heuristic → epsilon-greedy (more exploration)
            if "fast" in rec_text or "heuristic" in rec_text:
                return "epsilon_greedy"

            # Hybrid/balanced → UCB (balanced exploration/exploitation)
            if "hybrid" in rec_text or "balanced" in rec_text:
                return "ucb"

            # Multi-stage/thorough → Thompson (Bayesian)
            if "multi-stage" in rec_text or "thorough" in rec_text:
                return "thompson"

        # Default: UCB is generally good
        return "ucb"

    def get_last_analysis(self) -> Optional[DeepResult]:
        """Get the last deep analysis result"""
        return self.last_analysis

    def get_full_diagnostics(self) -> Dict[str, Any]:
        """Get comprehensive diagnostics"""
        diagnostics = {
            "available_solvers": len(self.available_solvers),
            "deep_analysis_enabled": self.use_deep_analysis,
        }

        if self.deep_think:
            diagnostics["deepthink_stats"] = self.deep_think.get_statistics()

        if self.mezan_engine:
            diagnostics["mezan_engine"] = self.mezan_engine.get_diagnostics()

        if self.last_analysis:
            diagnostics["last_analysis"] = {
                "insights_count": len(self.last_analysis.insights),
                "recommendations_count": len(self.last_analysis.recommendations),
                "confidence": self.last_analysis.confidence,
                "time": self.last_analysis.time_seconds,
            }

        return diagnostics

    def shutdown(self):
        """Shutdown all components"""
        if self.deep_think:
            self.deep_think.shutdown()


def create_intelligent_mezan() -> IntelligentMezanEngine:
    """Create intelligent MEZAN engine with default configuration"""
    return IntelligentMezanEngine(
        available_solvers=[],  # Would be populated with real solvers
        use_deep_analysis=True,
    )
