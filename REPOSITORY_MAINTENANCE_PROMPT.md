# Repository Maintenance & Cleanup - Master Prompt

Copy and paste this prompt into Claude Code whenever you need comprehensive repository maintenance:

---

## PROMPT START

Please perform a comprehensive repository maintenance check and cleanup for the AlaweinOS monorepo. Execute the following phases in order:

### Phase 1: Repository State Assessment

1. **Current Branch & Status**
   - Check current branch and git status
   - Verify working directory is clean
   - Identify any uncommitted changes

2. **Version Verification**
   - Confirm MEZAN is at latest version (check `pyproject.toml` and `MEZAN/core/__init__.py`)
   - Verify all project versions are consistent
   - Check if any updates are needed

3. **Branch Analysis**
   - List all local branches: `git branch`
   - List all remote branches: `git branch -r`
   - Identify merged branches: `git branch --merged main`
   - Identify unmerged branches: `git branch --no-merged main`
   - Check for stale branches (older than 30 days with no activity)

### Phase 2: Sync Verification

1. **Remote Sync Check**
   - Switch to main: `git checkout main`
   - Fetch all remotes: `git fetch --all --prune`
   - Pull latest from main: `git pull origin main`
   - Verify local main matches remote: `git log origin/main..main` (should be empty)
   - Check if there are unpushed commits on main

2. **Cross-Project Consistency**
   - Verify all 5 major systems (MEZAN, TalAI, optilibria, SimCore, qmlab) have consistent structure
   - Check that documentation is up to date
   - Verify no duplicate or conflicting files

### Phase 3: Branch Cleanup (Safe)

**IMPORTANT: Only clean up branches that are:**
- ✅ Fully merged to main (verified by git)
- ✅ Associated with closed/merged PRs
- ✅ Older than 7 days

**Steps:**

1. **Identify Safe-to-Delete Branches**
   ```bash
   # Local branches merged to main
   git branch --merged main | grep -v "main\|master\|\*"

   # Remote branches merged to main
   git branch -r --merged main | grep -v "main\|master\|HEAD"
   ```

2. **For Each Merged Branch:**
   - Verify it has an associated merged PR
   - Check it's not the current working branch
   - Confirm with user before deletion

3. **Delete Merged Local Branches**
   ```bash
   git branch -d <branch-name>  # Use -d (safe delete, only if merged)
   ```

4. **Delete Merged Remote Branches**
   ```bash
   git push origin --delete <branch-name>
   ```

5. **Prune Remote References**
   ```bash
   git remote prune origin
   ```

### Phase 4: Repository Organization Check

1. **File Structure Audit**
   - Count files in each major directory (Root, MEZAN, TalAI, optilibria, qmlab, SimCore)
   - Identify any session documents (files like `*SUMMARY.md`, `*REPORT.md`, `SESSION*.md`)
   - Check for duplicate documentation
   - Verify archive structure exists: `.archive/sessions/`

2. **Documentation Organization**
   - Ensure all projects have essential docs only (README, LICENSE, CONTRIBUTING, etc.)
   - Verify technical docs are in proper locations (e.g., `docs/` subdirectories)
   - Check Claude configs are in `.claude/` directories
   - Identify any orphaned or misplaced files

3. **If Cleanup Needed**
   - Run the cleanup script if it exists: `./scripts/master_cleanup.sh --dry-run`
   - Review the dry-run output
   - Execute cleanup: `./scripts/master_cleanup.sh --execute`
   - Commit and push changes

### Phase 5: Final Verification

1. **Repository Health Check**
   - Verify all tests pass: `make test` (or project-specific test commands)
   - Run linters: `make lint`
   - Check pre-commit hooks are working
   - Verify no broken symlinks or missing files

2. **Documentation Status**
   - Confirm README.md files are current
   - Verify CLAUDE.md has accurate information
   - Check that all major changes are documented in CHANGELOGs

3. **Git State**
   - Verify main branch is clean and synced
   - Confirm no stale branches remain
   - Check that all work is properly committed and pushed

### Phase 6: Summary Report

Provide a comprehensive summary including:

1. **Current State**
   - Active branch and status
   - Latest commit on main
   - MEZAN version confirmed

2. **Actions Taken**
   - Branches deleted (if any)
   - Files reorganized (if any)
   - Sync operations performed

3. **Branch Status**
   - Total branches (local + remote)
   - Active/working branches
   - Branches recommended for deletion (if any need user approval)

4. **Health Metrics**
   - File counts by project
   - Test status
   - Lint status
   - Overall repository health score

5. **Recommendations**
   - Any maintenance tasks needed
   - Suggested next steps
   - Potential issues to address

---

## Safety Rules

**DO:**
- ✅ Always use `git branch -d` (lowercase) for safe deletion (only deletes if merged)
- ✅ Verify branches are merged before deletion
- ✅ Create backups of important branches before deletion
- ✅ Use `--dry-run` modes when available
- ✅ Confirm remote sync before any destructive operations

**DON'T:**
- ❌ Never use `git branch -D` (force delete) without explicit approval
- ❌ Never delete branches that are not fully merged
- ❌ Never delete main, master, or current branch
- ❌ Never push --force to main/master
- ❌ Never delete remote branches without verifying they're merged

## Expected Outcome

After running this prompt, you should have:
- ✅ Clean, organized repository structure
- ✅ All branches synced with remote
- ✅ Only active/necessary branches remaining
- ✅ All session documents properly archived
- ✅ Comprehensive understanding of repository state
- ✅ Clear action items for any remaining issues

## PROMPT END

---

## Usage Instructions

1. Copy everything between "PROMPT START" and "PROMPT END"
2. Paste into Claude Code
3. Claude will execute all phases systematically
4. Review the summary report
5. Approve any branch deletions if needed

## When to Use This Prompt

- After completing major features or milestones
- Weekly/monthly repository maintenance
- Before starting new major work
- After merging multiple PRs
- When repository feels cluttered or disorganized
- When unsure about branch status
