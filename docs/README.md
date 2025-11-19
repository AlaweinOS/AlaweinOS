# MEZAN V4.1.0 - Documentation

Comprehensive API documentation for the MEZAN optimization framework.

## Building Documentation

### Prerequisites

```bash
pip install sphinx sphinx-rtd-theme
```

### Build HTML Documentation

```bash
cd docs
make html
```

Output will be in `_build/html/index.html`

### Build PDF Documentation (requires LaTeX)

```bash
make latexpdf
```

### Clean Build

```bash
make clean
```

## Documentation Structure

```
docs/
├── index.rst              # Main documentation index
├── conf.py                # Sphinx configuration
├── Makefile               # Build automation
│
├── api/                   # API Reference
│   ├── core.rst          # Core module
│   ├── problem.rst       # OptimizationProblem
│   ├── factory.rst       # OptimizerFactory
│   └── ...
│
├── deployment.rst         # Deployment guide
├── benchmarks.rst         # Benchmarking guide
├── testing.rst            # Testing guide
├── monitoring.rst         # Monitoring guide
│
├── _static/               # Static assets
├── _templates/            # Custom templates
└── _build/                # Generated documentation (gitignored)
```

## Quick Start Examples

### Core Usage

```python
from MEZAN.core import OptimizationProblem, ProblemType, OptimizerFactory

# Create problem
problem = OptimizationProblem(
    problem_type=ProblemType.QAP,
    data={
        "distance_matrix": [[0, 10], [10, 0]],
        "flow_matrix": [[0, 5], [5, 0]]
    }
)

# Create optimizer
factory = OptimizerFactory()
optimizer = factory.create_optimizer(problem)

# Solve
result = optimizer.solve(problem)
print(f"Status: {result.status}")
```

### With Feature Flags

```python
factory = OptimizerFactory(config={
    "feature_flags": {
        "enable_qap_libria": True,
        "enable_gpu_acceleration": True
    }
})

optimizer = factory.create_optimizer(problem, timeout=30.0)
result = optimizer.solve(problem)
```

### ATLAS Multi-Agent

```python
from MEZAN.ATLAS.atlas_core.engine import ATLASEngine
from MEZAN.ATLAS.atlas_core.agents import create_synthesis_agent

engine = ATLASEngine()
agent = create_synthesis_agent()
engine.register_agent(agent)

task_id = engine.submit_task({
    "type": "synthesis",
    "data": {"papers": [...]}
})

result = engine.get_task_result(task_id)
```

## Documentation Sections

### 1. Getting Started
- Installation instructions
- Quick start guide
- Basic examples
- Configuration

### 2. API Reference
- Core module documentation
- Libria solver APIs
- ATLAS engine APIs
- Visualization APIs

### 3. Deployment
- Docker Compose setup
- Kubernetes deployment
- Configuration management
- Security hardening

### 4. Benchmarking
- Running benchmarks
- QAPLIB tests
- Performance analysis
- Visualization

### 5. Testing
- Test structure
- Running tests
- Writing tests
- CI/CD integration

### 6. Monitoring
- Prometheus metrics
- Grafana dashboards
- Alert configuration
- Performance tracking

## Contributing to Documentation

### Adding New Pages

1. Create `.rst` file in appropriate directory
2. Add to `toctree` in `index.rst`
3. Rebuild docs: `make html`

### Docstring Format

Use Google-style docstrings:

```python
def solve(problem: OptimizationProblem) -> OptimizationResult:
    """Solve optimization problem.

    Args:
        problem: The optimization problem to solve

    Returns:
        Result containing solution, status, and metadata

    Raises:
        ValueError: If problem validation fails
        TimeoutError: If solver exceeds time limit

    Example:
        >>> problem = OptimizationProblem(...)
        >>> result = solver.solve(problem)
        >>> print(result.status)
        SolverStatus.OPTIMAL
    """
```

### Building Locally

```bash
# Clean previous build
make clean

# Build HTML
make html

# View in browser
open _build/html/index.html
```

## CI/CD

Documentation is automatically built and validated in GitHub Actions:

```yaml
- name: Build Docs
  run: |
    cd docs
    make html
    # Check for warnings
    make linkcheck
```

## Hosting

Documentation can be hosted on:
- **GitHub Pages**: Auto-deploy from `gh-pages` branch
- **Read the Docs**: Connect repository for automatic builds
- **Self-hosted**: Serve `_build/html` directory

## Resources

- **Sphinx Documentation**: https://www.sphinx-doc.org/
- **reStructuredText Primer**: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
- **RTD Theme**: https://sphinx-rtd-theme.readthedocs.io/

## Support

For documentation issues:
- **GitHub Issues**: https://github.com/AlaweinOS/AlaweinOS/issues
- **Email**: meshal@berkeley.edu
