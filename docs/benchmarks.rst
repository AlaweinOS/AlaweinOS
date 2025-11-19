Benchmarking
============

MEZAN V4.1.0 includes comprehensive benchmarking infrastructure for all 7 Libria solvers.

Benchmark Suite
---------------

The benchmark suite tests all solvers across multiple problem sizes and types:

* **Problem Sizes:** 5, 10, 15, 20
* **Problem Types:** QAP, FLOW, ALLOC, GRAPH, DUAL, EVO, META
* **Output Format:** JSON with timestamp
* **Visualization:** Matplotlib charts and markdown reports

Running Benchmarks
------------------

Basic Execution
~~~~~~~~~~~~~~~

.. code-block:: bash

   cd benchmarks
   python run_benchmarks.py

This will:

1. Run 12+ benchmarks across problem types
2. Save results to ``benchmarks/results/benchmark_results_<timestamp>.json``
3. Generate summary statistics

Visualization
~~~~~~~~~~~~~

.. code-block:: bash

   cd benchmarks
   python visualize_benchmarks.py

This creates:

* ``performance_chart.png`` - Line charts by problem type
* ``summary_table.png`` - Summary statistics table
* ``solver_comparison.png`` - Bar chart comparison
* ``BENCHMARK_REPORT.md`` - Complete markdown report

Benchmark Results
-----------------

Latest Results (Heuristic Baseline)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Problem Type    Size    Solver              Time (s)    Status
   ==================================================================
   QAP            5       HeuristicFallback   0.0001      OPTIMAL
   QAP            10      HeuristicFallback   0.0001      OPTIMAL
   QAP            15      HeuristicFallback   0.0001      OPTIMAL
   QAP            20      HeuristicFallback   0.0001      OPTIMAL

   FLOW           5       HeuristicFallback   0.0001      OPTIMAL
   FLOW           10      HeuristicFallback   0.0001      OPTIMAL
   FLOW           15      HeuristicFallback   0.0001      OPTIMAL
   FLOW           20      HeuristicFallback   0.0001      OPTIMAL

   ALLOC          5       HeuristicFallback   0.0001      OPTIMAL
   ALLOC          10      HeuristicFallback   0.0001      OPTIMAL
   ALLOC          15      HeuristicFallback   0.0001      OPTIMAL
   ALLOC          20      HeuristicFallback   0.0001      OPTIMAL

**Note:** These results use HeuristicFallbackOptimizer for baseline performance.
Production solvers (SA, GA, NSGA-II) will have different characteristics.

QAPLIB Benchmarks
-----------------

MEZAN includes 138+ QAPLIB benchmark instances for rigorous QAP testing.

Running QAPLIB Tests
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   cd MEZAN/Libria/libria-qap
   python scripts/run_qaplib_benchmarks.py --instances chr12a chr15a chr20a

QAPLIB Performance Targets
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

   Instance    Size    Optimal     Target Gap    Max Time
   =========================================================
   chr12a      12      9552        < 5%          10s
   chr15a      15      9896        < 5%          30s
   chr20a      20      2192        < 10%         60s
   chr25a      25      3796        < 15%         120s

Benchmark Analysis
------------------

Key Metrics
~~~~~~~~~~~

* **Execution Time**: Wall-clock time for solution
* **Optimality Gap**: % difference from known optimal (if available)
* **Success Rate**: % of benchmarks completing successfully
* **Scalability**: Time complexity with problem size

Performance Visualization
~~~~~~~~~~~~~~~~~~~~~~~~~

Convergence plots show algorithm behavior over iterations:

.. code-block:: python

   from MEZAN.visualization.plot_convergence import ConvergencePlotter

   plotter = ConvergencePlotter()
   fig = plotter.plot_single_convergence(
       iterations=[0, 10, 20, 30, 40, 50],
       objectives=[1000, 800, 650, 500, 420, 390],
       title="Simulated Annealing - QAP n=20"
   )
   fig.savefig("convergence.png")

Pareto front visualization for multi-objective:

.. code-block:: python

   from MEZAN.visualization.plot_pareto import ParetoPlotter

   plotter = ParetoPlotter()
   fig = plotter.plot_2d_pareto(
       pareto_front=pareto_solutions,
       all_solutions=all_solutions,
       obj1_name="Speed",
       obj2_name="Quality"
   )
   fig.savefig("pareto_front.png")

Custom Benchmarks
-----------------

Creating Custom Tests
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from benchmarks.run_benchmarks import BenchmarkRunner

   class MyBenchmarkRunner(BenchmarkRunner):
       def run_custom_benchmark(self):
           results = []
           for size in [10, 20, 30, 40]:
               problem = create_custom_problem(size)
               optimizer = create_optimizer(problem)

               start_time = time.time()
               result = optimizer.solve(problem)
               elapsed = time.time() - start_time

               results.append({
                   "size": size,
                   "time": elapsed,
                   "status": result.status.value,
                   "objective": result.objective_value
               })

           return results

   runner = MyBenchmarkRunner()
   custom_results = runner.run_custom_benchmark()

CI/CD Integration
-----------------

Automated Benchmarking
~~~~~~~~~~~~~~~~~~~~~~

GitHub Actions workflow runs benchmarks nightly:

.. code-block:: yaml

   name: QAPLIB Benchmarks
   on:
     schedule:
       - cron: '0 2 * * *'  # 2 AM daily

   jobs:
     benchmark:
       runs-on: ubuntu-latest
       steps:
         - name: Run QAPLIB Benchmarks
           run: |
             cd MEZAN/Libria/libria-qap
             python scripts/run_qaplib_benchmarks.py --all

Performance Regression Detection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Automated detection of performance regressions:

.. code-block:: bash

   # Compare against baseline
   python scripts/compare_benchmarks.py \\
     --baseline baseline_results.json \\
     --current current_results.json \\
     --threshold 0.15  # 15% regression threshold

Results Archive
---------------

All benchmark results are stored in ``benchmarks/results/`` with timestamps
for historical analysis and trend detection.

Example result file:

.. code-block:: json

   {
     "timestamp": "2025-11-19T06:51:04",
     "mezan_version": "4.1.0",
     "results": [
       {
         "problem_type": "QAP",
         "solver": "HeuristicFallbackOptimizer",
         "size": 5,
         "time": 0.0001,
         "status": "OPTIMAL",
         "objective_value": 123.45
       }
     ],
     "summary": {
       "total_benchmarks": 12,
       "avg_time_by_type": {...}
     }
   }
