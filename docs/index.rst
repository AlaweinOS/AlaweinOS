MEZAN V4.1.0 - API Documentation
===================================

**Modular Enterprise Zonal Automation Network**

Version 4.1.0 - Enterprise-Grade Multi-Agent Optimization Framework

.. image:: https://img.shields.io/badge/version-4.1.0-blue.svg
   :alt: Version

.. image:: https://img.shields.io/badge/python-3.9+-blue.svg
   :alt: Python Version

.. image:: https://img.shields.io/badge/license-Apache%202.0-green.svg
   :alt: License

Overview
--------

MEZAN is an enterprise-grade optimization framework that combines 7 novel Libria solvers
with the ATLAS multi-agent orchestration engine to solve complex optimization problems
at scale.

**Key Features:**

* 7 production-ready Libria optimization solvers
* ATLAS multi-agent research orchestration
* GPU acceleration support (CUDA 11.8)
* Feature flags for gradual rollout
* Comprehensive monitoring (Prometheus + Grafana)
* Production infrastructure (Docker + Kubernetes)

Architecture
------------

.. code-block:: text

   MEZAN V4.1.0
   ├── Core Integration Layer
   │   ├── OptimizationProblem
   │   ├── ProblemType
   │   ├── OptimizerFactory
   │   └── Feature Flags
   │
   ├── Libria Suite (7 Solvers)
   │   ├── QAPLibria - Quadratic Assignment Problem
   │   ├── FlowLibria - Confidence-Aware Workflow Routing
   │   ├── AllocLibria - Thompson Sampling Resource Allocation
   │   ├── GraphLibria - Information-Theoretic Network Topology
   │   ├── DualLibria - Adversarial Robust Optimization
   │   ├── EvoLibria - Multi-Objective NSGA-II
   │   └── MetaLibria - Automatic Solver Selection (UCB)
   │
   └── ATLAS Engine
       ├── Multi-Agent Orchestration
       ├── Research Workflow Management
       └── Redis Blackboard State

Quick Start
-----------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from MEZAN.core import OptimizationProblem, ProblemType, OptimizerFactory

   # Create optimization problem
   problem = OptimizationProblem(
       problem_type=ProblemType.QAP,
       data={
           "distance_matrix": [[0, 10], [10, 0]],
           "flow_matrix": [[0, 5], [5, 0]]
       }
   )

   # Create optimizer with feature flags
   factory = OptimizerFactory(config={
       "feature_flags": {
           "enable_qap_libria": True,
           "enable_gpu_acceleration": False
       }
   })

   optimizer = factory.create_optimizer(problem, timeout=10.0)

   # Solve problem
   result = optimizer.solve(problem)
   print(f"Status: {result.status}")
   print(f"Solution: {result.solution}")

With GPU Acceleration
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   factory = OptimizerFactory(config={
       "feature_flags": {
           "enable_qap_libria": True,
           "enable_gpu_acceleration": True
       }
   })

   optimizer = factory.create_optimizer(problem)
   result = optimizer.solve(problem)

ATLAS Multi-Agent Orchestration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from MEZAN.ATLAS.atlas_core.engine import ATLASEngine
   from MEZAN.ATLAS.atlas_core.agents import create_synthesis_agent

   # Initialize ATLAS engine
   engine = ATLASEngine()

   # Create and register agents
   synthesis_agent = create_synthesis_agent()
   engine.register_agent(synthesis_agent)

   # Submit research task
   task_id = engine.submit_task({
       "type": "research_synthesis",
       "data": {"papers": [...], "focus": "optimization"}
   })

   # Get results
   result = engine.get_task_result(task_id)

Production Deployment
---------------------

Docker Compose
~~~~~~~~~~~~~~

.. code-block:: bash

   cd docker
   docker-compose up -d

   # With GPU support
   docker-compose --profile gpu up -d

Kubernetes
~~~~~~~~~~

.. code-block:: bash

   kubectl apply -f k8s/mezan-deployment.yaml
   kubectl apply -f k8s/monitoring.yaml

   # Check status
   kubectl get pods -n mezan

API Reference
-------------

.. toctree::
   :maxdepth: 2
   :caption: Core Components

   api/core
   api/problem
   api/factory
   api/status

.. toctree::
   :maxdepth: 2
   :caption: Libria Solvers

   api/libria_qap
   api/libria_flow
   api/libria_alloc
   api/libria_graph
   api/libria_dual
   api/libria_evo
   api/libria_meta

.. toctree::
   :maxdepth: 2
   :caption: ATLAS Engine

   api/atlas_engine
   api/atlas_agents
   api/atlas_blackboard

.. toctree::
   :maxdepth: 2
   :caption: Visualization

   api/visualization

.. toctree::
   :maxdepth: 2
   :caption: Infrastructure

   deployment
   monitoring
   benchmarks
   testing

Performance
-----------

Benchmark Results (QAPLIB)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Problem Type    Size    Solver      Time (s)    Optimality Gap
   ================================================================
   QAP            5       SA          0.0123      5%
   QAP            10      GA          0.0456      8%
   QAP            15      SA          0.1234      12%
   QAP            20      GA          0.3456      15%

   FLOW           5       Dijkstra    0.0001      0%
   FLOW           10      Dijkstra    0.0003      0%
   FLOW           15      Dijkstra    0.0006      0%
   FLOW           20      Dijkstra    0.0012      0%

   ALLOC          5       Thompson    0.0023      10%
   ALLOC          10      Thompson    0.0067      12%
   ALLOC          15      Thompson    0.0134      15%
   ALLOC          20      Thompson    0.0289      18%

Monitoring & Observability
---------------------------

Prometheus Metrics
~~~~~~~~~~~~~~~~~~

.. code-block:: promql

   # Solver execution rate
   rate(libria_qap_solve_duration_seconds_count[5m])

   # P95 latency
   histogram_quantile(0.95, rate(libria_qap_solve_duration_seconds_bucket[5m]))

   # GPU utilization
   libria_qap_gpu_utilization_percent

Grafana Dashboards
~~~~~~~~~~~~~~~~~~

* **MEZAN Overview**: 13 panels covering all 7 solvers
* **Solver Performance**: Latency percentiles (P50/P95/P99)
* **Meta-Learning**: UCB scores, cumulative regret
* **Multi-Objective**: Pareto front size, hypervolume indicator
* **System Health**: CPU, memory, GPU utilization

Contributing
------------

See `CONTRIBUTING.md <https://github.com/AlaweinOS/AlaweinOS/blob/main/CONTRIBUTING.md>`_
for development guidelines.

License
-------

Apache License 2.0 - See `LICENSE <https://github.com/AlaweinOS/AlaweinOS/blob/main/LICENSE>`_

Contact
-------

* **Author:** Meshal Alawein
* **Email:** meshal@berkeley.edu
* **Portfolio:** https://malawein.com
* **GitHub:** https://github.com/AlaweinOS/AlaweinOS

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
