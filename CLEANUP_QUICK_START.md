# Repository Cleanup - Quick Start Guide

**Ready to clean up the repository? Follow these simple steps!**

---

## 🚀 Option 1: Automatic Cleanup (Recommended)

**Time:** 2 minutes
**Difficulty:** Easy

### Step 1: Preview Changes

```bash
./scripts/master_cleanup.sh --dry-run
```

This shows you exactly what will be moved without making any changes.

### Step 2: Execute Cleanup

```bash
./scripts/master_cleanup.sh --execute
```

### Step 3: Commit & Push

```bash
git add -A
git commit -m "chore: Comprehensive repository cleanup - organize 150+ files"
git push origin main
```

**Done!** Your repository is now clean and organized.

---

## 📋 Option 2: Manual Cleanup (Step by Step)

If you prefer to clean projects one at a time:

### Clean MEZAN (5 min)
```bash
# Archive session docs
mkdir -p .archive/sessions/mezan
mv MEZAN/SESSION_SUMMARY.md .archive/sessions/mezan/ 2>/dev/null
mv MEZAN/INTELLIGENT_MEZAN_V3_REPORT.md .archive/sessions/mezan/ 2>/dev/null
mv MEZAN/MEZAN_AGILE_ENGINE.md .archive/sessions/mezan/ 2>/dev/null
mv MEZAN/MEZAN_COMPLETE_DUAL_DOCUMENTATION.md .archive/sessions/mezan/ 2>/dev/null
mv MEZAN/MEZAN_IMPLEMENTATION_REPORT.md .archive/sessions/mezan/ 2>/dev/null
mv MEZAN/OPUS_LEVEL_FEATURES.md .archive/sessions/mezan/ 2>/dev/null

# Organize docs
mkdir -p MEZAN/docs/specs MEZAN/.claude
mv MEZAN/ATLAS_LIBRIA_INTEGRATION_SPEC.md MEZAN/docs/specs/ 2>/dev/null
mv MEZAN/BACKLOG_IMPROVEMENTS.md MEZAN/docs/ 2>/dev/null
mv MEZAN/FILE_MANIFEST.md MEZAN/docs/ 2>/dev/null
mv MEZAN/MASTER_PROJECT_INDEX.md MEZAN/docs/ 2>/dev/null
mv MEZAN/REPO_CONVENTIONS.md MEZAN/docs/ 2>/dev/null
mv MEZAN/CLAUDE_COORDINATION_GUIDE.md MEZAN/.claude/ 2>/dev/null

git add MEZAN .archive
git commit -m "chore: Clean up MEZAN directory"
```

### Clean Root (2 min)
```bash
mkdir -p .archive/sessions/2025-11-19

# Archive session docs
mv .audit-report.md .archive/sessions/2025-11-19/ 2>/dev/null
mv .reorganization-plan.md .archive/sessions/2025-11-19/ 2>/dev/null
mv DEPLOYMENT_CHECKLIST.md .archive/sessions/2025-11-19/ 2>/dev/null
mv FINAL_MERGE_GUIDE.md .archive/sessions/2025-11-19/ 2>/dev/null
mv FINAL_STATUS.md .archive/sessions/2025-11-19/ 2>/dev/null
mv GIT_STATUS.md .archive/sessions/2025-11-19/ 2>/dev/null
mv MERGE_COMMANDS.md .archive/sessions/2025-11-19/ 2>/dev/null
mv MERGE_STATUS.md .archive/sessions/2025-11-19/ 2>/dev/null
mv MISSION_COMPLETE.md .archive/sessions/2025-11-19/ 2>/dev/null
mv READY_TO_USE.md .archive/sessions/2025-11-19/ 2>/dev/null
mv test_execution_report.md .archive/sessions/2025-11-19/ 2>/dev/null
mv test_status_dashboard.md .archive/sessions/2025-11-19/ 2>/dev/null

git add . archive
git commit -m "chore: Clean up root directory"
```

### Clean Other Projects (Optional)
```bash
# TalAI
find TalAI -maxdepth 1 -name "*SUMMARY*" -o -name "*REPORT*" | xargs -I {} mv {} .archive/sessions/talai/

# optilibria
find optilibria -maxdepth 1 -name "*SUMMARY*" -o -name "*REPORT*" | xargs -I {} mv {} .archive/sessions/optilibria/

# qmlab
find qmlab -maxdepth 1 -name "*SUMMARY*" -o -name "*REPORT*" | xargs -I {} mv {} .archive/sessions/qmlab/

# SimCore
find SimCore -maxdepth 1 -name "*SUMMARY*" -o -name "*REPORT*" | xargs -I {} mv {} .archive/sessions/simcore/

git add .archive TalAI optilibria qmlab SimCore
git commit -m "chore: Clean up all project directories"
```

---

## 📊 What Gets Cleaned?

### Files Being Archived (~150 total)

**MEZAN (12 files):**
- 6 session documents → `.archive/sessions/mezan/`
- 5 technical docs → `MEZAN/docs/`
- 1 config → `MEZAN/.claude/`

**TalAI (~30 files):**
- All `*SUMMARY*.md`, `*REPORT*.md` → `.archive/sessions/talai/`

**optilibria (~20 files):**
- All session docs → `.archive/sessions/optilibria/`

**qmlab (~10 files):**
- All session docs → `.archive/sessions/qmlab/`

**SimCore (~10 files):**
- All session docs → `.archive/sessions/simcore/`

**Root (12 files):**
- All session docs → `.archive/sessions/2025-11-19/`

### Files Being Kept

**Essential files that stay in project roots:**
- README.md
- CLAUDE.md
- LICENSE
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- CHANGELOG.md (if exists)
- START_HERE.md (if exists)
- Configuration files (package.json, pyproject.toml, etc.)

---

## ✅ Verification

After cleanup, verify the results:

```bash
# Check file counts
echo "MEZAN: $(ls -la MEZAN/ | wc -l) items (should be ~15)"
echo "TalAI: $(ls -la TalAI/ | wc -l) items (should be ~30)"
echo "Root: $(ls -la | wc -l) items (should be ~25)"

# Check archive
echo "Archived: $(find .archive/sessions -type f | wc -l) files"

# View clean MEZAN directory
ls -la MEZAN/
```

**Expected Results:**
- MEZAN: 43 → ~15 items ✅
- TalAI: 111 → ~30 items ✅
- optilibria: 56 → ~20 items ✅
- qmlab: 54 → ~20 items ✅
- SimCore: 49 → ~18 items ✅
- Root: 40 → ~15 items ✅

---

## 🔄 Undo (If Needed)

If you need to undo the cleanup:

```bash
# Option 1: Before committing
git reset --hard HEAD

# Option 2: After committing
git revert HEAD

# Option 3: Restore specific files from archive
cp .archive/sessions/mezan/SESSION_SUMMARY.md MEZAN/
```

---

## 🛟 Troubleshooting

### Problem: Script not executable
```bash
chmod +x scripts/master_cleanup.sh
```

### Problem: Files not found
- Check you're in repository root: `pwd` should show `/home/user/AlaweinOS`
- Navigate to root: `cd /home/user/AlaweinOS`

### Problem: Permission denied
```bash
# Run with explicit bash
bash scripts/master_cleanup.sh --dry-run
```

### Problem: Want to skip a project
Edit `scripts/master_cleanup.sh` and comment out the phase you want to skip.

---

## 📞 Need Help?

- **Full Plan:** See `COMPREHENSIVE_CLEANUP_PLAN.md`
- **Analysis:** See `FINAL_CLEANUP_SUMMARY.md`
- **Questions:** Open GitHub issue or email meshal@berkeley.edu

---

## 🎉 After Cleanup

Your repository will be:
- ✅ 60% less cluttered
- ✅ Professionally organized
- ✅ Easy to navigate
- ✅ Ready for external contributors
- ✅ With full history preserved in `.archive/`

**Happy cleaning! 🧹**

---

**Quick Start Guide Version:** 1.0
**Last Updated:** 2025-11-19
