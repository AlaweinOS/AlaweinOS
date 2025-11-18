# Contributing to AlaweinOS GitHub Ecosystem

Thank you for your interest in contributing to the AlaweinOS GitHub ecosystem! This document provides guidelines and instructions for contributing to any of our 41+ repositories.

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Development Workflow](#development-workflow)
- [Coding Standards](#coding-standards)
- [Testing Requirements](#testing-requirements)
- [Documentation](#documentation)
- [Pull Request Process](#pull-request-process)
- [Issue Guidelines](#issue-guidelines)
- [Community](#community)

---

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment. All contributors are expected to:

- Be respectful and considerate
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Respect differing viewpoints and experiences
- Accept responsibility and apologize for mistakes
- Focus on what is best for the community

---

## 🚀 Getting Started

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME

# Add upstream remote
git remote add upstream https://github.com/AlaweinOS/REPO-NAME.git
```

### 2. Set Up Development Environment

```bash
# Install dependencies
make install

# Set up pre-commit hooks
pre-commit install

# Verify setup
make test
```

### 3. Create a Branch

```bash
# Create a feature branch
git checkout -b feature/your-feature-name

# Or a bugfix branch
git checkout -b fix/issue-description
```

---

## 📁 Repository Structure

Our repositories follow standardized golden templates based on type:

### Tool/Utility Repositories
```
repo/
├── src/              # Source code
├── tests/            # Test files
├── bin/              # Executable scripts
├── config/           # Configuration files
├── examples/         # Usage examples
├── docs/             # Documentation
└── README.md         # Project overview
```

### Research Library Repositories
```
repo/
├── src/              # Core algorithms
├── tests/            # Test suite
├── docs/             # Documentation
├── examples/         # Example notebooks
├── benchmarks/       # Performance tests
└── papers/           # Published papers
```

See `WORKSPACE/alaweimm90-workspace/ONBOARDING.md` for complete structure details.

---

## 🔄 Development Workflow

### 1. Keep Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream changes
git checkout main
git merge upstream/main
```

### 2. Make Your Changes

```bash
# Make changes to code
# Run tests frequently
make test

# Run linters
make lint

# Format code
make format
```

### 3. Commit Your Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "feat: add new feature X"

# Pre-commit hooks will run automatically
```

### Commit Message Format

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `perf`: Performance improvements
- `ci`: CI/CD changes

**Examples:**
```bash
git commit -m "feat(api): add user authentication endpoint"
git commit -m "fix(parser): handle edge case in CSV parsing"
git commit -m "docs: update installation instructions"
git commit -m "test: add unit tests for validator module"
```

---

## 📏 Coding Standards

### Python Projects

```python
# Follow PEP 8 style guide
# Use type hints
def process_data(input_data: List[str]) -> Dict[str, Any]:
    """Process input data and return results.
    
    Args:
        input_data: List of strings to process
        
    Returns:
        Dictionary containing processed results
    """
    pass

# Use docstrings for all public functions
# Keep functions focused and small
# Write self-documenting code
```

**Tools:**
- **Formatter**: Black (line length: 100)
- **Linter**: Ruff
- **Type Checker**: mypy
- **Import Sorter**: isort

### TypeScript/JavaScript Projects

```typescript
// Use TypeScript for type safety
interface UserData {
  id: string;
  name: string;
  email: string;
}

// Document complex functions
/**
 * Processes user data and returns formatted result
 * @param data - Raw user data
 * @returns Formatted user object
 */
function processUser(data: UserData): FormattedUser {
  // Implementation
}

// Use meaningful variable names
// Keep functions pure when possible
// Follow functional programming principles
```

**Tools:**
- **Formatter**: Prettier
- **Linter**: ESLint
- **Type Checker**: TypeScript compiler

### General Guidelines

- ✅ Write clear, self-documenting code
- ✅ Add comments for complex logic
- ✅ Keep functions small and focused
- ✅ Use meaningful variable names
- ✅ Follow DRY (Don't Repeat Yourself)
- ✅ Write tests for new features
- ✅ Update documentation

---

## 🧪 Testing Requirements

### Minimum Requirements

- **Unit Tests**: All new functions must have unit tests
- **Coverage**: Maintain >80% code coverage
- **Integration Tests**: Add for new features
- **Edge Cases**: Test boundary conditions

### Running Tests

```bash
# Run all tests
make test

# Run with coverage
make test-coverage

# Run specific test file
pytest tests/test_module.py

# Run specific test
pytest tests/test_module.py::test_function_name
```

### Writing Tests

```python
import pytest
from mymodule import my_function

def test_my_function_basic():
    """Test basic functionality."""
    result = my_function("input")
    assert result == "expected"

def test_my_function_edge_case():
    """Test edge case handling."""
    with pytest.raises(ValueError):
        my_function(None)

@pytest.mark.parametrize("input,expected", [
    ("a", "A"),
    ("b", "B"),
    ("c", "C"),
])
def test_my_function_parametrized(input, expected):
    """Test multiple inputs."""
    assert my_function(input) == expected
```

---

## 📚 Documentation

### Code Documentation

- Add docstrings to all public functions/classes
- Include type hints in Python code
- Document complex algorithms
- Add inline comments for tricky logic

### Project Documentation

Update relevant documentation:
- `README.md` - If changing functionality
- `USAGE.md` - If changing usage patterns
- `docs/` - For detailed documentation
- `CHANGELOG.md` - For notable changes

### Documentation Style

```python
def complex_function(param1: str, param2: int) -> Dict[str, Any]:
    """Brief one-line description.
    
    More detailed description if needed. Explain what the function
    does, any important algorithms, or edge cases.
    
    Args:
        param1: Description of first parameter
        param2: Description of second parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When param1 is empty
        TypeError: When param2 is negative
        
    Example:
        >>> result = complex_function("test", 42)
        >>> print(result)
        {'status': 'success'}
    """
    pass
```

---

## 🔀 Pull Request Process

### Before Submitting

1. ✅ All tests pass locally
2. ✅ Code is formatted and linted
3. ✅ Documentation is updated
4. ✅ Commit messages follow conventions
5. ✅ Branch is up to date with main

### Submitting a PR

1. **Push your branch**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request on GitHub**
   - Use a clear, descriptive title
   - Reference related issues
   - Describe changes in detail
   - Add screenshots if applicable

3. **PR Template**
   ```markdown
   ## Description
   Brief description of changes
   
   ## Type of Change
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Related Issues
   Fixes #123
   
   ## Testing
   - [ ] Unit tests added/updated
   - [ ] Integration tests added/updated
   - [ ] All tests passing
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] No breaking changes (or documented)
   ```

### Review Process

1. **Automated Checks**: CI/CD runs automatically
2. **Code Review**: Maintainers review your code
3. **Feedback**: Address review comments
4. **Approval**: Once approved, PR will be merged

### After Merge

```bash
# Update your local main branch
git checkout main
git pull upstream main

# Delete feature branch
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

---

## 🐛 Issue Guidelines

### Before Creating an Issue

1. Search existing issues
2. Check documentation
3. Try latest version
4. Gather relevant information

### Creating a Good Issue

**Bug Report Template:**
```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step one
2. Step two
3. Step three

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: [e.g., Windows 11]
- Python/Node version: [e.g., 3.11]
- Package version: [e.g., 1.2.3]

## Additional Context
Screenshots, logs, etc.
```

**Feature Request Template:**
```markdown
## Feature Description
Clear description of the feature

## Use Case
Why is this feature needed?

## Proposed Solution
How should it work?

## Alternatives Considered
Other approaches you've thought about

## Additional Context
Any other relevant information
```

---

## 🤝 Community

### Getting Help

- **Documentation**: Check `README.md` and `docs/`
- **Issues**: Search existing issues
- **Discussions**: Use GitHub Discussions
- **Contact**: Reach out to maintainers

### Recognition

We value all contributions! Contributors will be:
- Listed in `CONTRIBUTORS.md`
- Mentioned in release notes
- Recognized in project documentation

---

## 📊 Quality Standards

### Code Quality Checklist

- [ ] Code is clean and readable
- [ ] Functions are well-documented
- [ ] Tests are comprehensive
- [ ] No unnecessary complexity
- [ ] Follows project conventions
- [ ] Performance is acceptable
- [ ] Security best practices followed

### Review Checklist

Use `WORKSPACE/alaweimm90-workspace/CODE-REVIEW-CHECKLIST.md` for detailed review criteria.

---

## 🎯 Repository-Specific Guidelines

Different repository types may have additional guidelines:

- **Research Libraries**: Include benchmarks and papers
- **Tools/Utilities**: Provide usage examples
- **Platforms**: Consider scalability and security
- **Educational**: Focus on clarity and learning

Check the repository's `CLAUDE.md` for specific context.

---

## 📞 Questions?

- **General Questions**: Open a GitHub Discussion
- **Bug Reports**: Create an issue
- **Feature Requests**: Create an issue
- **Security Issues**: Email security@alaweinlabs.com (if applicable)

---

## 🙏 Thank You!

Thank you for contributing to AlaweinOS! Your contributions help make our projects better for everyone.

---

**Last Updated**: 2025-01-27
**Version**: 1.0

*For more information, see `WORKSPACE/alaweimm90-workspace/ONBOARDING.md`*
## 🧭 Code Review Rubric

Reviewers focus on continuous improvement and overall code health:

- Design: appropriate, modular, and consistent with architecture
- Functionality: correct behavior, user impact assessed
- Complexity: simplest viable design; avoid over-engineering
- Tests: unit/integration present; cover edge cases; reproducible
- Naming: clear, self-documenting identifiers
- Comments: explain why over what; update docs alongside code
- Style: follow project style guides and conventions
- Documentation: update READMEs and references when behavior changes

Standard of review: approve changes that clearly improve code health, even if not perfect. Prefer incremental improvements with clear follow-ups over blocking for polish.
