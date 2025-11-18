# Contributing to Optilibria

Thank you for your interest in contributing to Optilibria! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Code Standards](#code-standards)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Adding New Methods](#adding-new-methods)
- [Documentation](#documentation)

## Getting Started

Before contributing, please:

1. Read the [README.md](README.md) to understand the project
2. Check [existing issues](https://github.com/yourusername/optilibria/issues) for similar work
3. Open an issue to discuss major changes before starting work

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Git
- Recommended: Virtual environment (venv, conda, etc.)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/optilibria.git
cd Optilibria/optilibria

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode with all dependencies
pip install -e ".[dev]"

# Set up pre-commit hooks
pre-commit install
```

## Code Standards

All contributions must adhere to these standards:

### Style and Formatting

- **Line length**: 88 characters (Black default)
- **Formatter**: Black (automated)
- **Linter**: Ruff (replaces flake8, isort, pyupgrade)
- **Type checker**: mypy (strict mode)

### Running Code Quality Checks

```bash
# Format code with Black
black optilibria/ tests/

# Lint with Ruff
ruff check optilibria/ tests/

# Type check with mypy
mypy optilibria/

# Run all checks
pre-commit run --all-files
```

### Type Hints

All functions must have complete type annotations:

```python
from typing import List, Dict, Optional, Tuple

def solve_problem(
    problem: Problem,
    method: str,
    timeout: Optional[float] = None
) -> Tuple[Solution, Dict[str, float]]:
    """Solve optimization problem using specified method.

    Args:
        problem: Problem instance to solve
        method: Name of optimization method
        timeout: Optional time limit in seconds

    Returns:
        Tuple of (solution, metrics)
    """
    ...
```

### Docstrings

Use Google-style docstrings for all public functions, classes, and modules:

```python
def example_function(param1: int, param2: str) -> bool:
    """Brief description of function.

    Longer description if needed, explaining behavior,
    edge cases, and important details.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ValueError: When param1 is negative

    Examples:
        >>> example_function(42, "test")
        True
    """
    ...
```

## Testing

### Test Requirements

- All new code must have tests
- Minimum 85% code coverage
- Tests must pass on Python 3.9, 3.10, 3.11, 3.12

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=optilibria --cov-report=term-missing

# Run specific test file
pytest tests/test_adapters.py

# Run tests matching pattern
pytest -k "test_qap"

# Run with verbose output
pytest -v
```

### Writing Tests

```python
import pytest
from optilibria.adapters import QAPAdapter

def test_qap_adapter_basic():
    """Test basic QAP adapter functionality."""
    adapter = QAPAdapter()
    problem = adapter.from_qaplib("chr12a")

    assert problem is not None
    assert problem.size == 12

def test_qap_adapter_invalid_input():
    """Test QAP adapter handles invalid input."""
    adapter = QAPAdapter()

    with pytest.raises(ValueError):
        adapter.from_qaplib("nonexistent_problem")
```

## Submitting Changes

### Branch Naming

- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation updates
- `refactor/description` - Code refactoring
- `test/description` - Test additions/updates

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance

Examples:
```
feat(adapters): add TSP adapter with TSPLIB support

fix(methods): correct tabu search aspiration criteria

docs(readme): update installation instructions

test(core): add tests for problem registry
```

### Pull Request Process

1. **Create branch** from `main`
2. **Make changes** following code standards
3. **Write/update tests** to maintain 85%+ coverage
4. **Run quality checks** (`pre-commit run --all-files`)
5. **Update documentation** if needed
6. **Push branch** to your fork
7. **Open pull request** with description:
   - What changed and why
   - Link to related issue(s)
   - Testing performed
   - Screenshots (if UI changes)

### Review Process

- At least one maintainer approval required
- All CI checks must pass
- Code coverage must not decrease
- Documentation must be updated

## Adding New Methods

To add a new optimization method:

### 1. Create Method File

```python
# optilibria/optilibria/methods/your_method.py

from optilibria.core.interfaces import Method, Solution, Problem
from optilibria.core.registry import register_method

@register_method(
    name="your_method",
    category="metaheuristic",
    capabilities=["permutation", "continuous"]
)
class YourMethod(Method):
    """Brief description of your method.

    Longer description explaining the algorithm,
    its strengths, weaknesses, and use cases.

    References:
        Author et al. (Year). Paper title. Journal.
    """

    def solve(self, problem: Problem, **kwargs) -> Solution:
        """Solve the optimization problem.

        Args:
            problem: Problem instance
            **kwargs: Method-specific parameters

        Returns:
            Solution object
        """
        # Implementation
        pass
```

### 2. Add Tests

```python
# optilibria/tests/methods/test_your_method.py

import pytest
from optilibria.methods.your_method import YourMethod

def test_your_method_basic():
    """Test basic functionality."""
    method = YourMethod()
    # Test code

def test_your_method_convergence():
    """Test convergence on known problem."""
    # Test code
```

### 3. Add Benchmarks

```python
# Add benchmark configuration to scripts/benchmarks.yaml
your_method:
  instances: [small, medium, large]
  params:
    param1: [value1, value2]
```

### 4. Update Documentation

- Add method to `docs/methods/`
- Update method comparison table
- Add usage example to `examples/`

## Documentation

### Building Documentation

```bash
cd optilibria/
pip install -e ".[docs]"
cd docs/
make html
```

### Documentation Structure

- `docs/` - Main documentation
- `docs/methods/` - Individual method documentation
- `docs/tutorials/` - Step-by-step guides
- `docs/api/` - API reference (auto-generated)
- `examples/` - Runnable code examples

## Questions?

- Open an issue for questions
- Email: meshal@berkeley.edu
- Check existing documentation in `docs/`

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.
