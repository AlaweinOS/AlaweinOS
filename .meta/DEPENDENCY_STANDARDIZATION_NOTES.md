# Dependency Management Standardization Notes

**Date:** 2025-11-19
**Status:** Root configuration created; individual package standardization recommended for future

## Current State

The AlaweinOS monorepo contains 27+ Python packages, each with its own `pyproject.toml` file. This is the correct structure for a monorepo with independently deployable packages.

### Package Distribution

- **MEZAN**: 1 pyproject.toml (ATLAS)
- **TalAI**: 26 pyproject.toml files (one per module)
- **Optilibria**: 1 pyproject.toml
- **SimCore**: No pyproject.toml yet
- **QMLab**: Node.js project (package.json)

## Completed Actions

✅ Created root `pyproject.toml` with:
- Workspace-level metadata
- Common development dependencies
- Standardized tool configurations (black, ruff, mypy, pytest)
- Consistent Python version (>=3.9)
- Apache 2.0 license declaration

## Identified Inconsistencies

### 1. Author Metadata
- ❌ "Meshal Alawein" (optilibria)
- ❌ "IDEAS Team" (TalAI modules)
- ❌ "ATLAS Team" (MEZAN/ATLAS)

**Recommendation:** Standardize to `{name = "Meshal Alawein", email = "meshal@berkeley.edu"}`

### 2. License Declaration
- ❌ "Apache-2.0" (optilibria)
- ❌ "MIT" (some TalAI modules)
- ❌ Not specified (some packages)

**Recommendation:** Standardize to `{text = "Apache-2.0"}` (per root LICENSE file)

### 3. Python Version Requirements
- ❌ ">=3.8" (some TalAI modules)
- ❌ ">=3.9" (optilibria, MEZAN/ATLAS)

**Recommendation:** Standardize to `">=3.9"` for consistency

### 4. Build System Requirements
- ❌ `setuptools>=61.0` (some packages)
- ❌ `setuptools>=65.0` (optilibria)

**Recommendation:** Standardize to `setuptools>=65.0` (modern version)

## Recommended Future Actions

### Priority 1: Metadata Standardization
- [ ] Update all `authors` fields to use "Meshal Alawein <meshal@berkeley.edu>"
- [ ] Standardize license to "Apache-2.0" across all packages
- [ ] Add missing license declarations

### Priority 2: Version Requirements
- [ ] Standardize Python version to ">=3.9"
- [ ] Standardize setuptools to ">=65.0"
- [ ] Verify all packages work with Python 3.9+

### Priority 3: Tool Configuration
- [ ] Ensure all packages use ruff (not flake8/pylint)
- [ ] Ensure all packages use black with line-length=100
- [ ] Add mypy configuration where missing

### Priority 4: Documentation
- [ ] Add consistent README.md templates for all packages
- [ ] Document development setup in each package
- [ ] Create CONTRIBUTING.md guidelines

## Migration Script (Future Work)

A script should be created to automate standardization:

```bash
#!/bin/bash
# scripts/standardize-pyproject.sh

# Update all pyproject.toml files to use consistent metadata
find . -name "pyproject.toml" -type f -exec sed -i \
  's/name = "IDEAS Team"/name = "Meshal Alawein", email = "meshal@berkeley.edu"}/g' {} \;

# Additional sed commands for other standardizations...
```

## Current Approach

For this cleanup session, we've taken a pragmatic approach:
1. ✅ Created root pyproject.toml for workspace management
2. ✅ Documented inconsistencies and recommendations
3. ⏭️ Deferred individual package updates to future work

This allows us to return to MEZAN development without risking breaking changes to existing packages.

## References

- Root `pyproject.toml`: `/home/user/AlaweinOS/pyproject.toml`
- Python Packaging Guide: https://packaging.python.org/
- Monorepo Best Practices: https://monorepo.tools/

---

**Next Session:** Consider implementing automated standardization script and testing across all packages.
