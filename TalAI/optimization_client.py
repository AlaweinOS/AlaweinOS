"""tal-ai level optimization client facade.

This module provides a unified, *optional* interface over:

- Turingo (multi-paradigm optimization rodeo)
- Optilibria (universal optimization framework)

It is designed to be lightweight and defensive:
- If a dependency is not importable in the current environment, the
  corresponding function will raise a clear ImportError when called.
- Callers can feature-detect availability using the helper flags.
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Turingo integration
# ---------------------------------------------------------------------------

try:  # Prefer local module when running inside the turingo repo
    from turingo_client import async_solve as _turingo_async_solve, solve as _turingo_solve
except ImportError:  # pragma: no cover - path-dependent
    try:
        # Fallback if turingo is treated as a package
        from turingo.turingo_client import async_solve as _turingo_async_solve, solve as _turingo_solve
    except ImportError:  # pragma: no cover - defensive
        _turingo_async_solve = None  # type: ignore[assignment]
        _turingo_solve = None  # type: ignore[assignment]


HAS_TURINGO: bool = _turingo_async_solve is not None  # type: ignore[name-defined]


async def turingo_async_solve(
    problem_type: str,
    instance: str,
    *,
    paradigms: Optional[List[str]] = None,
    time_limit_hours: float = 2.0,
    validation_level: str = "rigorous",
    config_path: Optional[str] = None,
) -> Any:
    """Async wrapper around Turingo's `async_solve`.

    Raises ImportError if Turingo is not available in this environment.
    """

    if not HAS_TURINGO or _turingo_async_solve is None:
        raise ImportError(
            "Turingo is not available on PYTHONPATH. Ensure that the turingo "
            "project is installed or that its directory is on sys.path."
        )

    return await _turingo_async_solve(
        problem_type=problem_type,
        instance=instance,
        paradigms=paradigms,
        time_limit_hours=time_limit_hours,
        validation_level=validation_level,
        config_path=config_path,
    )


def turingo_solve(
    problem_type: str,
    instance: str,
    *,
    paradigms: Optional[List[str]] = None,
    time_limit_hours: float = 2.0,
    validation_level: str = "rigorous",
    config_path: Optional[str] = None,
) -> Any:
    """Sync wrapper around Turingo's `async_solve`.

    Useful for scripts or environments without an existing event loop.
    """

    if not HAS_TURINGO or _turingo_solve is None:
        raise ImportError(
            "Turingo is not available on PYTHONPATH. Ensure that the turingo "
            "project is installed or that its directory is on sys.path."
        )

    return _turingo_solve(
        problem_type=problem_type,
        instance=instance,
        paradigms=paradigms,
        time_limit_hours=time_limit_hours,
        validation_level=validation_level,
        config_path=config_path,
    )


# ---------------------------------------------------------------------------
# Optilibria integration
# ---------------------------------------------------------------------------

try:
    # Local sibling helper (if this repo is on sys.path)
    from optilibria_client import (
        optimize_problem as _optimize_problem,
        optimize_qap_problem as _optimize_qap_problem,
    )
except ImportError:  # pragma: no cover - path-dependent
    try:
        # If Optilibria is installed as a package and exposes its client
        from optilibria.optilibria_client import (
            optimize_problem as _optimize_problem,
            optimize_qap_problem as _optimize_qap_problem,
        )
    except ImportError:  # pragma: no cover - defensive
        _optimize_problem = None  # type: ignore[assignment]
        _optimize_qap_problem = None  # type: ignore[assignment]


HAS_OPTILIBRIA: bool = _optimize_problem is not None  # type: ignore[name-defined]


def optimize_problem(
    problem: Any,
    adapter: Any,
    *,
    method: str,
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Unified entry to Optilibria's universal optimizer.

    Delegates to `optilibria_client.optimize_problem` when available.
    Raises ImportError if Optilibria is not available.
    """

    if not HAS_OPTILIBRIA or _optimize_problem is None:
        raise ImportError(
            "Optilibria is not available on PYTHONPATH. Install Optilibria or "
            "ensure its repo (with optilibria_client.py) is on sys.path."
        )

    return _optimize_problem(problem, adapter, method=method, config=config)


def optimize_qap(
    flow_matrix: Any,
    distance_matrix: Any,
    *,
    method: str = "simulated_annealing",
    config: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Unified entry to Optilibria's QAP optimizer.

    Delegates to `optilibria_client.optimize_qap_problem` when available.
    Raises ImportError if Optilibria is not available.
    """

    if not HAS_OPTILIBRIA or _optimize_qap_problem is None:
        raise ImportError(
            "Optilibria is not available on PYTHONPATH. Install Optilibria or "
            "ensure its repo (with optilibria_client.py) is on sys.path."
        )

    return _optimize_qap_problem(flow_matrix, distance_matrix, method=method, config=config)


__all__ = [
    "HAS_TURINGO",
    "HAS_OPTILIBRIA",
    "turingo_async_solve",
    "turingo_solve",
    "optimize_problem",
    "optimize_qap",
]
