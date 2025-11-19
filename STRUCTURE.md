# AlaweinOS - Repository Structure Guide

**Last Updated:** 2025-11-19
**Version:** 4.0.0

This document provides a comprehensive navigation guide for the AlaweinOS monorepo structure.

---

## 📁 Root Directory

```
AlaweinOS/
├── .archive/           # Archived legacy documentation
├── .github/            # GitHub configuration and workflows
├── .meta/              # Meta documentation and notes
├── MEZAN/              # Meta-Equilibrium Zero-regret Assignment Network
├── TalAI/              # Autonomous Testing & Laboratory Analysis Intelligence
├── optilibria/         # Universal Optimization Framework
├── SimCore/            # High-Performance Simulation Core Engine
├── qmlab/              # Quantum Machine Learning Laboratory
├── docs/               # Shared documentation
├── scripts/            # Shared utility scripts
├── tests/              # Integration tests
├── reports/            # Analysis and compliance reports
├── .gitignore          # Git ignore patterns (consolidated)
├── CODEOWNERS          # Code ownership rules
├── CLAUDE.md           # AI assistant comprehensive guide
├── CODE_OF_CONDUCT.md  # Community guidelines
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # Apache 2.0 license
├── Makefile            # Root-level commands
├── PROJECT.md          # Project overview and roadmap
├── README.md           # Main repository documentation
├── SECURITY.md         # Security policy
├── STRUCTURE.md        # This file
└── pyproject.toml      # Workspace-level Python configuration
```

---

## 🗄️ Archive Directory (`.archive/`)

**Purpose:** Historical documentation preserved for reference but no longer actively maintained.

```
.archive/
├── README.md           # Archive documentation
├── sessions/           # Historical session reports
│   ├── AUTONOMOUS_SESSION_SUMMARY.md
│   ├── FINAL_SESSION_REPORT.md
│   ├── SESSION_2_COMPLETION_REPORT.md
│   ├── SESSION_3_COMPLETION_REPORT.md
│   ├── SESSION_4_REFACTORING_REPORT.md
│   └── SESSION_SUMMARY.md
├── development/        # Early-stage brainstorming and planning
│   ├── IDEA_ARCHIVE_ANALYSIS.md
│   └── Important-1.md  # Original MEZAN brainstorming (1,363 lines)
└── prompts/            # Outdated AI assistant superprompts
    ├── MEZAN_SUPERPROMPT.md
    ├── OPTILIBRIA_SUPERPROMPT.md
    └── SIMCORE_SUPERPROMPT.md
```

**Archived:** 2025-11-19 during repository cleanup

---

## ⚙️ GitHub Configuration (`.github/`)

**Purpose:** GitHub-specific configuration, workflows, and templates.

```
.github/
├── workflows/          # GitHub Actions CI/CD pipelines
│   ├── accessibility.yml       # QMLab accessibility testing
│   ├── ci.yml                  # Main CI pipeline
│   ├── code-quality.yml        # Code quality checks
│   ├── codeql.yml              # Security analysis
│   ├── compliance_check.yml    # Compliance validation
│   ├── optibench-nightly.yml   # Nightly benchmarking
│   └── repo-hygiene.yml        # Repository maintenance
├── ISSUE_TEMPLATE/     # Issue templates
├── PULL_REQUEST_TEMPLATE.md
└── dependabot.yml      # Dependency updates configuration
```

---

## 📝 Meta Documentation (`.meta/`)

**Purpose:** Internal documentation and development notes.

```
.meta/
├── DEPENDENCY_STANDARDIZATION_NOTES.md  # Dependency management guide
└── [other meta documentation as needed]
```

---

## 🤖 MEZAN - Meta-Equilibrium Zero-regret Assignment Network

**Location:** `/MEZAN/`
**Status:** V4.0.0 - Production Ready (58,076 lines)

```
MEZAN/
├── ATLAS/              # AI Research Orchestration System
│   ├── .github/        # ATLAS-specific workflows
│   ├── atlas-core/     # Core orchestration engine
│   │   ├── docs/       # Comprehensive documentation (100+ files)
│   │   ├── src/        # Source code
│   │   │   └── atlas/  # Main package
│   │   │       ├── agents/         # 8+ specialized research agents
│   │   │       ├── blackboard/     # Redis-backed shared state
│   │   │       ├── core/           # Core orchestration logic
│   │   │       ├── utils/          # Utilities
│   │   │       └── atlas_api_server.py  # Flask API server
│   │   ├── tests/      # Test suite
│   │   ├── examples/   # Usage examples
│   │   ├── docker/     # Docker configuration
│   │   ├── k8s/        # Kubernetes manifests
│   │   ├── helm/       # Helm charts (planned)
│   │   ├── terraform/  # Terraform configuration (planned)
│   │   ├── Makefile    # Build commands
│   │   ├── requirements.txt
│   │   ├── requirements-dev.txt
│   │   └── requirements-validation.txt
│   ├── pyproject.toml
│   ├── requirements.txt
│   ├── START_HERE.md   # ATLAS entry point
│   └── QUICK_START.md
├── Libria/             # Novel Optimization Solvers Suite
│   ├── libria-qap/     # GPU-accelerated QAP solver
│   │   ├── src/
│   │   ├── tests/
│   │   ├── docs/
│   │   └── requirements.txt
│   ├── libria-flow/    # Confidence-aware workflow routing
│   ├── libria-alloc/   # Constrained Thompson Sampling
│   ├── libria-graph/   # Network topology optimization
│   ├── libria-dual/    # Adversarial min-max optimization
│   ├── libria-evo/     # Evolutionary algorithms
│   ├── libria-meta/    # Solver-of-solvers
│   ├── EXECUTIVE_SUMMARY.md
│   └── docs/
├── docs/               # MEZAN-wide documentation
│   └── LOCAL_AI_ORCHESTRATION_SUPERPROMPT.md
├── MEZAN_COMPLETE_DUAL_DOCUMENTATION.md  # Vision vs. V4.0.0 reality
└── [other configuration files]
```

**Key Entry Points:**
- `MEZAN/ATLAS/START_HERE.md` - Start here for ATLAS
- `MEZAN/MEZAN_COMPLETE_DUAL_DOCUMENTATION.md` - Comprehensive MEZAN documentation
- `MEZAN/Libria/EXECUTIVE_SUMMARY.md` - Libria suite overview

---

## 🧪 TalAI - Autonomous Testing & Laboratory Analysis Intelligence

**Location:** `/TalAI/`
**Status:** Active Development (28+ modules)

```
TalAI/
├── alaweinos/          # Shared standards and common code
│   ├── src/
│   └── pyproject.toml
├── abstract-writer/    # Abstract generation
│   ├── src/
│   ├── tests/
│   ├── README.md
│   └── pyproject.toml
├── adversarial-review/ # Adversarial critique generation
├── atlas-autonomous-research/  # ATLAS integration
├── atlas-orchestrator/ # Multi-agent orchestration
├── chaos-engine/       # Chaos engineering for research
├── citation-predictor/ # Citation prediction
├── data-cleaner/       # Data cleaning automation
├── experiment-designer/  # Experimental design
├── failure-db/         # Failure database
├── ghost-researcher/   # Autonomous research execution
├── grant-writer/       # Grant proposal generation
├── hypothesis-match/   # Hypothesis matching
├── idea-calculus/      # Research idea analysis
├── lit-review-bot/     # Literature review automation
├── paper-miner/        # Paper mining and analysis
├── PEDs-Playbook/      # Practical experimental design
├── prompt-marketplace/ # Prompt sharing
├── promptforge/        # Prompt engineering tools
├── promptforge-lite/   # Lightweight prompt tools
├── research-pricer/    # Research cost estimation
├── turing-features/    # Advanced AI features
│   ├── meta-learning/
│   ├── self-refutation/
│   ├── hall-of-failures/
│   └── interrogation/
├── turingo/            # Turing test framework
├── validation-framework/  # Validation tools
└── MASTER_INDEX.md     # Module index
```

**Architecture Pattern:** Each module is independently installable with:
- `src/{module}/` - Source code
- `tests/` - Test suite
- `README.md` - Module documentation
- `pyproject.toml` - Package configuration

---

## 🔧 Optilibria - Universal Optimization Framework

**Location:** `/optilibria/`
**Status:** V1.0.0 Beta (138 tests, 95% coverage)

```
optilibria/
├── .github/            # CI/CD workflows
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── codeql.yml
│   │   ├── compliance_check.yml
│   │   └── llm-eval-caller.yml
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── dependabot.yml
├── optilibria/         # Main package
│   ├── __init__.py
│   ├── core/           # Core optimization logic
│   │   ├── optimizer.py
│   │   ├── domain_adapter.py
│   │   └── ...
│   ├── algorithms/     # Optimization algorithms
│   │   ├── random_search.py
│   │   ├── simulated_annealing.py
│   │   ├── local_search.py
│   │   ├── genetic_algorithm.py
│   │   └── tabu_search.py
│   ├── domains/        # Domain adapters
│   │   ├── qap/        # Quadratic Assignment Problem
│   │   └── tsp/        # Traveling Salesman Problem
│   ├── benchmarks/     # Benchmark instances
│   │   └── qaplib/     # 138 QAPLIB instances
│   ├── utils/          # Utilities
│   └── visualization/  # Plotting tools
├── tests/              # Test suite (138 tests)
│   ├── test_core/
│   ├── test_algorithms/
│   ├── test_domains/
│   └── test_benchmarks/
├── examples/           # Usage examples
├── docs/               # Documentation
├── scripts/            # Utility scripts
├── pyproject.toml      # Package configuration
├── README.md           # Main documentation
├── CLAUDE.md           # AI assistant guide
└── Makefile
```

**Key Features:**
- 5 optimization methods
- 138 QAPLIB benchmarks
- AI method selector
- Universal domain adapter architecture
- 95% test coverage

---

## 🎮 SimCore - High-Performance Simulation Core Engine

**Location:** `/SimCore/`
**Status:** Early Stage / Foundational Framework

```
SimCore/
├── .github/            # GitHub workflows
├── simcore/            # Main package (planned)
│   └── [to be developed]
├── tests/
├── README.md
└── [configuration files]
```

**Status:** Foundational framework in development.

---

## ⚛️ QMLab - Quantum Machine Learning Laboratory

**Location:** `/qmlab/`
**Status:** Production (https://qmlab.online/)

```
qmlab/
├── .github/            # GitHub workflows
│   └── workflows/
│       ├── ci.yml
│       └── accessibility.yml
├── src/                # React TypeScript source
│   ├── components/     # UI components
│   │   ├── circuit/    # Quantum circuit builder
│   │   ├── bloch/      # Bloch sphere visualization
│   │   ├── training/   # Training dashboard
│   │   └── ui/         # Shared UI components
│   ├── lib/            # Utilities and hooks
│   ├── App.tsx         # Main app component
│   └── main.tsx        # Entry point
├── public/             # Static assets
├── tests/              # Playwright E2E tests
│   ├── test/           # Standard tests
│   ├── accessibility/  # A11y tests
│   └── mobile/         # Mobile tests
├── docs/               # Documentation
├── package.json        # Node.js dependencies
├── vite.config.ts      # Vite build configuration
├── tsconfig.json       # TypeScript configuration
├── tailwind.config.js  # Tailwind CSS configuration
├── README.md
└── CLAUDE.md
```

**Tech Stack:** React 18, TypeScript, Vite, shadcn/ui, Three.js, Tailwind CSS

---

## 📚 Shared Directories

### `/docs/` - Shared Documentation

```
docs/
└── [cross-system documentation]
```

### `/scripts/` - Shared Utility Scripts

```
scripts/
└── [shared automation scripts]
```

### `/tests/` - Integration Tests

```
tests/
└── [cross-system integration tests]
```

### `/reports/` - Analysis and Compliance Reports

```
reports/
├── .github/            # Report generation workflows
└── [generated reports]
```

---

## 🔍 Navigation Tips

### Finding Files

**By System:**
```bash
# MEZAN/ATLAS files
find MEZAN/ATLAS -name "*.py"

# TalAI modules
ls TalAI/

# Optilibria tests
ls optilibria/tests/
```

**By File Type:**
```bash
# All Python files
find . -name "*.py" ! -path "./.git/*" ! -path "./.venv/*"

# All TypeScript files
find . -name "*.ts" -o -name "*.tsx"

# All configuration files
find . -name "pyproject.toml" -o -name "package.json"
```

**By Content:**
```bash
# Search for specific code
grep -r "optimization" --include="*.py"

# Search for TODOs
grep -r "TODO" --include="*.py" --include="*.ts"
```

### Understanding Dependencies

```bash
# Python dependencies
find . -name "pyproject.toml" -o -name "requirements*.txt"

# Node.js dependencies
find . -name "package.json"
```

### Running Tests

```bash
# Root level
make test

# MEZAN/ATLAS
cd MEZAN/ATLAS && make test

# Optilibria
cd optilibria && pytest

# QMLab
cd qmlab && npm run test
```

---

## 📊 Repository Statistics

**Updated:** 2025-11-19 (post-cleanup)

- **Total Files:** ~1,000+ across all systems
- **Total Lines:** 100,000+ lines of code
- **Systems:** 5 major
- **Modules:** 28+ in TalAI
- **Tests:** 138+ in Optilibria, comprehensive across systems
- **Documentation:** 100+ markdown files
- **Languages:** Python (primary), TypeScript/JavaScript (QMLab)
- **Configuration Files:**
  - 1 root .gitignore (consolidated from 29)
  - 1 root CODEOWNERS (consolidated from 11)
  - 27+ pyproject.toml files
  - 1 root pyproject.toml (workspace)

---

## 🗺️ Navigation Flowchart

```
START HERE
    ↓
Read ROOT/README.md (overview)
    ↓
Identify your interest:
    ├── AI Orchestration? → MEZAN/ATLAS/START_HERE.md
    ├── Research Automation? → TalAI/MASTER_INDEX.md
    ├── Optimization? → optilibria/README.md
    ├── Quantum ML? → qmlab/README.md
    └── Simulation? → SimCore/README.md
    ↓
Read system-specific CLAUDE.md for AI assistance
    ↓
Check pyproject.toml for dependencies
    ↓
Run system setup and tests
    ↓
Read system docs/ directory for deep dive
```

---

## 📞 Questions?

- **General Questions:** See `README.md` and `CLAUDE.md`
- **Contributing:** See `CONTRIBUTING.md`
- **Security:** See `SECURITY.md`
- **Code Ownership:** See `CODEOWNERS`
- **Project Vision:** See `PROJECT.md`

**Contact:** Meshal Alawein (meshal@berkeley.edu)

---

*Last Updated: 2025-11-19*
*This structure reflects the state after repository cleanup and organization.*
