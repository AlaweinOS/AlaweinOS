OptimizationProblem
===================

The ``OptimizationProblem`` class represents a complete optimization problem instance.

Class Definition
----------------

.. autoclass:: MEZAN.core.problem.OptimizationProblem
   :members:
   :undoc-members:
   :show-inheritance:
   :special-members: __init__

Attributes
----------

.. attribute:: problem_type

   Type of optimization problem (from ``ProblemType`` enum).

   :type: ProblemType

.. attribute:: data

   Problem-specific data dictionary. Required keys depend on problem type:

   * **QAP**: ``distance_matrix``, ``flow_matrix``
   * **FLOW**: ``workflow_graph``, ``confidence_scores``, ``start_node``, ``goal_node``
   * **ALLOC**: ``num_agents``, ``budget``
   * **GRAPH**: ``num_nodes``, ``optimization_criterion``
   * **DUAL**: ``objective_functions``, ``num_variables``
   * **EVO**: ``objective_functions``, ``num_variables``, ``variable_bounds``
   * **META**: ``problem_features``, ``algorithm_pool``

   :type: dict

.. attribute:: constraints

   Optional constraints dictionary.

   :type: dict, optional

.. attribute:: metadata

   Optional metadata for tracking and logging.

   :type: dict, optional

Problem Types
-------------

.. autoclass:: MEZAN.core.problem.ProblemType
   :members:
   :undoc-members:

Supported problem types:

* **QAP** - Quadratic Assignment Problem
* **FLOW** - Workflow routing optimization
* **ALLOC** - Resource allocation
* **GRAPH** - Network topology optimization
* **DUAL** - Robust min-max optimization
* **EVO** - Multi-objective optimization
* **META** - Automatic solver selection

Validation
----------

The ``OptimizationProblem`` class validates input data based on problem type:

.. code-block:: python

   # This will validate that distance_matrix and flow_matrix exist
   problem = OptimizationProblem(
       problem_type=ProblemType.QAP,
       data={
           "distance_matrix": [[0, 10], [10, 0]],
           "flow_matrix": [[0, 5], [5, 0]]
       }
   )

   # This will raise ValueError (missing required keys)
   bad_problem = OptimizationProblem(
       problem_type=ProblemType.QAP,
       data={"distance_matrix": [[0, 10], [10, 0]]}  # Missing flow_matrix
   )

Examples by Problem Type
------------------------

QAP (Quadratic Assignment)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   problem = OptimizationProblem(
       problem_type=ProblemType.QAP,
       data={
           "distance_matrix": distance_matrix,  # n x n symmetric matrix
           "flow_matrix": flow_matrix  # n x n matrix of interactions
       },
       constraints={
           "algorithm": "simulated_annealing",  # or "genetic_algorithm"
           "max_iterations": 1000,
           "temperature": 1000.0
       }
   )

FLOW (Workflow Routing)
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   problem = OptimizationProblem(
       problem_type=ProblemType.FLOW,
       data={
           "workflow_graph": {
               "nodes": ["A", "B", "C", "D"],
               "edges": [("A", "B"), ("B", "C"), ("C", "D"), ("A", "D")]
           },
           "confidence_scores": {"A": 0.9, "B": 0.7, "C": 0.8, "D": 0.95},
           "start_node": "A",
           "goal_node": "D"
       }
   )

ALLOC (Resource Allocation)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   problem = OptimizationProblem(
       problem_type=ProblemType.ALLOC,
       data={
           "num_agents": 10,
           "budget": 0.6  # 60% of resources
       },
       constraints={
           "exploration_weight": 2.0  # Thompson Sampling exploration
       }
   )

EVO (Multi-Objective)
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   def speed_obj(x):
       return x[0]**2 + x[1]**2

   def quality_obj(x):
       return -x[0] - x[1]

   problem = OptimizationProblem(
       problem_type=ProblemType.EVO,
       data={
           "objective_functions": [speed_obj, quality_obj],
           "num_variables": 2,
           "variable_bounds": (0.0, 10.0)
       },
       constraints={
           "population_size": 100,
           "num_generations": 50
       }
   )
