"""
Core optimization interface for Optilibria

This module provides the main optimize() function that serves as the
universal entry point for optimization across all domains and methods.
"""

import logging
from typing import Any, Dict, Optional, Union

import numpy as np

from optilibria.core.interfaces import (
    StandardizedProblem,
    StandardizedSolution,
    UniversalOptimizationInterface,
)

logger = logging.getLogger(__name__)


def optimize(
    problem: Union[Dict[str, Any], StandardizedProblem],
    adapter: Optional[UniversalOptimizationInterface] = None,
    method: str = 'simulated_annealing',
    config: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Universal optimization function - main entry point for Optilibria

    Args:
        problem: Either a domain-specific problem dict or StandardizedProblem
        adapter: Domain adapter (required if problem is dict)
        method: Optimization method name. Options:
            - 'random_search': Baseline random sampling
            - 'simulated_annealing': Simulated annealing metaheuristic
            - 'local_search': Hill climbing with restarts
            - 'genetic_algorithm': Population-based evolutionary algorithm
            - 'tabu_search': Memory-based local search
        config: Method-specific configuration parameters

    Returns:
        dict: Optimization result with keys:
            - 'solution': Best solution found
            - 'objective': Objective value
            - 'is_valid': Whether solution satisfies constraints
            - 'iterations': Number of iterations performed
            - 'convergence': Convergence information
            - 'metadata': Additional method-specific metadata

    Raises:
        ValueError: If adapter is None when problem is dict
        NotImplementedError: If method is not implemented

    Example:
        >>> from optilibria import optimize
        >>> from optilibria.adapters.qap import QAPAdapter
        >>> import numpy as np
        >>>
        >>> problem = {
        ...     'flow_matrix': np.array([[0, 5], [5, 0]]),
        ...     'distance_matrix': np.array([[0, 8], [8, 0]])
        ... }
        >>> adapter = QAPAdapter()
        >>> result = optimize(problem, adapter, method='simulated_annealing')
        >>> print(result['objective'])
    """
    # Set default config
    if config is None:
        config = {}

    # Encode problem if needed
    if isinstance(problem, dict):
        if adapter is None:
            raise ValueError(
                "adapter must be provided when problem is a dictionary. "
                "Use a domain adapter like QAPAdapter or TSPAdapter."
            )
        standardized_problem = adapter.encode_problem(problem)
    else:
        standardized_problem = problem

    # Select and run optimization method
    if method == 'random_search':
        from optilibria.methods.baselines.random_search import random_search_optimize
        result = random_search_optimize(standardized_problem, config)
    elif method == 'simulated_annealing':
        from optilibria.methods.baselines.simulated_annealing import (
            simulated_annealing_optimize,
        )
        result = simulated_annealing_optimize(standardized_problem, config)
    elif method == 'local_search':
        from optilibria.methods.baselines.local_search import local_search_optimize
        result = local_search_optimize(standardized_problem, config)
    elif method == 'genetic_algorithm':
        from optilibria.methods.baselines.genetic_algorithm import (
            genetic_algorithm_optimize,
        )
        result = genetic_algorithm_optimize(standardized_problem, config)
    elif method == 'tabu_search':
        from optilibria.methods.baselines.tabu_search import tabu_search_optimize
        result = tabu_search_optimize(standardized_problem, config)
    else:
        raise NotImplementedError(
            f"Method '{method}' is not implemented. "
            f"Available methods: random_search, simulated_annealing, "
            f"local_search, genetic_algorithm, tabu_search"
        )

    # Decode solution if adapter provided
    if adapter is not None and 'solution' in result:
        solution_obj = StandardizedSolution(
            vector=result['solution'],
            objective_value=result['objective'],
            is_valid=result.get('is_valid', True),
            metadata=result.get('metadata', {})
        )
        result['solution'] = adapter.decode_solution(solution_obj)

    logger.info(
        f"Optimization complete: method={method}, "
        f"objective={result.get('objective', 'N/A')}, "
        f"iterations={result.get('iterations', 'N/A')}"
    )

    return result


__all__ = ['optimize']
