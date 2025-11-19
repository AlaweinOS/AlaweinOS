"""
FlowLibria - Confidence-Aware Workflow Routing for MEZAN

Routes research workflows through agent networks based on validation confidence
scores and quality objectives.

**Problem Type:** Workflow Routing with Confidence
**Use Case:** ATLAS research task routing through validation agents
**Target:** Maximize end-to-end workflow confidence
"""

__version__ = "1.0.0"

from .solver import FlowLibriaSolver

__all__ = ["FlowLibriaSolver"]
