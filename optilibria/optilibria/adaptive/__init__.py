"""
Adaptive Learning System for Optilibria

This module provides sophisticated adaptive learning capabilities that learn from
optimization history and automatically improve method selection over time.

Key Components:
- Performance Database: SQLite storage of optimization runs
- Algorithm Portfolio Manager: Dynamic algorithm selection and resource allocation
- Online Learning System: Multi-armed bandits for method selection
- Meta-Learning: Transfer learning from similar problems
- Surrogate Models: Gaussian Process regression for expensive evaluations
- Ensemble Methods: Parallel algorithm execution with voting

Author: Meshal Alawein
Date: 2025-11-18
"""

from optilibria.adaptive.ensemble import EnsembleOptimizer
from optilibria.adaptive.meta_learning import MetaLearner, PerformancePredictor
from optilibria.adaptive.online_learning import (
    EXP3Selector,
    OnlineLearner,
    ThompsonSampler,
    UCB1Selector,
)
from optilibria.adaptive.performance_db import PerformanceDatabase
from optilibria.adaptive.portfolio import AlgorithmPortfolioManager
from optilibria.adaptive.surrogate import (
    AcquisitionFunction,
    GPSurrogate,
    SurrogateOptimizer,
)

__all__ = [
    # Database
    'PerformanceDatabase',
    # Portfolio
    'AlgorithmPortfolioManager',
    # Online Learning
    'OnlineLearner',
    'UCB1Selector',
    'ThompsonSampler',
    'EXP3Selector',
    # Meta-Learning
    'MetaLearner',
    'PerformancePredictor',
    # Surrogate Models
    'GPSurrogate',
    'SurrogateOptimizer',
    'AcquisitionFunction',
    # Ensemble
    'EnsembleOptimizer',
]