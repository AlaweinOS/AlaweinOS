#!/bin/bash
# SimCore Final Merge Script
# This script completes the merge to main

set -e

echo "🚀 SimCore Final Merge"
echo "======================="
echo ""

# Check we're in the right directory
if [ ! -d "SimCore" ]; then
    echo "❌ Error: SimCore directory not found"
    echo "   Please run from /home/user/AlaweinOS"
    exit 1
fi

echo "📍 Current location: $(pwd)"
echo "📍 Current branch: $(git branch --show-current)"
echo ""

# Fetch latest from remote
echo "📥 Fetching latest from remote..."
git fetch origin

# Check if PR branch exists on remote
if git ls-remote --exit-code --heads origin claude/simcore-final-merge-01UjRWvPCZQuMBwNkk9GUQ4n > /dev/null 2>&1; then
    echo "✅ PR branch found on remote"
else
    echo "❌ PR branch not found on remote"
    exit 1
fi

echo ""
echo "🔀 Merging PR branch to main..."
echo ""

# Switch to main
git checkout main

# Merge PR branch (fast-forward if possible)
git merge --ff origin/claude/simcore-final-merge-01UjRWvPCZQuMBwNkk9GUQ4n -m "Merge PR: SimCore comprehensive enhancement v3.0.0"

echo ""
echo "✅ Local merge complete!"
echo ""
echo "📊 Current status:"
git log --oneline -3
echo ""

# Try to push to main
echo "🚀 Attempting to push to origin/main..."
if git push origin main 2>&1 | tee /tmp/push_output.txt; then
    echo ""
    echo "✅ Successfully pushed to origin/main!"
    echo ""
    echo "🎉 MERGE COMPLETE!"
    echo ""
    echo "SimCore is now on main branch (local and remote)"
    echo ""
    echo "To start using:"
    echo "  cd SimCore"
    echo "  npm run dev"
    echo ""
else
    echo ""
    echo "⚠️  Push to origin/main blocked (branch protection)"
    echo ""
    echo "Your options:"
    echo ""
    echo "1. Merge via GitHub Web UI:"
    echo "   Visit: https://github.com/AlaweinOS/AlaweinOS/compare/main...claude/simcore-final-merge-01UjRWvPCZQuMBwNkk9GUQ4n"
    echo "   Click 'Create pull request' then 'Merge'"
    echo ""
    echo "2. Use locally (already works!):"
    echo "   cd SimCore"
    echo "   npm run dev"
    echo ""
    echo "All your work is safe on the PR branch!"
fi
