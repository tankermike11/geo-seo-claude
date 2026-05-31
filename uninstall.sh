#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Unified Uninstaller — GEO-SEO + AI Marketing Suite
# ============================================================

CLAUDE_DIR="${HOME}/.claude"
SKILLS_DIR="${CLAUDE_DIR}/skills"
AGENTS_DIR="${CLAUDE_DIR}/agents"

INTERACTIVE=true
if [ ! -t 0 ]; then
    INTERACTIVE=false
fi

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

shopt -s nullglob

echo ""
echo -e "${YELLOW}GEO-SEO + AI Marketing Suite — Uninstaller${NC}"
echo ""
echo "This will remove:"
echo ""

[ -d "$SKILLS_DIR/geo" ]    && echo "  → ${SKILLS_DIR}/geo/"
[ -d "$SKILLS_DIR/market" ] && echo "  → ${SKILLS_DIR}/market/"
for skill_dir in "$SKILLS_DIR"/geo-*/ "$SKILLS_DIR"/market-*/; do
    [ -d "$skill_dir" ] && echo "  → ${skill_dir}"
done
for agent_file in "$AGENTS_DIR"/geo-*.md "$AGENTS_DIR"/market-*.md; do
    [ -f "$agent_file" ] && echo "  → ${agent_file}"
done

echo ""
if [ "$INTERACTIVE" = true ]; then
    read -p "Are you sure you want to uninstall? (y/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Uninstall cancelled."
        exit 0
    fi
else
    echo -e "${YELLOW}Non-interactive mode — proceeding...${NC}"
fi

echo ""

# ---- GEO skills ----
if [ -d "$SKILLS_DIR/geo" ]; then
    rm -rf "$SKILLS_DIR/geo"
    echo -e "${GREEN}✓ Removed geo (main skill + venv)${NC}"
fi
for skill_dir in "$SKILLS_DIR"/geo-*/; do
    if [ -d "$skill_dir" ]; then
        rm -rf "$skill_dir"
        echo -e "${GREEN}✓ Removed $(basename "$skill_dir")${NC}"
    fi
done

# ---- Marketing skills ----
if [ -d "$SKILLS_DIR/market" ]; then
    rm -rf "$SKILLS_DIR/market"
    echo -e "${GREEN}✓ Removed market (main skill)${NC}"
fi
for skill_dir in "$SKILLS_DIR"/market-*/; do
    if [ -d "$skill_dir" ]; then
        rm -rf "$skill_dir"
        echo -e "${GREEN}✓ Removed $(basename "$skill_dir")${NC}"
    fi
done

# ---- Agents ----
for agent_file in "$AGENTS_DIR"/geo-*.md "$AGENTS_DIR"/market-*.md; do
    if [ -f "$agent_file" ]; then
        rm -f "$agent_file"
        echo -e "${GREEN}✓ Removed $(basename "$agent_file")${NC}"
    fi
done

echo ""
echo -e "${GREEN}GEO-SEO + AI Marketing Suite has been uninstalled.${NC}"
echo ""
echo "Note: Python dependencies lived in the isolated venv inside the geo skill"
echo "directory and were removed automatically. Your system Python is untouched."
echo ""
echo "Note: Prospect data at ~/.geo-prospects/ was NOT removed."
echo "  To remove it: rm -rf ~/.geo-prospects"
echo ""
