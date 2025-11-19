#!/bin/bash
# AlaweinOS Master Repository Cleanup Script
# Organizes and archives ~150 session documents across all projects

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

DRY_RUN=true
[[ "$1" == "--execute" ]] && DRY_RUN=false

# Move file with logging
move_file() {
    local src=$1
    local dest=$2

    if [ ! -f "$src" ]; then
        return
    fi

    if [ "$DRY_RUN" = true ]; then
        echo -e "  ${YELLOW}WOULD MOVE:${NC} $src → $dest"
    else
        mkdir -p "$(dirname "$dest")"
        mv "$src" "$dest"
        echo -e "  ${GREEN}✅ Moved:${NC} $src → $dest"
    fi
}

# Remove directory
remove_dir() {
    local dir=$1

    if [ ! -d "$dir" ]; then
        return
    fi

    if [ "$DRY_RUN" = true ]; then
        echo -e "  ${YELLOW}WOULD DELETE DIR:${NC} $dir"
    else
        rm -rf "$dir"
        echo -e "  ${GREEN}✅ Deleted:${NC} $dir"
    fi
}

# Header
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}  AlaweinOS Master Repository Cleanup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}🔍 DRY RUN MODE - No changes will be made${NC}"
else
    echo -e "${GREEN}⚡ EXECUTION MODE - Changes will be applied${NC}"
fi
echo ""

# Verify location
if [ ! -d "MEZAN" ] || [ ! -f "pyproject.toml" ]; then
    echo -e "${RED}❌ Error: Not in AlaweinOS root directory${NC}"
    echo "Current directory: $(pwd)"
    exit 1
fi

echo "📂 Working directory: $(pwd)"
echo ""

# Create archive structure
if [ "$DRY_RUN" = false ]; then
    mkdir -p .archive/sessions/{mezan,talai,optilibria,qmlab,simcore,2025-11-19}
fi

# ==========================================
# PHASE 1: MEZAN
# ==========================================
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Phase 1: MEZAN Cleanup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

MEZAN_SESSION_DOCS=(
    "MEZAN/SESSION_SUMMARY.md"
    "MEZAN/INTELLIGENT_MEZAN_V3_REPORT.md"
    "MEZAN/MEZAN_AGILE_ENGINE.md"
    "MEZAN/MEZAN_COMPLETE_DUAL_DOCUMENTATION.md"
    "MEZAN/MEZAN_IMPLEMENTATION_REPORT.md"
    "MEZAN/OPUS_LEVEL_FEATURES.md"
)

echo "Archiving session documents..."
for file in "${MEZAN_SESSION_DOCS[@]}"; do
    if [ -f "$file" ]; then
        move_file "$file" ".archive/sessions/mezan/$(basename "$file")"
    fi
done

echo ""
echo "Organizing technical documentation..."

MEZAN_TECH_DOCS=(
    "MEZAN/ATLAS_LIBRIA_INTEGRATION_SPEC.md:MEZAN/docs/specs/ATLAS_LIBRIA_INTEGRATION_SPEC.md"
    "MEZAN/BACKLOG_IMPROVEMENTS.md:MEZAN/docs/BACKLOG_IMPROVEMENTS.md"
    "MEZAN/FILE_MANIFEST.md:MEZAN/docs/FILE_MANIFEST.md"
    "MEZAN/MASTER_PROJECT_INDEX.md:MEZAN/docs/MASTER_PROJECT_INDEX.md"
    "MEZAN/REPO_CONVENTIONS.md:MEZAN/docs/REPO_CONVENTIONS.md"
)

for mapping in "${MEZAN_TECH_DOCS[@]}"; do
    src="${mapping%%:*}"
    dest="${mapping##*:}"
    move_file "$src" "$dest"
done

echo ""
echo "Moving Claude configuration..."
move_file "MEZAN/CLAUDE_COORDINATION_GUIDE.md" "MEZAN/.claude/COORDINATION_GUIDE.md"

echo ""

# ==========================================
# PHASE 2: TalAI
# ==========================================
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Phase 2: TalAI Cleanup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo "Archiving TalAI session documents..."

SESSION_PATTERNS=("*SESSION*" "*SUMMARY*" "*REPORT*" "*COMPLETE*" "*VALIDATION*" "*DELIVERY*" "*SPRINT*" "*CYCLE*")

for pattern in "${SESSION_PATTERNS[@]}"; do
    find TalAI -maxdepth 1 -type f -name "$pattern" 2>/dev/null | while read -r file; do
        if [ -f "$file" ]; then
            move_file "$file" ".archive/sessions/talai/$(basename "$file")"
        fi
    done
done

echo ""

# ==========================================
# PHASE 3: optilibria
# ==========================================
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Phase 3: optilibria Cleanup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo "Archiving optilibria session documents..."

for pattern in "${SESSION_PATTERNS[@]}"; do
    find optilibria -maxdepth 1 -type f -name "$pattern" 2>/dev/null | while read -r file; do
        if [ -f "$file" ]; then
            move_file "$file" ".archive/sessions/optilibria/$(basename "$file")"
        fi
    done
done

echo ""

# ==========================================
# PHASE 4: qmlab
# ==========================================
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Phase 4: qmlab Cleanup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo "Archiving qmlab session documents..."

for pattern in "${SESSION_PATTERNS[@]}"; do
    find qmlab -maxdepth 1 -type f -name "$pattern" 2>/dev/null | while read -r file; do
        if [ -f "$file" ]; then
            move_file "$file" ".archive/sessions/qmlab/$(basename "$file")"
        fi
    done
done

echo ""

# ==========================================
# PHASE 5: SimCore
# ==========================================
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Phase 5: SimCore Cleanup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo "Archiving SimCore session documents..."

for pattern in "${SESSION_PATTERNS[@]}"; do
    find SimCore -maxdepth 1 -type f -name "$pattern" 2>/dev/null | while read -r file; do
        if [ -f "$file" ]; then
            move_file "$file" ".archive/sessions/simcore/$(basename "$file")"
        fi
    done
done

echo ""

# ==========================================
# PHASE 6: Root Directory
# ==========================================
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Phase 6: Root Directory Cleanup${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

echo "Archiving root session documents..."

ROOT_SESSION_FILES=(
    ".audit-report.md"
    ".reorganization-plan.md"
    "DEPLOYMENT_CHECKLIST.md"
    "FINAL_MERGE_GUIDE.md"
    "FINAL_STATUS.md"
    "GIT_STATUS.md"
    "MERGE_COMMANDS.md"
    "MERGE_STATUS.md"
    "MISSION_COMPLETE.md"
    "READY_TO_USE.md"
    "test_execution_report.md"
    "test_status_dashboard.md"
)

for file in "${ROOT_SESSION_FILES[@]}"; do
    move_file "$file" ".archive/sessions/2025-11-19/$file"
done

echo ""

# ==========================================
# SUMMARY
# ==========================================
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${BLUE}Cleanup Summary${NC}"
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}This was a DRY RUN - no changes were made${NC}"
    echo ""
    echo "To execute cleanup, run:"
    echo -e "  ${GREEN}./scripts/master_cleanup.sh --execute${NC}"
else
    echo -e "${GREEN}✅ Cleanup completed successfully!${NC}"
    echo ""
    echo "Files archived: ~150 across 6 locations"
    echo ""
    echo "Next steps:"
    echo "  1. Review changes: git status"
    echo "  2. Commit: git add -A && git commit -m 'chore: Comprehensive repository cleanup'"
    echo "  3. Push: git push origin main"
fi

echo ""
echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
