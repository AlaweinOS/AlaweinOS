"""
DualLibria - Adversarial Min-Max Robust Optimization

Ensures MEZAN workflows are robust under worst-case adversarial scenarios
(agent failures, network partitions, etc.).

**Problem Type:** Min-Max Robust Optimization
**Use Case:** Robust ATLAS workflow design with failure tolerance
**Target:** Minimize worst-case performance
"""

__version__ = "1.0.0"

from .solver import DualLibriaSolver

__all__ = ["DualLibriaSolver"]
