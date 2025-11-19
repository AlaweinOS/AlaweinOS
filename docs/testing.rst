Testing
=======

MEZAN V4.1.0 includes comprehensive test suite with 103+ test files.

Test Structure
--------------

.. code-block:: text

   tests/
   ├── MEZAN/core/tests/
   │   └── test_integration_layer.py (21 tests) ✅
   │
   ├── MEZAN/ATLAS/atlas-core/tests/
   │   ├── test_agents.py (8 tests) ✅
   │   ├── test_engine.py (6 tests, 5 require Redis)
   │   ├── test_auth.py
   │   ├── test_monitoring.py
   │   └── integration/
   │       ├── test_end_to_end_workflow.py
   │       ├── test_distributed_execution.py
   │       └── ...
   │
   └── MEZAN/Libria/*/tests/
       ├── libria-qap/tests/test_solver.py
       ├── libria-flow/tests/test_solver.py
       ├── libria-alloc/tests/test_solver.py
       ├── libria-dual/tests/test_solver.py
       ├── libria-evo/tests/test_solver.py
       ├── libria-graph/tests/test_solver.py
       └── libria-meta/tests/
           ├── test_meta_solver.py
           ├── test_aslib_parser.py
           └── test_qaplibria_backend_matrices.py

Running Tests
-------------

All Tests
~~~~~~~~~

.. code-block:: bash

   export PYTHONPATH=/home/user/AlaweinOS:$PYTHONPATH
   pytest MEZAN/ -v

Core Integration Layer
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pytest MEZAN/core/tests/test_integration_layer.py -v

**Expected:** 21/21 passing

ATLAS Agents
~~~~~~~~~~~~

.. code-block:: bash

   pytest MEZAN/ATLAS/atlas-core/tests/test_agents.py -v

**Expected:** 8/8 passing

ATLAS Engine (Requires Redis)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Start Redis first
   docker run -d --name mezan-redis -p 6379:6379 redis:7-alpine

   # Run tests
   pytest MEZAN/ATLAS/atlas-core/tests/test_engine.py -v

**Expected:** 6/6 passing (with Redis)

Libria Solvers
~~~~~~~~~~~~~~

.. code-block:: bash

   # Install solvers first
   cd MEZAN/Libria/libria-qap && pip install -e . && cd -

   # Run tests
   pytest MEZAN/Libria/libria-qap/tests/ -v

With Coverage
~~~~~~~~~~~~~

.. code-block:: bash

   # Install pytest-cov
   pip install pytest-cov

   # Run with coverage
   pytest MEZAN/ --cov=MEZAN --cov-report=html --cov-report=term

   # View HTML report
   open htmlcov/index.html

Test Results
------------

Current Status
~~~~~~~~~~~~~~

.. code-block:: text

   Component               Tests    Passed    Failed    Blocked
   ===============================================================
   MEZAN Core              21       21        0         0
   ATLAS Agents            8        8         0         0
   ATLAS Engine            6        1         0         5 (Redis)
   Libria Solvers          ?        0         0         ? (install)
   ───────────────────────────────────────────────────────────────
   TOTAL                   35+      29        0         5+

   Overall Status: 🟢 CORE FUNCTIONAL

Coverage Analysis
~~~~~~~~~~~~~~~~~

.. code-block:: text

   Component                    Coverage    Target
   ==================================================
   MEZAN Core Integration       ~85%        90%
   ATLAS Agents                 ~70%        80%
   ATLAS Engine                 ~30%        70%
   Libria Solvers               TBD         80%

CI/CD Integration
-----------------

GitHub Actions Workflow
~~~~~~~~~~~~~~~~~~~~~~~

``.github/workflows/mezan-ci.yml`` runs 10 parallel jobs:

1. **Lint** - Black, Ruff, mypy
2. **Test Integration Layer** - 21 core tests
3. **Test Libria Meta** - Meta-learning tests
4. **QAPLIB Benchmarks** - Performance tests
5. **Performance Profiling** - CPU/Memory analysis
6. **Regression Detection** - Performance alerts
7. **Build Docs** - Sphinx documentation
8. **Docker Build** - Multi-platform images
9. **Security Scan** - Trivy + Bandit
10. **Summary** - Workflow summary

Test Matrix
~~~~~~~~~~~

.. code-block:: yaml

   strategy:
     matrix:
       python-version: [3.9, 3.10, 3.11, 3.12]
       os: [ubuntu-latest, windows-latest, macos-latest]

Writing Tests
-------------

Unit Test Example
~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from MEZAN.core import OptimizationProblem, ProblemType

   def test_create_qap_problem():
       \"\"\"Test QAP problem creation\"\"\"
       problem = OptimizationProblem(
           problem_type=ProblemType.QAP,
           data={
               "distance_matrix": [[0, 10], [10, 0]],
               "flow_matrix": [[0, 5], [5, 0]]
           }
       )

       assert problem.problem_type == ProblemType.QAP
       assert "distance_matrix" in problem.data
       assert len(problem.data["distance_matrix"]) == 2

   def test_invalid_qap_problem():
       \"\"\"Test QAP validation\"\"\"
       with pytest.raises(ValueError):
           OptimizationProblem(
               problem_type=ProblemType.QAP,
               data={"distance_matrix": [[0, 10], [10, 0]]}
               # Missing flow_matrix
           )

Integration Test Example
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from MEZAN.core import OptimizerFactory, OptimizationProblem, ProblemType

   def test_end_to_end_qap_solve():
       \"\"\"Test complete QAP solve workflow\"\"\"
       # Create problem
       problem = OptimizationProblem(
           problem_type=ProblemType.QAP,
           data={
               "distance_matrix": [[0, 10, 20], [10, 0, 15], [20, 15, 0]],
               "flow_matrix": [[0, 5, 3], [5, 0, 2], [3, 2, 0]]
           }
       )

       # Create optimizer
       factory = OptimizerFactory()
       optimizer = factory.create_optimizer(problem, timeout=5.0)

       # Solve
       result = optimizer.solve(problem)

       # Verify result
       assert result is not None
       assert result.status in [SolverStatus.OPTIMAL, SolverStatus.FEASIBLE]
       assert result.solution is not None
       assert result.computation_time > 0

Mock Test Example
~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from unittest.mock import Mock, patch
   from MEZAN.ATLAS.atlas_core.agents import SynthesisAgent

   @patch('anthropic.Anthropic')
   def test_synthesis_agent_with_mock(mock_anthropic):
       \"\"\"Test synthesis agent with mocked API\"\"\"
       # Mock API response
       mock_anthropic.return_value.messages.create.return_value = Mock(
           content=[Mock(text="Synthesized result")]
       )

       # Create agent
       agent = SynthesisAgent(api_key="test-key")

       # Execute task
       result = agent.execute_task({
           "type": "synthesis",
           "papers": ["paper1", "paper2"]
       })

       # Verify
       assert "Synthesized result" in result["output"]
       mock_anthropic.return_value.messages.create.assert_called_once()

Test Fixtures
~~~~~~~~~~~~~

.. code-block:: python

   import pytest
   from MEZAN.core import OptimizationProblem, ProblemType

   @pytest.fixture
   def sample_qap_problem():
       \"\"\"Fixture providing sample QAP problem\"\"\"
       return OptimizationProblem(
           problem_type=ProblemType.QAP,
           data={
               "distance_matrix": [[0, 10], [10, 0]],
               "flow_matrix": [[0, 5], [5, 0]]
           }
       )

   def test_with_fixture(sample_qap_problem):
       \"\"\"Test using fixture\"\"\"
       assert sample_qap_problem.problem_type == ProblemType.QAP

Debugging Tests
---------------

Run Specific Test
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pytest MEZAN/core/tests/test_integration_layer.py::test_create_qap_problem -v

With PDB Debugger
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pytest --pdb  # Drop into debugger on failure
   pytest --pdb --trace  # Drop into debugger at start

Verbose Output
~~~~~~~~~~~~~~

.. code-block:: bash

   pytest -vv --tb=long  # Very verbose with full tracebacks

Show Print Statements
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   pytest -s  # Show print() output

Continuous Integration
----------------------

Pre-commit Hooks
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Install pre-commit
   pip install pre-commit
   pre-commit install

   # Run manually
   pre-commit run --all-files

Local CI Simulation
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Simulate CI pipeline locally
   black --check .
   ruff check . --fix
   mypy MEZAN/
   pytest MEZAN/ --cov=MEZAN

Test Reports
------------

* **Full Report:** ``test_execution_report.md``
* **Dashboard:** ``test_status_dashboard.md``
* **Coverage:** ``htmlcov/index.html`` (after running with --cov)

Troubleshooting
---------------

Import Errors
~~~~~~~~~~~~~

.. code-block:: bash

   # Set PYTHONPATH
   export PYTHONPATH=/home/user/AlaweinOS:$PYTHONPATH

   # Or use pip install -e .
   pip install -e .

Redis Connection Errors
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Start Redis
   docker run -d --name mezan-redis -p 6379:6379 redis:7-alpine

   # Verify connection
   redis-cli ping

Missing Dependencies
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Install development dependencies
   pip install -e ".[dev]"

   # Install specific solver
   cd MEZAN/Libria/libria-qap
   pip install -e .
