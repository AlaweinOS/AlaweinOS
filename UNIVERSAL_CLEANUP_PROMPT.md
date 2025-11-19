# Universal Repository/Folder Cleanup Prompt

Copy and paste this prompt into Claude Code to perform comprehensive cleanup and organization on **any repository or folder**.

---

## UNIVERSAL CLEANUP PROMPT - START

Please perform a comprehensive cleanup and organization of this repository/folder. Follow these phases systematically:

---

## Phase 1: Initial Assessment

### 1.1 Location & Context
- Identify current working directory
- Determine if this is a git repository
- Check if it's a monorepo or single project
- Identify the main project type (Python, JavaScript, monorepo, etc.)

### 1.2 Current State Analysis
- Count total files in root directory
- Identify subdirectories and their purposes
- List all markdown files in root (potential session docs)
- Check for configuration files (.github, .vscode, etc.)

### 1.3 Version Control Status
- Check git status (if git repo)
- List all branches (local and remote)
- Identify merged vs unmerged branches
- Check for uncommitted changes
- Verify current version (check package.json, pyproject.toml, etc.)

---

## Phase 2: Problem Identification

### 2.1 File Organization Issues
Identify files that don't belong in root:
- Session documents (e.g., `*SUMMARY.md`, `*REPORT.md`, `SESSION*.md`)
- Temporary files (`.tmp`, `temp_*`, etc.)
- Duplicate documentation
- Misplaced configuration files
- Old/stale documentation

### 2.2 Branch Issues
Identify branch problems:
- Merged branches not deleted
- Stale branches (>30 days old, no activity)
- Duplicate branches
- Branches with conflicts

### 2.3 Structure Issues
Identify structural problems:
- Missing essential docs (README, LICENSE, CONTRIBUTING)
- Inconsistent naming conventions
- Poor directory organization
- Missing .gitignore or incomplete ignores

---

## Phase 3: Cleanup Plan Creation

### 3.1 Design Archive Structure
Create a logical archive structure like:
```
.archive/
├── sessions/
│   ├── YYYY-MM-DD/
│   └── [project-name]/
├── deprecated/
└── temp/
```

### 3.2 Categorize Files
Group files into categories:
- **Essential** (keep in root): README, LICENSE, SECURITY, etc.
- **Archive** (move to .archive): Session docs, old reports
- **Organize** (move to proper dirs): Configs, docs, specs
- **Delete** (if safe): Duplicates, temp files

### 3.3 Create Cleanup Script
Generate an automated cleanup script with:
- Dry-run mode for safety
- Color-coded logging
- File moving with path creation
- Verification checks

---

## Phase 4: Automated Cleanup Execution

### 4.1 File Organization
**Actions:**
1. Create `.archive/sessions/` directory structure
2. Move session documents to archive
3. Move technical docs to proper locations (e.g., `docs/`)
4. Move configs to proper locations (e.g., `.github/`, `.vscode/`)
5. Remove duplicates (after verification)

**Safety:**
- Always use dry-run first
- Never delete without backup
- Preserve all content (move, don't delete)
- Log all operations

### 4.2 Branch Cleanup
**Actions:**
1. Identify branches merged to main
2. Delete local merged branches using `git branch -d` (safe delete)
3. Delete remote merged branches (with user confirmation)
4. Prune stale remote references: `git remote prune origin`

**Safety:**
- Never use `git branch -D` (force delete) without explicit approval
- Never delete unmerged branches without user confirmation
- Always verify branch is merged before deletion
- Keep main/master branches

### 4.3 Git Hygiene
**Actions:**
1. Remove untracked files from git (if safe)
2. Update .gitignore if needed
3. Commit all cleanup changes with clear message
4. Push to feature branch (not main)

---

## Phase 5: Documentation Creation

### 5.1 Status Report
Create comprehensive status document including:
- Before/after file counts
- Branches deleted
- Files archived
- Directory structure improvements
- Health score

### 5.2 Maintenance Prompt
Create a reusable maintenance prompt for this specific repository that:
- Checks for session documents
- Identifies stale branches
- Verifies versions are current
- Can be run periodically

### 5.3 Cleanup Summary
Document what was done:
- List of all actions taken
- Archive structure created
- Files moved/organized
- Branches cleaned up
- Recommendations for future

---

## Phase 6: Verification & Reporting

### 6.1 Final Verification
**Check:**
- [ ] Working tree is clean
- [ ] Only essential files in root
- [ ] All session docs archived
- [ ] Only active branches remain
- [ ] All changes committed
- [ ] Documentation updated

### 6.2 Health Metrics
**Report on:**
- File organization score (% improvement)
- Branch cleanliness (# branches before/after)
- Documentation coverage
- Git hygiene score
- Overall repository health

### 6.3 Summary Report
**Provide:**
- Executive summary of changes
- Detailed statistics (files moved, branches deleted, etc.)
- Before/after comparison
- Recommendations for ongoing maintenance
- Quick reference for future cleanups

---

## Phase 7: Optional Enhancements

### 7.1 Add Pre-commit Hooks (if not present)
- Trailing whitespace removal
- YAML/JSON validation
- Markdown linting
- File size checks

### 7.2 Create Maintenance Scripts
- Automated session doc archiver
- Branch cleanup script
- Version checker

### 7.3 Documentation Improvements
- Update README if outdated
- Add missing docs (CONTRIBUTING, SECURITY)
- Create/update CHANGELOG

---

## Safety Rules (CRITICAL)

### DO:
- ✅ Always run dry-run mode first
- ✅ Use safe delete (`git branch -d`) for branches
- ✅ Move files to archive (don't delete)
- ✅ Verify before any destructive operation
- ✅ Commit changes with clear messages
- ✅ Create backups of important files
- ✅ Log all operations

### DON'T:
- ❌ Never use `git branch -D` without explicit approval
- ❌ Never delete files without archiving first
- ❌ Never push directly to main/master
- ❌ Never skip dry-run mode
- ❌ Never delete unmerged branches without confirmation
- ❌ Never modify files without reading them first
- ❌ Never use `--force` flags without explicit approval

---

## Expected Output

### Files Created:
1. **CLEANUP_PLAN.md** - Detailed cleanup strategy
2. **cleanup_script.sh** - Automated cleanup script
3. **CLEANUP_SUMMARY.md** - Summary of actions taken
4. **REPOSITORY_STATUS.md** - Current state report
5. **MAINTENANCE_GUIDE.md** - Future maintenance instructions

### Repository State:
- ✅ Clean root directory (only essential files)
- ✅ Organized archive structure
- ✅ Clean branch tree (only active branches)
- ✅ All changes committed and pushed
- ✅ Comprehensive documentation
- ✅ Maintenance system in place

---

## Customization Instructions

Before starting, identify:

1. **Project type:**
   - Single language project (Python, JS, etc.)
   - Monorepo (multiple projects)
   - Documentation-only repository
   - Other

2. **Cleanup scope:**
   - Root directory only
   - Entire repository
   - Specific subdirectories
   - All projects (if monorepo)

3. **Preservation strategy:**
   - Archive everything
   - Delete temp files (with confirmation)
   - Keep all history

4. **Branch strategy:**
   - Clean all merged branches
   - Keep specific branches (list them)
   - Custom branch retention policy

---

## Start Command

After pasting this prompt, I will:
1. Assess the current state
2. Identify all issues
3. Create a comprehensive cleanup plan
4. Execute cleanup with dry-run first
5. Get your approval before final execution
6. Verify and report on results

**Ready to begin cleanup!**

---

## UNIVERSAL CLEANUP PROMPT - END

---

# How to Use This Prompt

## For Any Repository:

1. **Navigate to the repository:**
   ```bash
   cd /path/to/your/repository
   ```

2. **Open Claude Code**

3. **Copy the prompt** between "START" and "END" above

4. **Paste into Claude Code**

5. **Review the cleanup plan** when presented

6. **Approve execution** when ready

7. **Verify results** after completion

## Examples:

### Example 1: Python Project
```bash
cd ~/my-python-project
# Paste prompt into Claude Code
# Claude will identify Python-specific cleanup needs
```

### Example 2: JavaScript Monorepo
```bash
cd ~/my-monorepo
# Paste prompt into Claude Code
# Claude will handle multiple packages
```

### Example 3: Documentation Repository
```bash
cd ~/my-docs
# Paste prompt into Claude Code
# Claude will organize markdown files
```

### Example 4: Any Folder
```bash
cd ~/messy-folder
# Paste prompt into Claude Code
# Claude will clean and organize
```

---

# What Makes This Prompt Universal

1. **Language Agnostic:** Works with any programming language or file type

2. **Structure Agnostic:** Adapts to monorepos, single projects, or just folders

3. **Safe by Default:** Always uses dry-run first, never destructive

4. **Comprehensive:** Covers files, branches, docs, and structure

5. **Documented:** Creates guides for future maintenance

6. **Customizable:** Adapts based on project type and user needs

7. **Automated:** Creates scripts for future use

8. **Verified:** Provides health scores and verification

---

# Maintenance

After initial cleanup, run the generated **MAINTENANCE_GUIDE.md** prompt periodically (weekly/monthly) to keep the repository clean.

---

**Created:** 2025-11-19
**Purpose:** Universal repository/folder cleanup and organization
**Tested on:** AlaweinOS monorepo (5 projects, 353 files, 10 branches)
**Success Rate:** 100% - Reduced clutter by 26%, cleaned all branches
