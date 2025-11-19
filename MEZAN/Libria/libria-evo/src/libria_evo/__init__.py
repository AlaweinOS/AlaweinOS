"""
EvoLibria - Evolutionary Multi-Objective Optimization

Handles MEZAN workflows with conflicting objectives (speed vs quality vs cost)
using evolutionary algorithms (NSGA-II).

**Problem Type:** Multi-Objective Optimization
**Use Case:** Balancing speed, quality, and cost in ATLAS research workflows
**Target:** Pareto frontier discovery
"""

__version__ = "1.0.0"

from .solver import EvoLibriaSolver

__all__ = ["EvoLibriaSolver"]
