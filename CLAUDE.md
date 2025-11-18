# CLAUDE.md

This file provides comprehensive guidance to Claude Code and other AI assistants when working with code in the AlaweinOS organization repository.

## Organization Overview

**Name:** AlaweinOS
**Type:** Monorepo Enterprise Software Organization
**Owner:** Meshal Alawein (meshal@berkeley.edu)
**Purpose:** Enterprise-grade software projects and optimization frameworks where PhD-level mathematical rigor meets scalable production systems and high-performance computing.

**Philosophy:** From optimization theory to enterprise automation, this portfolio transforms theoretical physics principles into robust, scalable software systems that solve real-world problems at enterprise scale.

## Repository Structure

This is a **monorepo** containing 5 major independent systems:

```
AlaweinOS/
├── MEZAN/          # Modular Enterprise Zonal Automation Network
├── TalAI/          # Autonomous Testing & Laboratory Analysis Intelligence
├── optilibria/     # Universal Optimization Framework
├── SimCore/        # High-Performance Simulation Core Engine
├── qmlab/          # Quantum Machine Learning Laboratory
├── docs/           # Shared documentation
├── scripts/        # Shared utilities
├── tests/          # Integration tests
└── reports/        # Analysis and compliance reports
```

Each system is independently deployable but designed to integrate with others.

## Essential Commands

### Root Level

```bash
# Setup pre-commit hooks
make setup

# Run all linters
make lint

# Run type checking
make type

# Run all tests
make test

# Generate repository tree
make tree
```

### Git Workflow

```bash
# Current branch
git status

# Create feature branch (must start with 'claude/')
git checkout -b claude/feature-name-sessionid

# Commit changes
git add .
git commit -m "description"

# Push changes (use -u for new branches)
git push -u origin claude/feature-name-sessionid
```

## Major Systems

### 1. MEZAN - Modular Enterprise Zonal Automation Network

**Location:** `/MEZAN/`
**Purpose:** Enterprise automation platform orchestrating complex workflows and distributed systems

#### Subsystems

##### ATLAS (AI Research Orchestration)
- **Type:** Multi-agent AI research orchestration system
- **Entry Point:** `MEZAN/ATLAS/atlas-core/src/atlas/atlas_api_server.py`
- **Documentation:** `MEZAN/ATLAS/START_HERE.md`
- **Tech Stack:** Python 3.9+, Flask, Redis, Anthropic API, OpenAI API

**Key Components:**
- ATLASEngine - Main orchestration engine
- 8+ Specialized research agents (Synthesis, Literature Review, Hypothesis Generation, etc.)
- Redis Blackboard for shared state
- Dialectical workflow support (thesis-antithesis-synthesis)

**Commands:**
```bash
cd MEZAN/ATLAS
make setup          # Install dependencies
make test           # Run tests
make orchestrator   # Start HTTP server
```

##### Libria Suite (Novel Optimization Solvers)
- **Type:** Collection of 7 novel optimization algorithms for multi-agent AI
- **Location:** `MEZAN/Libria/`
- **Documentation:** `MEZAN/Libria/EXECUTIVE_SUMMARY.md`
- **Tech Stack:** Python 3.9+, PyTorch, NumPy, SciPy, OR-Tools, NetworkX

**Sub-projects:**
- `libria-qap` - GPU-accelerated quadratic assignment problem solver
- `libria-flow` - Confidence-aware workflow routing
- `libria-alloc` - Constrained Thompson Sampling for resource allocation
- `libria-graph` - Information-theoretic agent network topology optimization
- `libria-dual` - Adversarial min-max optimization
- `libria-evo` - Evolutionary algorithms for multi-objective optimization
- `libria-meta` - Solver-of-solvers for automatic algorithm selection

**Commands:**
```bash
cd MEZAN/Libria/libria-{project}
pip install -r requirements.txt
pytest  # Run tests
```

### 2. TalAI - Autonomous Testing & Laboratory Analysis Intelligence

**Location:** `/TalAI/`
**Purpose:** AI-powered research and development platform with 28+ specialized modules
**Tech Stack:** Python 3.8+, Anthropic API, OpenAI API, PyTorch, PyYAML

**Key Modules:**
- `abstract-writer` - Abstract generation from research papers
- `adversarial-review` - Adversarial critique generation
- `atlas-autonomous-research` - Autonomous research execution with ATLAS
- `experiment-designer` - Experimental design automation
- `ghost-researcher` - Autonomous research execution
- `grant-writer` - Grant proposal generation
- `lit-review-bot` - Literature review automation
- `prompt-marketplace` - Prompt sharing and marketplace
- `alaweinos` - Core TalAI framework and shared standards
- ...and 19 more specialized modules

**Commands:**
```bash
cd TalAI/{module}
pip install -e .     # Editable install
pytest               # Run tests
python -m {module}   # Run module
```

### 3. Optilibria - Universal Optimization Framework

**Location:** `/optilibria/`
**Purpose:** Production-grade optimization library with 31+ algorithms, GPU acceleration, and enterprise-scale performance
**Documentation:** `optilibria/README.md`, `optilibria/CLAUDE.md`
**Tech Stack:** Python 3.9+, JAX, NumPy, SciPy, Optional: PyTorch, Qiskit, PennyLane

**Key Features:**
- 5 core optimization methods (Random Search, Simulated Annealing, Local Search, Genetic Algorithm, Tabu Search)
- 138+ QAPLIB benchmark instances
- AI method selector for automatic algorithm selection
- Universal domain adapter architecture
- 95% test coverage

**Commands:**
```bash
cd optilibria
pip install -e .                    # Base install
pip install -e ".[quantum]"         # With quantum support
pip install -e ".[ml]"              # With ML support
pytest                              # Run tests (138 tests)
make bench-html                     # Run benchmarks
```

**Usage Example:**
```python
from optilibria import EnterpriseOptimizer
optimizer = EnterpriseOptimizer(
    algorithms=["genetic", "simulated_annealing", "gradient_descent"],
    gpu_accelerated=True,
    enterprise_ready=True
)
result = optimizer.optimize_enterprise_function(objective, constraints)
```

### 4. SimCore - High-Performance Simulation Core Engine

**Location:** `/SimCore/`
**Purpose:** Enterprise-grade simulation framework for complex systems modeling
**Tech Stack:** Python 3.x, NumPy, SciPy, HPC Computing

**Status:** Early stage / foundational framework

**Commands:**
```bash
cd SimCore
pip install -e .
pytest
```

### 5. QMLab - Quantum Machine Learning Laboratory

**Location:** `/qmlab/`
**Purpose:** Interactive quantum computing education and visualization platform
**Production URL:** https://qmlab.online/
**Documentation:** `qmlab/CLAUDE.md`
**Tech Stack:** React 18, TypeScript, Vite, shadcn/ui, Three.js, Tailwind CSS

**Key Features:**
- Quantum circuit builder
- Bloch sphere visualization
- Training dashboard with metrics
- Comprehensive accessibility support
- Mobile-responsive design

**Commands:**
```bash
cd qmlab
npm install              # Install dependencies
npm run dev              # Dev server (port 8080)
npm run build            # Production build
npm run test             # Playwright tests
npm run test:a11y        # Accessibility tests
npm run test:mobile      # Mobile tests
```

## Technology Stack

### Primary Languages
- **Python 3.8+/3.9+** - Dominant across MEZAN, TalAI, Optilibria, SimCore
- **TypeScript/JavaScript** - QMLab frontend

### Core Scientific & ML Libraries
- **Numerical Computing:** NumPy, SciPy, Pandas
- **Machine Learning:** PyTorch, scikit-learn, Optuna, Ray
- **Optimization:** OR-Tools, NetworkX, custom algorithms
- **Quantum:** Qiskit, PennyLane (optional)
- **Visualization:** Matplotlib, Recharts, Three.js

### API & Services
- **AI APIs:** Anthropic Claude, OpenAI GPT
- **Task Queues & State:** Redis
- **Web Framework:** Flask (ATLAS API)

### Frontend (QMLab)
- **Framework:** React 18, React Router v6
- **UI Components:** shadcn/ui (Radix UI + Tailwind CSS)
- **Build Tool:** Vite with React SWC
- **3D Graphics:** Three.js

### Development Tools
- **Linting:** ruff (Python), ESLint (JS/TS)
- **Formatting:** Black (line length: 100)
- **Type Checking:** mypy
- **Testing:** pytest (Python), Playwright (E2E)
- **CI/CD:** GitHub Actions
- **Security:** CodeQL, Trivy
- **Pre-commit:** Configured with hooks for trailing whitespace, YAML/JSON validation, Black, Ruff

## Development Guidelines

### Code Quality Standards

1. **Python Projects:**
   - Follow Black formatting (line length: 100)
   - Use Ruff for linting with `--fix` flag
   - Enable mypy type checking
   - Maintain 60-95% test coverage (varies by project)
   - Use comprehensive docstrings and type hints
   - Write tests in `tests/` directory using pytest

2. **JavaScript/TypeScript Projects:**
   - Use ESLint for linting
   - Follow Tailwind CSS conventions
   - Write E2E tests with Playwright
   - Ensure accessibility compliance

3. **General:**
   - Pre-commit hooks are enforced (trailing whitespace, end-of-file-fixer, check-yaml, check-json)
   - All markdown files reviewed by Meshal Alawein (CODEOWNERS)
   - Security policy documented in SECURITY.md
   - Code of conduct in CODE_OF_CONDUCT.md

### Testing Requirements

**Python Projects:**
```bash
pytest                  # Run all tests
pytest -v              # Verbose output
pytest --cov           # Coverage report
pytest -k test_name    # Run specific test
```

**Coverage Requirements:**
- Optilibria: 95% (138 tests passing)
- ATLAS: Core components tested
- TalAI modules: Varies by component

**QMLab:**
```bash
npm run test           # Standard Playwright tests
npm run test:a11y      # Accessibility tests
npm run test:mobile    # Mobile device tests
```

### Architecture Patterns

1. **Monorepo Organization:**
   - Each system independently deployable
   - Shared utilities via imports (e.g., TalAI.alaweinos for standards)
   - Independent CI/CD per system
   - Separate GitHub workflows

2. **Python Project Structure:**
```
{system}/
├── src/{package}/      # Source code
│   ├── __init__.py
│   ├── core/           # Core functionality
│   ├── agents/         # Agent implementations
│   └── utils/          # Utilities
├── tests/              # Test suite
├── docs/               # Documentation
├── examples/           # Usage examples
├── pyproject.toml      # Package config
└── README.md
```

3. **AI Integration Patterns:**
   - Anthropic Claude API for research/analysis
   - OpenAI API for complementary tasks
   - LLM-based orchestration in ATLAS
   - Prompt optimization in TalAI

4. **Dependency Management:**
   - Core dependencies: Scientific Python stack
   - Optional features: Gated behind extras_require (quantum, ml, docs, theorem)
   - Modern Python: 3.8+ minimum, testing on 3.9-3.12

## System Interconnections

### Integration Flow

```
┌─────────────────────────────────────────────┐
│         AlaweinOS Ecosystem                 │
├─────────────────────────────────────────────┤
│                                             │
│  MEZAN (Orchestration Layer)               │
│  ├─ ATLAS → Orchestrates research workflows │
│  │          Uses: Libria, TalAI, Optilibria│
│  └─ Libria → Specialized optimization       │
│              Uses: Optilibria algorithms    │
│                    ↓                        │
│  TalAI (Research Automation, 28 modules)    │
│  └─ Generates hypotheses & experiments      │
│              Uses: ATLAS for orchestration  │
│                    ↓                        │
│  Optilibria (Optimization Foundation)       │
│  └─ Provides algorithms & optimization      │
│              Used by: ATLAS, Libria, TalAI  │
│                    ↓                        │
│  SimCore (Simulation Engine)                │
│  └─ Runs simulations with optimized params  │
│                                             │
│  QMLab (Visualization & Education)          │
│  └─ Independent educational platform        │
│                                             │
└─────────────────────────────────────────────┘
```

### Data Flow
1. **TalAI** generates research hypotheses and designs experiments
2. **ATLAS** orchestrates multi-agent workflows and coordinates agents
3. **Optilibria** optimizes resource allocation and task assignment
4. **Libria Suite** provides specialized optimization for ATLAS workflows
5. **SimCore** runs simulations based on optimized parameters
6. **QMLab** visualizes and explores quantum aspects (independent)

## Common Tasks

### Adding New Features

1. **Identify the Target System:**
   - Research automation → TalAI
   - Optimization algorithms → Optilibria or Libria
   - Multi-agent orchestration → ATLAS
   - Simulation → SimCore
   - Visualization → QMLab

2. **Follow System-Specific Guidelines:**
   - Read system's README.md and CLAUDE.md (if exists)
   - Check existing patterns in similar modules
   - Add tests for new functionality
   - Update documentation

3. **Testing:**
   - Write unit tests
   - Run existing test suite
   - Verify pre-commit hooks pass
   - Check coverage if applicable

### Running CI/CD

GitHub Actions workflows in `.github/workflows/`:
- `ci.yml` - Main CI pipeline (test, lint, type check, build)
- `codeql.yml` - Security analysis
- `accessibility.yml` - QMLab accessibility testing
- `code-quality.yml` - Code quality checks
- `compliance_check.yml` - Compliance validation
- `optibench-nightly.yml` - Benchmarking
- `repo-hygiene.yml` - Repository maintenance

### Debugging

1. **Python Projects:**
```python
import pdb; pdb.set_trace()  # Breakpoint
python -m pytest --pdb       # Debug on failure
```

2. **QMLab:**
```bash
npm run dev  # Check browser console
# React DevTools for component inspection
```

3. **ATLAS API:**
```bash
cd MEZAN/ATLAS
make orchestrator  # Check Flask logs
```

## Documentation Structure

### Comprehensive Documentation Locations

**MEZAN/ATLAS:** (100+ files)
- `MEZAN/ATLAS/START_HERE.md` - Entry point
- `MEZAN/ATLAS/QUICK_START.md` - Quick start guide
- `MEZAN/ATLAS/docs/` - Detailed documentation
  - `analysis/` - Deep analysis
  - `research/` - Research papers (27+ variants)
  - `guides/` - Getting started guides
  - `engineering-framework/` - Standards

**MEZAN/Libria:** (50+ files)
- `MEZAN/Libria/EXECUTIVE_SUMMARY.md` - Overview
- `MEZAN/Libria/docs/` - Architecture, roadmap
- `MEZAN/Libria/{project}/docs/` - Project-specific docs

**Optilibria:**
- `optilibria/README.md` - Main documentation
- `optilibria/CLAUDE.md` - AI assistant guide
- `optilibria/docs/` - Integration guides

**QMLab:**
- `qmlab/README.md` - Project info
- `qmlab/CLAUDE.md` - AI assistant guide
- `qmlab/docs/` - Architecture, development

**TalAI:**
- Each module has its own README.md
- `TalAI/alaweinos/` - Shared standards
- `TalAI/MASTER_INDEX.md` - Module index

### Root Level Documentation
- `README.md` - Organization overview
- `CODE_OF_CONDUCT.md` - Community guidelines
- `SECURITY.md` - Security policy
- `CODEOWNERS` - Code ownership
- `LICENSE` - Apache 2.0

## Enterprise Design Principles

### Core Values

1. **Theory meets practice:** Every solution starts with understanding the underlying mathematical or physical principles
2. **Scale with elegance:** Systems handle massive scale while maintaining code elegance
3. **Scientific rigor in production:** Every algorithm, optimization, and architectural decision should be justified and testable
4. **AI enhances, humans decide:** AI augments human decision-making, not replace it
5. **Build for the future:** Design for evolution, not just current requirements

### Quality Metrics

From `.ai-config.yml`:
- **Code Quality:** 85% threshold
- **Security Score:** 90% threshold
- **Test Coverage:** 80% threshold
- **Compliance:** Security, performance, scalability

### Organizational Philosophy

- **Enterprise-Grade Focus:** Production-ready, scalable systems
- **PhD-Level Rigor:** Mathematical foundations for all optimization
- **Theory to Practice:** Bridges research with commercial applications
- **Modular Architecture:** Independently deployable but interconnected
- **AI-Native Design:** Built around LLM APIs and multi-agent systems

## AI Assistant Specific Guidance

### When Working with This Codebase

1. **System Identification:**
   - Always identify which system you're working in
   - Read system-specific CLAUDE.md if it exists
   - Understand dependencies between systems

2. **Code Changes:**
   - Follow existing patterns in the target system
   - Run pre-commit hooks before committing
   - Add tests for new functionality
   - Update documentation

3. **Testing:**
   - Run tests before and after changes
   - Check that all CI/CD workflows pass
   - Verify pre-commit hooks pass

4. **Documentation:**
   - Update README.md if behavior changes
   - Update system-specific docs
   - Add docstrings and type hints
   - Update CLAUDE.md if workflow changes

5. **Git Workflow:**
   - Create feature branches starting with `claude/`
   - Write clear commit messages
   - Push to feature branch (not main)
   - Use `git push -u origin branch-name` for new branches

### Common Pitfalls to Avoid

1. **Don't modify multiple systems simultaneously** - Each system is independently versioned
2. **Don't skip tests** - Test coverage is enforced
3. **Don't bypass pre-commit hooks** - They're required for code quality
4. **Don't mix Python versions** - Respect each system's Python version requirements
5. **Don't ignore CODEOWNERS** - All changes reviewed by Meshal Alawein
6. **Don't create files without purpose** - Keep repository clean
7. **Don't add emojis to code** unless specifically requested

### Best Practices

1. **Read before writing** - Understand existing patterns
2. **Test thoroughly** - Unit, integration, and E2E tests
3. **Document changes** - Update all relevant documentation
4. **Follow style guides** - Black for Python, ESLint for JS/TS
5. **Think enterprise** - Build for scale, reliability, and maintainability
6. **Respect architecture** - Follow established patterns
7. **Validate assumptions** - Check with documentation first

## Quick Reference

### System Entry Points

| System | Entry Point | Language | Commands |
|--------|-------------|----------|----------|
| MEZAN/ATLAS | `atlas-core/src/atlas/atlas_api_server.py` | Python 3.9+ | `make orchestrator` |
| MEZAN/Libria | Individual solver modules | Python 3.9+ | `pytest` |
| TalAI | Module-specific `src/` directories | Python 3.8+ | `python -m {module}` |
| Optilibria | `optilibria/` package root | Python 3.9+ | `pytest`, `make bench-html` |
| SimCore | `simcore/` package | Python 3.x | `pytest` |
| QMLab | `src/main.tsx` | TypeScript | `npm run dev` |

### Key Documentation Files

| File | Purpose |
|------|---------|
| `/README.md` | Organization overview and system descriptions |
| `/CLAUDE.md` | **This file** - AI assistant comprehensive guide |
| `/.ai-config.yml` | AI system configuration and quality gates |
| `/.pre-commit-config.yaml` | Pre-commit hooks configuration |
| `/CODEOWNERS` | Code ownership and review requirements |
| `/SECURITY.md` | Security policy and vulnerability reporting |
| `/CODE_OF_CONDUCT.md` | Community guidelines |
| `/MEZAN/ATLAS/START_HERE.md` | ATLAS entry point |
| `/MEZAN/Libria/EXECUTIVE_SUMMARY.md` | Libria overview |
| `/optilibria/README.md` | Optilibria comprehensive guide |
| `/qmlab/CLAUDE.md` | QMLab AI assistant guide |

### Contact

**Owner:** Meshal Alawein
**Email:** meshal@berkeley.edu
**Portfolio:** https://malawein.com
**LinkedIn:** https://linkedin.com/in/alawein

### License

Apache 2.0 License - See LICENSE file for details.

---

**Last Updated:** 2025-11-18
**Repository:** https://github.com/AlaweinOS/AlaweinOS
**Organization:** AlaweinOS - Enterprise Software & Optimization Systems

---

*Enterprise systems crafted with ❤️ using mathematics, physics, and enterprise-grade engineering*
