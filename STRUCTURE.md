# AlaweinOS Repository Structure

**Navigation guide for the AlaweinOS monorepo**

---

## Directory Layout

```
AlaweinOS/
├── .archive/                 # Historical documentation (38+ files)
│   ├── session-reports/
│   ├── cycle-reports/
│   ├── sprint-reports/
│   ├── handoffs/
│   ├── completion-reports/
│   └── README.md
├── .claude/                  # Claude Code configuration
│   └── instructions.md
├── .github/                  # GitHub workflows and templates
│   ├── workflows/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── header.svg, divider.svg
├── docs/                     # Shared monorepo documentation
│   └── README.md
├── reports/                  # Compliance and analysis reports
│   ├── README.md
│   ├── CODE_OF_CONDUCT.md
│   └── SECURITY.md
├── scripts/                  # Shared utility scripts
│   └── README.md
├── MEZAN/                    # Enterprise Automation Platform
│   ├── ATLAS/                # Multi-agent AI orchestration
│   ├── Libria/               # Novel optimization algorithms
│   ├── docs/
│   ├── START_HERE.md
│   └── README.md
├── TalAI/                    # AI Research Platform (28+ modules)
│   ├── abstract-writer/
│   ├── grant-writer/
│   ├── lit-review-bot/
│   ├── {25+ more modules}/
│   ├── MASTER_INDEX.md
│   └── README.md
├── optilibria/               # Universal Optimization Framework
│   ├── optilibria/           # Core library
│   ├── benchmarks/
│   ├── examples/
│   ├── docs/
│   ├── CLAUDE.md
│   └── README.md
├── SimCore/                  # Interactive Scientific Computing
│   ├── src/                  # React/TypeScript source
│   ├── public/
│   ├── docs/
│   ├── scripts/
│   ├── SIMCORE_CLAUDE_CODE_DOCUMENTATION.md
│   └── README.md
├── qmlab/                    # Quantum ML Laboratory
│   ├── src/                  # React/TypeScript source
│   ├── public/
│   ├── docs/
│   ├── CLAUDE.md
│   └── README.md
├── README.md                 # Organization overview
├── PROJECT.md                # Comprehensive project documentation
├── STRUCTURE.md              # This file
├── CLAUDE.md                 # AI assistant comprehensive guide
├── CONTRIBUTING.md           # Contribution guidelines
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── CODEOWNERS
└── LICENSE
```

---

## How to Navigate

### 🎯 I want to...

#### **Learn about the organization**
→ Start with `README.md`
→ Read `PROJECT.md` for comprehensive overview
→ Check `CLAUDE.md` for detailed system descriptions

#### **Work with a specific system**

**MEZAN (Enterprise Automation):**
→ `MEZAN/START_HERE.md` - Entry point
→ `MEZAN/ATLAS/START_HERE.md` - ATLAS subsystem
→ `MEZAN/Libria/EXECUTIVE_SUMMARY.md` - Optimization algorithms

**TalAI (Research Platform):**
→ `TalAI/README.md` - Overview
→ `TalAI/MASTER_INDEX.md` - Module index
→ `TalAI/{module}/README.md` - Specific module docs

**Optilibria (Optimization):**
→ `optilibria/README.md` - Complete guide
→ `optilibria/CLAUDE.md` - AI assistant guide
→ `optilibria/examples/` - Usage examples

**SimCore (Scientific Computing):**
→ `SimCore/README.md` - Platform overview
→ `SimCore/SIMCORE_CLAUDE_CODE_DOCUMENTATION.md` - Full documentation
→ `SimCore/docs/DEVELOPMENT.md` - Development guide

**qmlab (Quantum ML):**
→ `qmlab/README.md` - Platform overview
→ `qmlab/CLAUDE.md` - AI assistant guide
→ `qmlab/docs/` - Detailed documentation

#### **Understand system architecture**
→ `PROJECT.md` - System interdependencies
→ `{system}/docs/` - System-specific architecture
→ `CLAUDE.md` - Detailed technical descriptions

#### **Contribute to the project**
→ `CONTRIBUTING.md` - Contribution guidelines
→ `CODE_OF_CONDUCT.md` - Community guidelines
→ `{system}/CONTRIBUTING.md` - System-specific guidelines (if exists)

#### **Find historical information**
→ `.archive/README.md` - Archive index
→ `.archive/{category}/` - Specific historical docs

#### **Set up development environment**
→ `PROJECT.md` - Quick start per system
→ `{system}/README.md` - System setup
→ `{system}/docs/DEVELOPMENT.md` - Development details

---

## System Entry Points

| System | Primary Entry | Documentation | Type |
|--------|--------------|---------------|------|
| MEZAN | `MEZAN/START_HERE.md` | `MEZAN/README.md` | Python |
| TalAI | `TalAI/MASTER_INDEX.md` | `TalAI/README.md` | Python |
| Optilibria | `optilibria/README.md` | `optilibria/CLAUDE.md` | Python |
| SimCore | `SimCore/README.md` | `SimCore/SIMCORE_CLAUDE_CODE_DOCUMENTATION.md` | TypeScript |
| qmlab | `qmlab/README.md` | `qmlab/CLAUDE.md` | TypeScript |

---

## File Naming Conventions

### Documentation Files
- `README.md` - Overview and quick start (UPPERCASE)
- `CLAUDE.md` - AI assistant guidance (UPPERCASE)
- `START_HERE.md` - Entry point (UPPERCASE)
- `{topic}.md` - Specific documentation (lowercase with hyphens)

### Code Files
- **Python**: `lowercase_with_underscores.py`
- **TypeScript**: `camelCase.ts` or `PascalCase.tsx` (components)
- **Configuration**: `.config-name` or `config-name.{ext}`

### Branches
- Feature branches: `claude/feature-name-sessionid`
- All work branches must start with `claude/`

---

## Directory Purposes

### Root Directories

**`.archive/`**
Historical documentation preserved for reference. Organized by category (sessions, cycles, sprints, handoffs, completion reports).

**`.claude/`**
Claude Code AI assistant configuration and instructions.

**`.github/`**
GitHub Actions workflows, PR templates, and repository assets.

**`docs/`**
Shared monorepo documentation that applies across systems.

**`reports/`**
Compliance reports, analysis outputs, and quality metrics.

**`scripts/`**
Shared utility scripts for development, testing, and deployment.

### System Directories

Each major system (`MEZAN/`, `TalAI/`, `optilibria/`, `SimCore/`, `qmlab/`) is independently structured with:
- `src/` or package directory - Source code
- `tests/` - Test suites
- `docs/` - System documentation
- `examples/` - Usage examples (where applicable)
- `README.md` - System overview
- Configuration files (package.json, pyproject.toml, etc.)

---

## Adding New Content

### New System
1. Create top-level directory: `{SystemName}/`
2. Add `README.md` with overview
3. Add `CLAUDE.md` or equivalent for AI guidance
4. Update `PROJECT.md` with system description
5. Update this `STRUCTURE.md` with navigation
6. Update root `README.md` if featured

### New Module (within system)
1. Create module directory within system
2. Add module `README.md`
3. Update system's index/master documentation
4. Add to system's README if significant

### New Documentation
1. Determine scope (monorepo vs. system-specific)
2. Place in appropriate `docs/` directory
3. Update relevant navigation files
4. Link from related documents

### Historical Reports
1. Place in `.archive/{category}/`
2. Update `.archive/README.md` if significant
3. Remove from active documentation

---

## Quick Reference: Common Paths

**Main Documentation:**
- `/README.md` - Organization overview
- `/PROJECT.md` - Comprehensive project docs
- `/CLAUDE.md` - AI assistant guide (20KB)
- `/CONTRIBUTING.md` - How to contribute

**System READMEs:**
- `/MEZAN/README.md`
- `/TalAI/README.md`
- `/optilibria/README.md`
- `/SimCore/README.md`
- `/qmlab/README.md`

**Entry Points:**
- `/MEZAN/START_HERE.md`
- `/TalAI/MASTER_INDEX.md`
- `/optilibria/README.md`
- `/SimCore/SIMCORE_CLAUDE_CODE_DOCUMENTATION.md`
- `/qmlab/CLAUDE.md`

**Historical:**
- `/.archive/README.md`

---

## Navigation Tips

1. **Start with README.md** for overview
2. **Read PROJECT.md** for comprehensive understanding
3. **Check STRUCTURE.md** (this file) for navigation
4. **Use system entry points** for deep dives
5. **Review CLAUDE.md** for AI assistant guidance
6. **Explore .archive/** for historical context

---

## Questions?

- **General questions:** See PROJECT.md or contact meshal@berkeley.edu
- **System-specific:** Check system's README.md or CLAUDE.md
- **Contributing:** See CONTRIBUTING.md
- **Historical:** Check .archive/README.md

---

**Last Updated:** 2025-11-19
**Maintainer:** Dr. Meshal Alawein (meshal@berkeley.edu)
