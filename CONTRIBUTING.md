# Contributing to AlaweinOS

Thank you for your interest in contributing to AlaweinOS! This guide will help you get started with contributing to our enterprise monorepo.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Standards](#code-standards)
- [Testing Requirements](#testing-requirements)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [System-Specific Guidelines](#system-specific-guidelines)

---

## Code of Conduct

This project adheres to the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

---

## Getting Started

### Prerequisites

**For Python systems (MEZAN, TalAI, optilibria):**
- Python 3.8+ (3.9-3.12 recommended)
- pip or poetry
- Virtual environment tool (venv, conda)

**For TypeScript systems (SimCore, qmlab):**
- Node.js 16+ (18-20 recommended)
- npm or yarn

**General:**
- Git 2.x+
- Code editor (VS Code recommended)
- Pre-commit hooks support

### Initial Setup

1. **Clone the repository:**
```bash
git clone https://github.com/AlaweinOS/AlaweinOS.git
cd AlaweinOS
```

2. **Choose your system:**
Navigate to the system you want to work on:
- `cd MEZAN/`
- `cd TalAI/`
- `cd optilibria/`
- `cd SimCore/`
- `cd qmlab/`

3. **Install dependencies:**

**Python:**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"  # or pip install -e .
```

**TypeScript:**
```bash
npm install
```

4. **Set up pre-commit hooks (if available):**
```bash
# Python projects
pre-commit install

# Or system-specific setup
make setup  # If Makefile exists
```

---

## Development Workflow

### Branch Naming

**All feature branches must start with `claude/`:**
```bash
git checkout -b claude/feature-name-sessionid
```

Examples:
- `claude/add-optimization-algorithm-01ABC`
- `claude/fix-simulation-bug-02XYZ`
- `claude/update-documentation-03DEF`

### Development Cycle

1. **Create feature branch:**
```bash
git checkout -b claude/your-feature-name-sessionid
```

2. **Make your changes:**
- Write code following system standards
- Add tests for new functionality
- Update documentation

3. **Test your changes:**
```bash
# Python
pytest
pytest --cov

# TypeScript
npm test
npm run build
```

4. **Lint and format:**
```bash
# Python
black .
ruff check . --fix
mypy .

# TypeScript
npm run lint
npm run typecheck
```

5. **Commit your changes:**
```bash
git add .
git commit -m "Component: Brief description

Detailed explanation
"
```

6. **Push to remote:**
```bash
git push -u origin claude/your-feature-name-sessionid
```

7. **Create Pull Request:**
- Use the PR template
- Reference related issues
- Request review

---

## Code Standards

### Python Projects (MEZAN, TalAI, optilibria)

**Formatting:**
- **Black** with line length 100
- **isort** for import sorting

**Linting:**
- **Ruff** for fast linting
- **flake8** (where configured)

**Type Checking:**
- **mypy** with strict mode (where configured)
- Type hints required for public APIs

**Code Style:**
```python
# Good
def calculate_optimization(
    objective_function: Callable,
    constraints: List[Constraint],
    max_iterations: int = 1000
) -> OptimizationResult:
    """Calculate optimal solution using specified algorithm.

    Args:
        objective_function: Function to minimize/maximize
        constraints: List of problem constraints
        max_iterations: Maximum iteration count

    Returns:
        OptimizationResult containing solution and metadata
    """
    # Implementation
    pass
```

**Documentation:**
- Docstrings for all public functions/classes
- Google or NumPy style docstrings
- Type hints in signatures

### TypeScript Projects (SimCore, qmlab)

**Formatting:**
- **ESLint** with project configuration
- **Prettier** for consistent formatting

**Type Safety:**
- Strict TypeScript mode
- No `any` types without justification
- Explicit return types for functions

**Code Style:**
```typescript
// Good
interface SimulationParams {
  timeStep: number;
  iterations: number;
  accuracy?: 'low' | 'medium' | 'high';
}

function runSimulation(params: SimulationParams): SimulationResult {
  // Implementation
}
```

**Components:**
- Functional components with hooks
- Props interfaces defined
- Comprehensive JSDoc comments

### General Standards

**File Organization:**
- One class/component per file
- Logical grouping of related functionality
- Clear directory structure

**Naming:**
- **Python**: `snake_case` for functions/variables, `PascalCase` for classes
- **TypeScript**: `camelCase` for functions/variables, `PascalCase` for classes/types
- **Files**: `lowercase-with-hyphens.md` for docs, language conventions for code

**Comments:**
- Explain "why", not "what"
- Keep comments up-to-date
- Remove commented-out code

---

## Testing Requirements

### Python

**Framework:** pytest

**Coverage Requirements:**
- **MEZAN**: Core components tested
- **TalAI**: Module-specific (varies)
- **optilibria**: 95% coverage (strictly enforced)

**Running Tests:**
```bash
# All tests
pytest

# With coverage
pytest --cov=src --cov-report=html

# Specific test
pytest tests/test_specific.py::test_function_name

# Verbose
pytest -v
```

**Test Structure:**
```python
def test_optimization_algorithm_correctness():
    """Test that algorithm produces correct results."""
    # Arrange
    problem = create_test_problem()

    # Act
    result = optimizer.optimize(problem)

    # Assert
    assert result.is_valid()
    assert result.objective_value < threshold
```

### TypeScript

**Frameworks:**
- **Vitest** for unit tests
- **Playwright** for E2E tests
- **React Testing Library** for components

**Running Tests:**
```bash
# Unit tests
npm test

# E2E tests
npm run test:e2e

# Coverage
npm run test:coverage
```

**Test Structure:**
```typescript
describe('SimulationEngine', () => {
  it('should calculate results accurately', () => {
    const engine = new SimulationEngine(params);
    const result = engine.run();

    expect(result.isValid).toBe(true);
    expect(result.accuracy).toBeGreaterThan(0.95);
  });
});
```

### Test Guidelines

- Write tests for new features
- Update tests for bug fixes
- Test edge cases and error conditions
- Keep tests focused and readable
- Use descriptive test names

---

## Commit Guidelines

### Commit Message Format

```
Component: Brief description (50 chars max)

Detailed explanation (wrap at 72 chars)
- Change 1
- Change 2
- Why this change was made

Fixes #123
```

**Examples:**

```
Optilibria: Add GPU-accelerated simulated annealing

Implements GPU acceleration for simulated annealing algorithm
using JAX for automatic differentiation and compilation.

Performance improvements:
- 10x faster for large problems (n > 1000)
- Automatic CPU fallback when GPU unavailable
- Memory-efficient batch processing

Fixes #456
```

```
SimCore: Fix quantum tunneling visualization bug

Corrects wave function normalization in the visualization
component that was causing incorrect probability displays.

Changes:
- Normalize wave function before rendering
- Add validation checks
- Update unit tests

Fixes #789
```

### Commit Types

- **Feature**: New feature or capability
- **Fix**: Bug fix
- **Docs**: Documentation changes
- **Refactor**: Code refactoring
- **Test**: Adding or updating tests
- **Perf**: Performance improvements
- **Chore**: Maintenance tasks

---

## Pull Request Process

### Before Creating PR

1. ✅ All tests pass
2. ✅ Code is linted and formatted
3. ✅ Documentation is updated
4. ✅ Commit messages follow guidelines
5. ✅ Branch is up-to-date with main

### Creating PR

1. **Use PR template** (automatically loaded)
2. **Write clear description:**
   - What changes were made
   - Why they were needed
   - How to test
3. **Link related issues**
4. **Request reviewers**
5. **Add labels** (if applicable)

### PR Template

```markdown
## Description
Brief description of changes

## Changes Made
- Change 1
- Change 2

## Testing
How to test these changes

## Checklist
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Code follows style guide
- [ ] Commits follow guidelines
```

### Review Process

1. **Automated checks** must pass:
   - CI/CD pipeline
   - Linting
   - Tests
   - Security scans

2. **Code review** by maintainer:
   - Code quality
   - Design decisions
   - Test coverage
   - Documentation

3. **Address feedback:**
   - Make requested changes
   - Respond to comments
   - Re-request review

4. **Merge:**
   - Squash and merge (default)
   - Rebase and merge (if linear history desired)
   - Delete branch after merge

---

## System-Specific Guidelines

### MEZAN

**Focus:** Enterprise automation and orchestration

**Key Areas:**
- ATLAS multi-agent coordination
- Libria optimization algorithms
- Workflow orchestration

**See:** `MEZAN/CONTRIBUTING.md` (if exists) or `MEZAN/README.md`

### TalAI

**Focus:** AI research automation

**Key Areas:**
- Research module development
- Integration with ATLAS
- Prompt engineering

**See:** `TalAI/README.md` and module-specific docs

### Optilibria

**Focus:** Optimization algorithms

**Key Areas:**
- Algorithm implementation
- Benchmarking (QAPLIB)
- GPU acceleration

**Standards:**
- 95% test coverage required
- Rigorous mathematical validation
- Comprehensive benchmarks

**See:** `optilibria/CLAUDE.md`

### SimCore

**Focus:** Interactive scientific computing

**Key Areas:**
- Scientific simulations
- WebGPU acceleration
- Visualization components

**Standards:**
- Research-grade accuracy
- Accessibility (WCAG 2.1 AA)
- Performance (90+ Lighthouse)

**See:** `SimCore/docs/DEVELOPMENT.md`

### qmlab

**Focus:** Quantum computing education

**Key Areas:**
- Educational content
- Accessibility
- User experience

**Standards:**
- WCAG 2.1 AA compliance
- Mobile responsive
- Comprehensive testing

**See:** `qmlab/CLAUDE.md`

---

## Questions?

- **General questions:** Open an issue or contact meshal@berkeley.edu
- **System-specific:** Check system README or documentation
- **Security issues:** See SECURITY.md

---

## License

By contributing, you agree that your contributions will be licensed under the Apache 2.0 License.

---

**Thank you for contributing to AlaweinOS!**

We appreciate your efforts to improve enterprise-grade software systems.

---

**Last Updated:** 2025-11-19
**Maintainer:** Dr. Meshal Alawein (meshal@berkeley.edu)
