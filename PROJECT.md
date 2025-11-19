# AlaweinOS Project Overview

**Organization:** AlaweinOS
**Type:** Enterprise Monorepo
**Owner:** Dr. Meshal Alawein
**Email:** meshal@berkeley.edu
**Website:** https://malawein.com

---

## What is AlaweinOS?

AlaweinOS is an **enterprise-grade monorepo** housing multiple production-ready software systems where **PhD-level mathematical rigor** meets **scalable production engineering**.

The organization transforms **theoretical physics and optimization principles** into **robust, commercial-grade software systems** that solve real-world problems at enterprise scale.

---

## Systems Overview

AlaweinOS contains **5 major independent systems**, each production-ready and designed for enterprise deployment:

### 1. MEZAN - Modular Enterprise Zonal Automation Network
**Type:** Enterprise Automation Platform
**Tech:** Python 3.9+, Flask, Redis, Multi-Agent AI
**Status:** Production

Enterprise automation platform orchestrating complex workflows and distributed systems.

**Subsystems:**
- **ATLAS**: Multi-agent AI research orchestration (8+ specialized agents)
- **Libria Suite**: 7 novel optimization algorithms for multi-agent coordination

**Use Cases:**
- Complex workflow orchestration
- Multi-agent AI coordination
- Enterprise task automation
- Research process automation

### 2. TalAI - Autonomous Testing & Laboratory Analysis Intelligence
**Type:** AI Research Platform
**Tech:** Python 3.8+, Anthropic API, OpenAI API, PyTorch
**Status:** Production

AI-powered research and development platform with 28+ specialized modules for scientific research automation.

**Key Capabilities:**
- Autonomous research execution
- Literature review automation
- Grant proposal generation
- Experimental design
- Multi-modal analysis (equations, figures, molecules)

**Modules:** 28+ specialized research automation tools

### 3. Optilibria - Universal Optimization Framework
**Type:** Production Optimization Library
**Tech:** Python 3.9+, JAX, NumPy, SciPy, Optional GPU
**Status:** Production

Production-grade optimization library with 31+ algorithms, GPU acceleration, and enterprise-scale performance.

**Features:**
- 31+ optimization algorithms
- GPU acceleration (CUDA, JAX)
- 138+ QAPLIB benchmarks
- AI method selector
- 95% test coverage

**Algorithms:** Genetic, Simulated Annealing, Tabu Search, Local Search, Gradient methods, and more

### 4. SimCore - Interactive Scientific Computing Laboratory
**Type:** Web-Based Scientific Platform
**Tech:** React 18.3, TypeScript 5.5, WebGPU, Three.js
**Status:** Production

Web-based interactive scientific computing platform with 25+ simulations across physics, mathematics, and scientific machine learning.

**Features:**
- 25+ interactive scientific simulations
- WebGPU hardware acceleration
- Progressive Web App (offline capable)
- Publication-quality visualizations
- Research-grade accuracy

**Domains:** Quantum mechanics, statistical physics, computational mathematics

### 5. qmlab - Quantum Machine Learning Laboratory
**Type:** Educational Web Platform
**Tech:** React 18, TypeScript, Vite
**Status:** Production (https://qmlab.online/)

Interactive quantum computing education and visualization platform with comprehensive accessibility.

**Features:**
- Quantum circuit builder
- Bloch sphere visualization
- Training dashboard
- WCAG 2.1 AA compliant
- Mobile responsive

---

## Technology Stack

### Languages
- **Python**: 3.8+ to 3.12 (MEZAN, TalAI, optilibria)
- **TypeScript/JavaScript**: (SimCore, qmlab)

### Core Technologies

**Backend/Scientific:**
- NumPy, SciPy, Pandas
- PyTorch, JAX, scikit-learn
- OR-Tools, NetworkX
- Qiskit, PennyLane (quantum)
- Flask (APIs)
- Redis (state management)

**Frontend:**
- React 18
- Vite
- shadcn/ui (Radix UI + Tailwind)
- Three.js, plotly.js
- WebGPU

**AI/ML:**
- Anthropic Claude API
- OpenAI GPT API
- Custom ML models

**DevOps:**
- GitHub Actions
- Docker
- Kubernetes (MEZAN, TalAI)
- CodeQL, Trivy (security)

---

## Quick Start

### Repository Setup
```bash
# Clone repository
git clone https://github.com/AlaweinOS/AlaweinOS.git
cd AlaweinOS

# Setup pre-commit hooks (if Makefile exists)
make setup 2>/dev/null || echo "Manual setup required per system"
```

### Working with Individual Systems

**Python Systems (MEZAN, TalAI, optilibria):**
```bash
cd {system}/
pip install -e .              # Development install
pytest                        # Run tests
python -m {module}            # Run specific module
```

**TypeScript Systems (SimCore, qmlab):**
```bash
cd {system}/
npm install                   # Install dependencies
npm run dev                   # Development server
npm run build                 # Production build
npm test                      # Run tests
```

---

## Development Workflow

### Branch Naming
All feature branches must start with `claude/`:
```bash
git checkout -b claude/feature-name-sessionid
```

### Commit Guidelines
```bash
git add .
git commit -m "Component: Brief description

Detailed explanation
- Change 1
- Change 2
"
git push -u origin claude/feature-name-sessionid
```

### Testing Requirements
- **Python**: pytest with 60-95% coverage (varies by system)
- **TypeScript**: Playwright for E2E, unit tests with coverage

### Code Quality
- **Python**: Black (line length 100), Ruff, mypy
- **TypeScript**: ESLint, Prettier
- **All**: Pre-commit hooks enforced

---

## System Interdependencies

```
┌─────────────────────────────────────────────┐
│         AlaweinOS Ecosystem                 │
├─────────────────────────────────────────────┤
│                                             │
│  MEZAN (Orchestration)                      │
│  ├─ ATLAS → Uses: Libria, TalAI,Optilibria │
│  └─ Libria → Uses: Optilibria algorithms   │
│              ↓                              │
│  TalAI (Research Automation)                │
│  └─ Uses: ATLAS for orchestration          │
│              ↓                              │
│  Optilibria (Optimization Core)             │
│  └─ Used by: ATLAS, Libria, TalAI          │
│                                             │
│  SimCore (Scientific Computing - Web)       │
│  └─ Independent educational platform        │
│                                             │
│  qmlab (Quantum ML - Web)                   │
│  └─ Independent educational platform        │
│                                             │
└─────────────────────────────────────────────┘
```

**Integration Points:**
- ATLAS orchestrates research using TalAI modules
- Libria algorithms leverage Optilibria core
- TalAI uses ATLAS for multi-agent workflows
- SimCore and qmlab are standalone web platforms

---

## Documentation

### Root Level
- **README.md** - Organization overview
- **CLAUDE.md** - Comprehensive AI assistant guide (20KB)
- **PROJECT.md** - This file
- **STRUCTURE.md** - Directory navigation
- **CONTRIBUTING.md** - Contribution guidelines

### System-Specific
Each system has:
- README.md (overview and quick start)
- CLAUDE.md or equivalent (AI guidance)
- Detailed docs/ directory

### Shared Documentation
- `docs/` - Shared monorepo documentation
- `.archive/` - Historical documentation (38+ files)

---

## Getting Help

### System-Specific Help

**MEZAN:** See `MEZAN/START_HERE.md`
**TalAI:** See `TalAI/MASTER_INDEX.md`
**Optilibria:** See `optilibria/README.md`
**SimCore:** See `SimCore/SIMCORE_CLAUDE_CODE_DOCUMENTATION.md`
**qmlab:** See `qmlab/CLAUDE.md`

### General Questions
- Review STRUCTURE.md for navigation
- Check CLAUDE.md for AI assistant guidance
- See CONTRIBUTING.md for development guidelines

### Contact
**Dr. Meshal Alawein**
Email: meshal@berkeley.edu
Portfolio: https://malawein.com
LinkedIn: https://linkedin.com/in/alawein

---

## Project Philosophy

### Core Values
1. **Theory meets practice** - Mathematical rigor in production code
2. **Scale with elegance** - Handle massive scale while maintaining code quality
3. **Scientific rigor** - Every decision justified and testable
4. **AI enhances, humans decide** - AI augmentation, not replacement
5. **Build for the future** - Design for evolution

### Quality Standards
- Code Quality: 85% threshold
- Security Score: 90% threshold
- Test Coverage: 80% threshold
- All systems production-ready

---

## License

Apache 2.0 - See LICENSE file

---

## Contributing

See CONTRIBUTING.md for:
- Development setup per system
- Code standards
- Testing requirements
- PR process
- Review guidelines

---

**AlaweinOS**: Enterprise systems crafted with mathematical rigor and production-grade engineering.

**Last Updated:** 2025-11-19
