Core Module
===========

The MEZAN core module provides the foundational classes and interfaces for the optimization framework.

Overview
--------

The core module includes:

* ``OptimizationProblem`` - Problem definition and validation
* ``ProblemType`` - Enum of supported problem types
* ``SolverStatus`` - Result status codes
* ``OptimizerFactory`` - Factory for creating optimizers
* ``OptimizationResult`` - Standardized result structure

Classes
-------

.. automodule:: MEZAN.core.problem
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: MEZAN.core.factory
   :members:
   :undoc-members:
   :show-inheritance:

.. automodule:: MEZAN.core.optimizer
   :members:
   :undoc-members:
   :show-inheritance:

Example Usage
-------------

Creating a Problem
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from MEZAN.core import OptimizationProblem, ProblemType

   problem = OptimizationProblem(
       problem_type=ProblemType.QAP,
       data={
           "distance_matrix": [[0, 10, 20], [10, 0, 15], [20, 15, 0]],
           "flow_matrix": [[0, 5, 3], [5, 0, 2], [3, 2, 0]]
       },
       constraints={"max_iterations": 1000}
   )

Using the Factory
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from MEZAN.core import OptimizerFactory

   factory = OptimizerFactory(config={
       "feature_flags": {
           "enable_all_libria": True,
           "enable_gpu_acceleration": True
       },
       "default_timeout": 30.0
   })

   optimizer = factory.create_optimizer(problem, timeout=10.0)
   result = optimizer.solve(problem)

Checking Results
~~~~~~~~~~~~~~~~

.. code-block:: python

   from MEZAN.core import SolverStatus

   if result.status == SolverStatus.OPTIMAL:
       print(f"Optimal solution found: {result.solution}")
       print(f"Objective value: {result.objective_value}")
       print(f"Computation time: {result.computation_time}s")
   elif result.status == SolverStatus.FEASIBLE:
       print(f"Feasible solution found (not proven optimal)")
   else:
       print(f"Solver failed: {result.status}")
       print(f"Message: {result.message}")
