#!/bin/bash

# cleanup_old.sh - Clean up old files marked for deletion
# Usage: ./cleanup_old.sh [--dry-run]

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

DRY_RUN=false
if [ "$1" = "--dry-run" ] || [ "$1" = "-n" ]; then
    DRY_RUN=true
fi

echo "==================================="
echo "  Cleanup Old Files"
echo "==================================="
echo ""

if [ "$DRY_RUN" = true ]; then
    echo -e "${YELLOW}DRY RUN MODE - No changes will be made${NC}"
    echo ""
fi

# Find deleted files in git status
deleted_files=$(git status --porcelain | grep "^ D" | cut -c4- || echo "")

if [ -z "$deleted_files" ]; then
    echo -e "${GREEN}✓ No files marked for deletion${NC}"
    echo ""
    echo "Working directory is clean!"
    exit 0
fi

# Count files
count=$(echo "$deleted_files" | wc -l)
echo "📋 Found $count files marked for deletion:"
echo ""

# Show first 30 files
echo "$deleted_files" | head -n 30 | sed 's/^/   /'
if [ "$count" -gt 30 ]; then
    echo "   ... and $((count - 30)) more files"
fi
echo ""

# Calculate sizes (approximate)
echo "📊 Analyzing sizes..."
total_size=0
for file in $deleted_files; do
    if [ -f "$file" ]; then
        size=$(stat -c%s "$file" 2>/dev/null || echo "0")
        total_size=$((total_size + size))
    fi
done

# Convert to human readable
if [ "$total_size" -gt 1048576 ]; then
    size_display="$(echo "scale=2; $total_size / 1048576" | bc)MB"
elif [ "$total_size" -gt 1024 ]; then
    size_display="$(echo "scale=2; $total_size / 1024" | bc)KB"
else
    size_display="${total_size}B"
fi

echo "   Total size: $size_display"
echo ""

if [ "$DRY_RUN" = true ]; then
    echo "==================================="
    echo "  DRY RUN - Summary"
    echo "==================================="
    echo "   Files to delete: $count"
    echo "   Space to free: $size_display"
    echo ""
    echo "Run without --dry-run to actually delete files"
    exit 0
fi

# Confirm deletion
echo -e "${YELLOW}⚠ This will stage all deletions for commit${NC}"
echo ""
read -p "Continue? (y/N) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

echo ""
echo "🔄 Staging deletions..."

# Stage deletions
git add -u 2>&1 || {
    echo -e "${RED}ERROR: Failed to stage deletions${NC}"
    exit 1
}

echo -e "${GREEN}✓ Staged $count deletions${NC}"
echo ""

# Show what was staged
echo "📝 Staged for commit:"
git diff --cached --name-only --diff-filter=D | head -n 10 | sed 's/^/   /'
if [ "$count" -gt 10 ]; then
    echo "   ... and $((count - 10)) more"
fi
echo ""

# Offer to commit
echo -e "${YELLOW}Files are staged but not committed${NC}"
echo ""
read -p "Create commit now? (y/N) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "💾 Creating commit..."

    git commit -m "chore: clean old files

Removed $count deprecated files:
- Old reference materials
- Duplicate content
- Obsolete structure

Freed approximately $size_display.

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>" 2>&1 || {
        echo -e "${RED}ERROR: Failed to create commit${NC}"
        exit 1
    }

    echo -e "${GREEN}✓ Commit created${NC}"
    echo ""

    # Offer to push
    read -p "Push to GitHub? (y/N) " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        echo "🚀 Pushing to GitHub..."

        if git push origin master 2>&1; then
            echo -e "${GREEN}✓ Pushed successfully${NC}"
        else
            echo -e "${RED}ERROR: Push failed${NC}"
            echo "   Commit saved locally"
            echo "   Try: git push origin master"
        fi
    else
        echo ""
        echo "Commit saved locally."
        echo "Push later with: git push origin master"
    fi
else
    echo ""
    echo "Changes staged but not committed."
    echo "Commit later with: git commit"
fi

echo ""
echo "==================================="
echo -e "  ${GREEN}✓ Cleanup Complete!${NC}"
echo "==================================="
echo ""
echo "📊 Summary:"
echo "   Deleted: $count files"
echo "   Freed: $size_display"
