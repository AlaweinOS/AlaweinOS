# Optilibria: Universal Optimization Framework

[![Tests](https://img.shields.io/badge/tests-138%20passing-brightgreen)](tests/)
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)](./)
[![Methods](https://img.shields.io/badge/methods-5-blue)](./)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE)

**Optilibria** is a universal optimization framework that provides a unified interface for solving optimization problems across different domains. Focused on combinatorial optimization (QAP, TSP, etc.) with extensible architecture for continuous, multi-objective, and constraint optimization.

## 🎯 Project Status

**Current Version**: 1.0.0 (Beta)
**Status**: Active Development - Core functionality implemented and tested

### What's Working ✅

- ✅ **Universal Domain Adapter Architecture**: Extensible interface for any optimization domain
- ✅ **QAP Domain Adapter**: Fully functional Quadratic Assignment Problem solver with 95% test coverage
- ✅ **TSP Domain Adapter**: Traveling Salesman Problem solver with coordinate and distance matrix support
- ✅ **5 Optimization Methods**: Random Search, Simulated Annealing, Local Search, Genetic Algorithm, Tabu Search
- ✅ **QAPLIB Benchmarking**: 138 benchmark instances with automated testing
- ✅ **Comprehensive Test Suite**: 138 tests, 95% coverage across all modules
- ✅ **Production-Ready Code**: Full type hints, logging, error handling
- ✅ **Visualization Tools**: Publication-quality plots for convergence, tours, and comparisons
- ✅ **AI Method Selector**: Intelligent automatic method selection based on problem features

### In Progress 🚧

- 🚧 **Novel Optimization Methods**: FFT-Laplace preconditioning algorithm
- 🚧 **Additional Domain Adapters**: Portfolio Optimization, Scheduling
- 🚧 **API Documentation**: Sphinx-based comprehensive documentation
- 🚧 **CI/CD Pipeline**: GitHub Actions workflows

### Planned 📋

- 📋 **Extended Method Library**: 15+ additional optimization algorithms
- 📋 **Multi-objective optimization support**
- 📋 **Hyperparameter auto-tuning**
- 📋 **Cross-domain transfer learning**
- 📋 **Autonomous agent-based research system**

## 🚀 Quick Start

### Installation

#### Basic Installation

```bash
# Clone the repository
git clone https://github.com/alaweimm90/Optilibria.git
cd Optilibria

# Install core dependencies only
pip install -e .
```

#### Installation with Optional Dependencies

Optilibria supports several optional dependency groups for extended functionality:

```bash
# Development tools (testing, linting, type checking)
pip install -e ".[dev]"

# Quantum computing support (Qiskit, PennyLane)
pip install -e ".[quantum]"

# Machine learning integration (PyTorch, Optuna, Ray)
pip install -e ".[ml]"

# Documentation building (Sphinx)
pip install -e ".[docs]"

# Theorem proving (Z3 solver)
pip install -e ".[theorem]"

# Install multiple groups
pip install -e ".[dev,quantum,ml]"

# Install all optional dependencies
pip install -e ".[dev,quantum,ml,docs,theorem]"
```

#### Optional Dependency Groups

| Group | Packages | Use Case | Required For |
|-------|----------|----------|--------------|
| `dev` | pytest, black, ruff, mypy | Development & testing | Running tests, code quality |
| `quantum` | qiskit, pennylane | Quantum-inspired methods | Quantum warm-starts, QAOA |
| `ml` | torch, optuna, ray | ML-based optimization | Neural architecture search, hyperparameter tuning |
| `docs` | sphinx, sphinx-rtd-theme | Documentation | Building API docs |
| `theorem` | z3-solver | Formal verification | Constraint verification, theorem proving |

**Note**: All optional dependencies are truly optional. The core framework works without them, and tests requiring optional dependencies are automatically skipped if not installed.

### Basic Usage

```python
from optilibria import optimize
from optilibria.adapters.qap import QAPAdapter
import numpy as np

# Define a Quadratic Assignment Problem
problem = {
    'flow_matrix': np.array([
        [0, 5, 2],
        [5, 0, 3],
        [2, 3, 0]
    ]),
    'distance_matrix': np.array([
        [0, 8, 15],
        [8, 0, 13],
        [15, 13, 0]
    ])
}

# Initialize adapter
adapter = QAPAdapter()

# Optimize using simulated annealing
result = optimize(
    problem,
    adapter,
    method='simulated_annealing',
    config={'iterations': 1000, 'seed': 42}
)

print(f"Best solution: {result['solution']}")
print(f"Objective value: {result['objective']}")
print(f"Valid: {result['is_valid']}")
```

## 📊 Available Methods

| Method | Type | Best For | Coverage | Status |
|--------|------|----------|----------|--------|
| Random Search | Baseline | Quick baseline, small problems | 100% | ✅ Ready |
| Simulated Annealing | Metaheuristic | General-purpose, medium problems | 99% | ✅ Ready |
| Local Search | Hill Climbing | Fast local optimization | 99% | ✅ Ready |
| Genetic Algorithm | Evolutionary | Large problems, population-based | 100% | ✅ Ready |
| Tabu Search | Metaheuristic | Avoiding local optima, memory-based | 100% | ✅ Ready |
| FFT-Laplace | Novel | Large QAP instances (n > 50) | - | 🚧 Coming |
| Ant Colony | Swarm Intelligence | Graph problems, pheromone trails | - | 📋 Planned |
| Particle Swarm | Swarm Intelligence | Continuous optimization | - | 📋 Planned |

## 🌍 Domain Adapters

| Domain | Adapter Class | Coverage | Status | Example |
|--------|---------------|----------|--------|---------|
| Quadratic Assignment (QAP) | `QAPAdapter` | 95% | ✅ Ready | `examples/qap/basic_qap_example.py` |
| Traveling Salesman (TSP) | `TSPAdapter` | 98% | ✅ Ready | `examples/tsp/basic_tsp_example.py` |
| Portfolio Optimization | `PortfolioAdapter` | - | 📋 Planned | - |
| Job Shop Scheduling | `SchedulingAdapter` | - | 📋 Planned | - |
| Neural Architecture Search | `NASAdapter` | - | 📋 Planned | - |

### QAP Convenience API (`optilibria.qaplibria`)

For QAP-focused workflows, you can use the dedicated convenience layer:

```python
from optilibria.qaplibria import optimize_qap
import numpy as np

flow = np.array([[0, 5, 2], [5, 0, 3], [2, 3, 0]])
distance = np.array([[0, 8, 15], [8, 0, 13], [15, 13, 0]])

result = optimize_qap(flow, distance, method="simulated_annealing", config={"iterations": 1000, "seed": 42})

print(result["solution"], result["objective"], result["is_valid"])
```

This is a thin facade over the universal `optimize()` function and `QAPAdapter`,
keeping the main API consistent while making QAP-only experiments easier to read.


## 🏗️ Architecture

```
optilibria/
├── core/
│   ├── interfaces/          # Universal optimization interfaces
│   └── registry/           # Domain & method registration
├── adapters/
│   ├── qap/                # QAP adapter (95% coverage)
│   └── tsp/                # TSP adapter (98% coverage)
├── methods/
│   ├── baselines/          # 5 methods (99%+ coverage)
│   │   ├── RandomSearch
│   │   ├── SimulatedAnnealing
│   │   ├── LocalSearch
│   │   ├── GeneticAlgorithm
│   │   └── TabuSearch
│   └── novel/              # Novel algorithms (in progress)
├── utils/
│   └── qaplib_loader.py     # 138 benchmark instances
├── visualization/           # Publication-quality plotting
└── ai/
    └── method_selector.py   # Intelligent method selection

tests/
└── unit/                    # 138 tests, 95% coverage

examples/
└── qap/                     # Working QAP examples
```

## 📖 Documentation

### Current Documentation
- [Installation Guide](CONTRIBUTING.md)
- [Quick Start Example](examples/qap/basic_qap_example.py)
- [API Documentation](optilibria/__init__.py)
- [Creating Domain Adapters](DOMAIN_ADAPTER_ARCHITECTURE.md)
- [Contributing Guide](CONTRIBUTING.md)

### Project History & Planning
- [AI Planning Summary](AI_CHAT_SUMMARY.md) - Concise overview of planning discussions (4 pages)
- [Historical Planning Archive](archive/historical_planning/ARCHIVE_INDEX.md) - Complete planning documents archive
  - [Framework Summary](archive/historical_planning/qap_optilibria_summary_COMPACT.md) - 8-page essential reference (34+ methods, 3-paper strategy, benchmarks)
  - Migration guides, launch checklists, and strategic planning documents

## 🔧 Troubleshooting

### Common Installation Issues

#### Z3 Solver (theorem group)

**Issue**: `ImportError: No module named 'z3'` or Z3 installation fails

**Solutions**:
```bash
# On Ubuntu/Debian
sudo apt-get install libz3-dev
pip install z3-solver

# On macOS
brew install z3
pip install z3-solver

# On Windows
pip install z3-solver
```

**Workaround**: Tests requiring Z3 are automatically skipped if not installed. Use test markers:
```bash
# Skip Z3-dependent tests
pytest -m "not theorem"
```

#### CUDA/GPU Support (ml group)

**Issue**: PyTorch CUDA not available or GPU not detected

**Solutions**:
```bash
# Install PyTorch with CUDA support (example for CUDA 11.8)
pip install torch --index-url https://download.pytorch.org/whl/cu118

# Verify CUDA availability
python -c "import torch; print(torch.cuda.is_available())"
```

**Workaround**: All ML methods work on CPU. GPU is optional for performance.

#### Resource Module (Unix-only)

**Issue**: `ModuleNotFoundError: No module named 'resource'` on Windows

**Solution**: The `resource` module is Unix-only. Optilibria handles this gracefully:
- Memory profiling features are disabled on Windows
- All core functionality works without it
- Tests requiring `resource` are automatically skipped on Windows

#### Quantum Libraries (quantum group)

**Issue**: Qiskit or PennyLane installation conflicts

**Solutions**:
```bash
# Install quantum group separately if conflicts occur
pip install qiskit==0.40.0
pip install pennylane==0.30.0

# Or use a virtual environment
python -m venv venv-quantum
source venv-quantum/bin/activate  # On Windows: venv-quantum\Scripts\activate
pip install -e ".[quantum]"
```

### Platform-Specific Notes

#### Windows
- `resource` module not available (memory profiling disabled)
- Use PowerShell or Command Prompt for installation
- Some tests may be skipped automatically

#### macOS
- May need Xcode Command Line Tools: `xcode-select --install`
- Use Homebrew for system dependencies

#### Linux
- Install build essentials: `sudo apt-get install build-essential`
- May need additional libraries for Z3 or quantum packages

### Test Markers Reference

Run specific test subsets based on dependencies:

```bash
# Core tests only (no optional dependencies)
pytest -m "unit and not fft_laplace and not theorem and not quantum and not ml"

# Skip tests requiring specific dependencies
pytest -m "not theorem"  # Skip Z3-dependent tests
pytest -m "not quantum"  # Skip quantum computing tests
pytest -m "not ml"       # Skip ML-dependent tests

# Run only fast tests
pytest -m "not slow"

# Run only tests for a specific domain
pytest -m "qap"  # QAP-related tests only
pytest -m "tsp"  # TSP-related tests only
```

### Getting Help

If you encounter issues not covered here:

1. **Check existing issues**: [GitHub Issues](https://github.com/alaweimm90/Optilibria/issues)
2. **Create a new issue**: Include:
   - Python version (`python --version`)
   - OS and version
   - Full error message
   - Installation command used
3. **Community support**: [Discussions](https://github.com/alaweimm90/Optilibria/discussions)

## 🧪 Testing

```bash
# Run core, stable tests only (unit-level, no heavy research suites)
python -m pytest tests -m "unit and not fft_laplace and not theorem"

# Run full test suite (may include slower / research-grade tests)
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=optilibria --cov-report=term

# Run specific test file
python -m pytest tests/unit/test_qap_adapter.py -v
```

### Extended Suites

```bash
# End-to-end coverage (longer workflow smoke tests)
python -m pytest tests/e2e -m e2e

# Performance/regression guards
python -m pytest tests/performance -m performance
```

These suites are gated by markers so that they can be run selectively when you want broader coverage without slowing down day-to-day development. The CI workflow already runs the full `tests/` directory with coverage and uploads results to Codecov.

**Test Profiles**

- **Core unit tests**: Fast, stable tests that should always pass on a standard
  development machine. Use `-m "unit and not fft_laplace and not theorem"`.
- **FFT-Laplace suite**: Research-grade performance and convergence checks for the
  novel FFT-Laplace method. Marked with `@pytest.mark.fft_laplace` and can be run
  selectively via `-m fft_laplace`. These tests may fail while the method is being
  actively developed.
- **Theorem prover suite**: Tests in `tests/unit/test_theorem_prover.py` exercise the
  Z3-based formal verification components. They are marked with
  `@pytest.mark.theorem` and require the optional `theorem` dependency group
  (`pip install .[theorem]`). On environments without Z3, these tests are skipped.

**Test Coverage**: 94.43%
**Total Tests**: 51 (all passing in the core profile)


### Reverse-Time Saddle Escape (Research-Grade Method)

Optilibria includes an experimental **reverse-time saddle point escape** method
(`optilibria.methods.novel.reverse_time_saddle`) with its own comprehensive
validation suite:

- Mathematical foundation: time-reversed gradient dynamics to escape saddle points
- Implementation: `SaddlePointDetector` + `ReverseTimeSaddleEscape` +
  `reverse_time_saddle_optimize`
- Tests: 40+ dedicated unit tests in
  `tests/unit/test_reverse_time_saddle.py` (all currently passing)
- Benchmarks: optional `pytest-benchmark`-based microbenchmarks for detection and
  escape speed (skipped automatically if the plugin is not installed)

This method is **research-grade** and intended for experimentation rather than
production use at this stage. It is also part of the patent portfolio described
in the *Patent Strategy* section below.

## 🔬 Research & Innovation

Optilibria is being developed as part of research into universal optimization frameworks.

### Patent Strategy
Patent applications are in preparation for:
1. **FFT-Laplace Preconditioning** (US Patent Pending): O(n² log n) algorithm for QAP
2. **Fractional-Order IMEX Dynamics** (Patent Pending): Memory-enhanced convergence
3. **Universal Domain Adapter Architecture**: Extensible framework design

**Portfolio Value**: $2-5M (see [Archive](archive/historical_planning/ARCHIVE_INDEX.md) for details)

### Publications in Preparation
Three-paper publication strategy:
- **Paper 1**: "FFT-Laplace Preconditioned Flows on the Birkhoff Polytope" (Target: ICML/IPCO 2025)
- **Paper 2**: "Fractional-Order IMEX Dynamics with Reverse-Time Continuation" (Target: ICLR/AISTATS 2025)
- **Paper 3**: "Structure-Aware Priors: TDA/GNN Regularization with Quantum-Inspired Warm-Starts" (Target: IPCO/Mathematical Programming 2025)

See [Framework Summary](archive/historical_planning/qap_optilibria_summary_COMPACT.md) for complete method taxonomy and research roadmap.

## 📈 Performance Goals

Target performance on QAPLIB benchmarks (being validated):
- Small instances (n < 20): < 1 second, optimal solutions
- Medium instances (20 ≤ n < 50): < 30 seconds, < 1% optimality gap
- Large instances (n ≥ 50): < 5 minutes, < 2% optimality gap

## 🤝 Contributing

We welcome contributions! Areas where we'd love help:

1. **New Domain Adapters**: TSP, Portfolio, Vehicle Routing
2. **Optimization Methods**: Implementing classical algorithms
3. **Benchmarking**: Running experiments on standard problems
4. **Documentation**: Tutorials, examples, API docs
5. **Testing**: Edge cases, integration tests

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## 📜 License

This project is licensed under the Apache License 2.0 - see [LICENSE](LICENSE) for details.

## 📧 Contact

**Meshal Alawein**
Email: meshal@berkeley.edu
GitHub: [@alaweimm90](https://github.com/alaweimm90)

## 🌟 Citation

If you use Optilibria in your research, please cite:

```bibtex
@software{optilibria2025,
  author = {Alawein, Meshal},
  title = {Optilibria: Universal Optimization Framework},
  version = {1.0.0-beta},
  year = {2025},
  url = {https://github.com/alaweimm90/Optilibria}
}
```

## 🙏 Acknowledgments

- QAPLIB benchmark library for test instances
- Scientific Python ecosystem (NumPy, SciPy, pytest)
- Open source optimization community

---

**Note**: This is an active research project under development. Core functionality is stable and tested, but the API may evolve as new features are added. Production use is possible but please test thoroughly for your specific use case.
## 🛡️ Enterprise Compliance

- Governance: `governance/master-config.yaml`
- Compliance: `scripts/compliance_checker.py` writes `reports/compliance_report.json`
- Style Report: generated via ULTRATHINK++ style enforcer
- SSOT References:
  - `ORGANIZATIONS/alaweimm90-tools/agis/docs/standards/INDEX.md`
  - `ORGANIZATIONS/alaweimm90-tools/agis/docs/standards/5-TOOLS/ide-integration.md`
  - `ORGANIZATIONS/alaweimm90-tools/agis/docs/standards/2-PROMPTS/PROMPT_REGISTRY.md`

### IDE Setup

```bash
# Validate VS Code settings (if .vscode present)
python .meta/tools/vscode-settings-manager/cli.py validate --file .vscode/settings.json
```
### Agents & Workflows

- Agents registry: `ai/AGENT_REGISTRY.yaml`
- Workflows: `ai/WORKFLOWS.yaml`
- Python source: `ORGANIZATIONS/AlaweinOS/TalAI/ideaforge/agents.py`
