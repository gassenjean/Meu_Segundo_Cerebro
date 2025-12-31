#!/bin/bash

# quick_backup.sh - Quick backup with timestamp
# Usage: ./quick_backup.sh [message]

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if in git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}ERROR: Not in a git repository${NC}"
    exit 1
fi

echo "==================================="
echo "  Quick Backup"
echo "==================================="
echo ""

# Get timestamp
TIMESTAMP=$(date +"%d%b%Y_%H%M")
MESSAGE="${1:-emergency snapshot}"

echo "📦 Creating backup..."
echo "   Time: $(date '+%Y-%m-%d %H:%M:%S')"
echo "   Message: $MESSAGE"
echo ""

# Check for uncommitted changes
uncommitted=$(git status --porcelain | wc -l)
if [ "$uncommitted" -eq 0 ]; then
    echo -e "${YELLOW}⚠ No changes to backup${NC}"
    echo ""
    echo "Current status:"
    git status --short
    exit 0
fi

echo "📝 Files to backup:"
git status --short | head -n 20
if [ "$uncommitted" -gt 20 ]; then
    echo "   ... and $((uncommitted - 20)) more files"
fi
echo ""

# Stage all changes
echo "🔄 Staging changes..."
git add . 2>&1 || {
    echo -e "${RED}ERROR: Failed to stage changes${NC}"
    exit 1
}
echo -e "${GREEN}✓ Staged successfully${NC}"
echo ""

# Create commit
echo "💾 Creating commit..."
git commit -m "backup: $MESSAGE $TIMESTAMP

Quick backup created at $TIMESTAMP.

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>" 2>&1 || {
    echo -e "${RED}ERROR: Failed to create commit${NC}"
    exit 1
}
echo -e "${GREEN}✓ Commit created${NC}"
echo ""

# Push to remote
echo "🚀 Pushing to GitHub..."
if git push origin master 2>&1; then
    echo -e "${GREEN}✓ Pushed successfully${NC}"
else
    echo -e "${RED}ERROR: Push failed${NC}"
    echo "   Commit saved locally but not pushed to remote"
    echo "   Try: git push origin master"
    exit 1
fi
echo ""

# Show result
echo "==================================="
echo -e "  ${GREEN}✓ Backup Complete!${NC}"
echo "==================================="
echo ""
echo "📊 Backup Info:"
echo "   Commit: $(git rev-parse --short HEAD)"
echo "   Files: $uncommitted changed"
echo "   Remote: $(git remote get-url origin)"
echo ""
echo "To restore this backup:"
echo "   git reset --hard $(git rev-parse --short HEAD)"
