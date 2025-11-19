Repository Conventions, Structure, and Cleanup Plan

Summary
- This document defines naming and documentation conventions, presents accurate current structure diagrams, and lists concrete cleanup actions. It does not rename or remove anything yet.

Top-Level Overview
- Projects: `ATLAS`, `Libria`
- MEZAN docs hub under `MEZAN/` (README, ARCHITECTURE, etc.)
- Meta docs consolidated under `docs/` and `MEZAN/`
- Datasets: ASlib scenarios in `Libria/libria-meta/aslib_data`

Current Structure (top-down)
- .archive/ (legacy archive) — contains `Chats/`, `Reports/` (corrected)
- .claude/
- ATLAS/
- Libria/
- MEZAN/
- Root-level docs (*.md)
- docker-compose.yml

ATLAS (selected)
- docs/
- src/atlas/
- tests/
- atlas-core/
  - atlas_core/
  - tests/
  - venv/ [committed virtualenv]

Libria (selected)
- libria-meta/
  - aslib_data/ [datasets]
  - baselines/
  - benchmark/
  - libria_meta/
  - tests/
- other components: `libria-core/`, `libria-graph/`, etc.

Tree Diagrams (accurate excerpts)
- Top-level
  - ATLAS
  - Libria
  - START_HERE.md
  - FILE_MANIFEST.md
  - docker-compose.yml
  - .archieve/
  - .claude/

- Libria (depth ≤ 3)
  - libria-meta/
    - aslib_data/
    - baselines/
    - benchmark/
    - libria_meta/
    - tests/
  - libria-core/
  - libria-graph/
  - libria-evo/
  - ...

- ATLAS (depth ≤ 3)
  - src/atlas/
  - docs/
  - tests/
  - atlas-core/
    - atlas_core/
    - tests/
    - venv/ [committed]

Naming Conventions (proposed)
- Directories (projects): lowercase-kebab, e.g., `libria-meta`, `atlas-core`
- Python packages: lowercase_snake, e.g., `atlas_core`, `libria_meta`
- Tests: `tests/` adjacent to source or at project root (consistent within ATLAS and Libria)
- Data folders: lowercase-kebab; datasets pinned under a single `data/` root when possible (ASlib stays under `libria-meta/aslib_data`)
- Docs files: lowercase-kebab for filenames (e.g., `start-here.md`, `project-index.md`); page titles inside the file use Title Case

Documentation Layout (proposed)
- Root
  - `README.md`: brief overview and pointers to ATLAS/Libria
  - `start-here.md`: quick start across projects
  - `contributing.md`, `code-of-conduct.md`
- ATLAS/
  - `README.md` with ATLAS-specific quick start
  - `docs/` for guides, architecture, API
- Libria/
  - `README.md` with Libria-specific quick start
  - `docs/` for baselines, evaluation, datasets

Completed Cleanups
- Typos/misnamed folders
  - `.archieve/` → `.archive/` (migrated contents)
  - `.archieve/Rpeorts/` → `.archive/Reports/` (corrected)
- Committed transient artifacts
  - Remove committed virtualenv `ATLAS/atlas-core/venv/` and add to `.gitignore`
  - Remove `**/.pytest_cache/` and add to `.gitignore` (present under `ATLAS/` and `Libria/libria-meta/`)
- Dataset vendor folders
  - `Libria/libria-meta/aslib_data/.git` and `.github/` are vendor metadata; consider pruning from the repo if not required
- Duplicated “start here” docs
  - Root `START_HERE.md` and ATLAS `START_HERE.md` overlap; consolidate to one canonical entry per project with consistent naming (`start-here.md`)
- Mixed casing and verbose filenames
  - Long, all-caps root docs (e.g., `COMPREHENSIVE_PROJECT_HANDOFF_FOR_SIDER_AI.md`): consider moving into `docs/` and renaming using lowercase-kebab

Suggested Renames (mapping)
- `START_HERE.md` (root) → keep as canonical; `start-here.md` mirrors path
- `ATLAS/atlas-core/venv/` → remove; add `atlas-core/venv/` to gitignore
- Keep large root docs referenced via `MEZAN/` copies and `docs/` index

Git Hygiene (proposed .gitignore entries)
- `**/.pytest_cache/`
- `**/__pycache__/`
- `**/.ipynb_checkpoints/`
- `**/venv/`
- `**/.DS_Store`

Adoption Plan
- Step 1: Approve the rename map and .gitignore updates
- Step 2: Apply renames + update intra-repo links and imports (search/replace)
- Step 3: Remove committed caches/venv; add protective .gitignore rules
- Step 4: Create per-project READMEs; migrate root long-form docs into `docs/`
- Step 5: CI check for forbidden artifacts (venv, caches) and naming lint

Notes
- All diagrams and lists above reflect the actual repository contents. No renames were performed by this document.
