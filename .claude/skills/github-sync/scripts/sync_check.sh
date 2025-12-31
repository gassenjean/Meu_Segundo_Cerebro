#!/bin/bash

# sync_check.sh - Check synchronization status with GitHub
# Usage: ./sync_check.sh

set -e

echo "==================================="
echo "  GitHub Sync Status Check"
echo "==================================="
echo ""

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

# 1. Repository Info
echo "📁 Repository Information:"
echo "   Remote: $(git remote get-url origin 2>/dev/null || echo 'No remote configured')"
echo "   Branch: $(git branch --show-current)"
echo ""

# 2. Local Status
echo "📝 Local Status:"
uncommitted=$(git status --porcelain | wc -l)
if [ "$uncommitted" -eq 0 ]; then
    echo -e "   ${GREEN}✓ Working directory clean${NC}"
else
    echo -e "   ${YELLOW}⚠ $uncommitted uncommitted changes${NC}"
    echo ""
    echo "   Modified files:"
    git status --short | head -n 10
    if [ "$uncommitted" -gt 10 ]; then
        echo "   ... and $((uncommitted - 10)) more"
    fi
fi
echo ""

# 3. Remote Status
echo "🌐 Remote Status:"
git fetch origin --quiet 2>/dev/null || echo "   Warning: Could not fetch from remote"

LOCAL=$(git rev-parse @ 2>/dev/null)
REMOTE=$(git rev-parse @{u} 2>/dev/null || echo "no-remote")
BASE=$(git merge-base @ @{u} 2>/dev/null || echo "no-base")

if [ "$REMOTE" = "no-remote" ]; then
    echo -e "   ${YELLOW}⚠ No remote tracking branch${NC}"
elif [ "$LOCAL" = "$REMOTE" ]; then
    echo -e "   ${GREEN}✓ Up to date with origin${NC}"
elif [ "$LOCAL" = "$BASE" ]; then
    echo -e "   ${YELLOW}⚠ Need to pull${NC}"
    commits_behind=$(git rev-list HEAD..@{u} --count 2>/dev/null || echo "?")
    echo "   Behind by: $commits_behind commits"
elif [ "$REMOTE" = "$BASE" ]; then
    echo -e "   ${YELLOW}⚠ Need to push${NC}"
    commits_ahead=$(git rev-list @{u}..HEAD --count 2>/dev/null || echo "?")
    echo "   Ahead by: $commits_ahead commits"
else
    echo -e "   ${RED}⚠ Diverged from origin${NC}"
    echo "   Need to pull and merge"
fi
echo ""

# 4. Recent Commits
echo "📜 Recent Commits (local):"
git log --oneline -5 --pretty=format:"   %C(yellow)%h%C(reset) - %s %C(green)(%cr)%C(reset)" 2>/dev/null
echo ""
echo ""

# 5. Stashes
stash_count=$(git stash list | wc -l)
if [ "$stash_count" -gt 0 ]; then
    echo "💾 Stashes:"
    echo -e "   ${YELLOW}$stash_count stashed changes${NC}"
    git stash list | head -n 3 | sed 's/^/   /'
    echo ""
fi

# 6. Sync Logs Check
echo "📋 Sync Logs:"
if [ -f "SESSION_LOG.md" ]; then
    echo -e "   ${GREEN}✓ SESSION_LOG.md exists${NC}"
    last_update=$(stat -c %y "SESSION_LOG.md" 2>/dev/null | cut -d' ' -f1 || echo "unknown")
    echo "   Last updated: $last_update"
else
    echo -e "   ${YELLOW}⚠ SESSION_LOG.md not found${NC}"
fi

if [ -f "PC_SYNC_LOG.md" ]; then
    echo -e "   ${GREEN}✓ PC_SYNC_LOG.md exists${NC}"
    last_update=$(stat -c %y "PC_SYNC_LOG.md" 2>/dev/null | cut -d' ' -f1 || echo "unknown")
    echo "   Last updated: $last_update"
else
    echo -e "   ${YELLOW}⚠ PC_SYNC_LOG.md not found${NC}"
fi
echo ""

# 7. Recommendations
echo "💡 Recommendations:"
if [ "$uncommitted" -gt 0 ]; then
    echo "   1. Review and commit changes: git add . && git commit"
fi
if [ "$REMOTE" != "no-remote" ] && [ "$LOCAL" != "$REMOTE" ]; then
    if [ "$LOCAL" = "$BASE" ]; then
        echo "   2. Pull latest changes: git pull --rebase origin master"
    elif [ "$REMOTE" = "$BASE" ]; then
        echo "   2. Push your changes: git push origin master"
    else
        echo "   2. Sync with remote: git pull --rebase && git push"
    fi
fi
if [ "$uncommitted" -eq 0 ] && [ "$LOCAL" = "$REMOTE" ]; then
    echo -e "   ${GREEN}✓ Everything is in sync!${NC}"
fi
echo ""

echo "==================================="
echo "  Sync check complete!"
echo "==================================="
