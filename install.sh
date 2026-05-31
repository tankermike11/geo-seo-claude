#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# Unified Installer — GEO-SEO + AI Marketing Suite
# ============================================================

REPO_URL="https://github.com/zubair-trabzada/geo-seo-claude.git"
CLAUDE_DIR="${HOME}/.claude"
SKILLS_DIR="${CLAUDE_DIR}/skills"
AGENTS_DIR="${CLAUDE_DIR}/agents"
GEO_INSTALL_DIR="${SKILLS_DIR}/geo"
VENV_DIR="${GEO_INSTALL_DIR}/.venv"
VENV_PY="${VENV_DIR}/bin/python3"
# shellcheck disable=SC2088
VENV_MD_PY='~/.claude/skills/geo/.venv/bin/python3'
TEMP_DIR=$(mktemp -d)

INTERACTIVE=true
if [ ! -t 0 ]; then
    INTERACTIVE=false
fi

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

print_header() {
    echo ""
    echo -e "${CYAN}╔══════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║   GEO-SEO + AI Marketing Suite — Installer       ║${NC}"
    echo -e "${CYAN}║   GEO · SEO · Copy · Emails · Social · PDF       ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════╝${NC}"
    echo ""
}

print_success() { echo -e "${GREEN}✓ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠ $1${NC}"; }
print_error()   { echo -e "${RED}✗ $1${NC}"; }
print_info()    { echo -e "${BLUE}→ $1${NC}"; }

cleanup() { rm -rf "$TEMP_DIR"; }
trap cleanup EXIT

sed_inplace() {
    local pattern="$1"
    local file="$2"
    sed -i.bak "$pattern" "$file" && rm -f "${file}.bak"
}

main() {
    print_header

    # ---- Prerequisites ----
    print_info "Checking prerequisites..."

    if ! command -v git &> /dev/null; then
        print_error "Git is required but not installed."
        echo "  Install: https://git-scm.com/downloads"
        exit 1
    fi
    print_success "Git found: $(git --version)"

    PYTHON_CMD=""
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PY_VERSION=$(python --version 2>&1 | grep -oE '[0-9]+\.[0-9]+' | head -1)
        if [ -n "$PY_VERSION" ]; then
            MAJOR=$(echo "$PY_VERSION" | cut -d. -f1)
            MINOR=$(echo "$PY_VERSION" | cut -d. -f2)
            if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 8 ]; then
                PYTHON_CMD="python"
            fi
        fi
    fi

    if [ -z "$PYTHON_CMD" ]; then
        print_error "Python 3.8+ is required but not found."
        echo "  Install: https://www.python.org/downloads/"
        exit 1
    fi
    print_success "Python found: $($PYTHON_CMD --version)"

    if ! command -v claude &> /dev/null; then
        print_warning "Claude Code CLI not found in PATH."
        echo "  Install: npm install -g @anthropic-ai/claude-code"
        echo ""
        if [ "$INTERACTIVE" = true ]; then
            read -p "Continue installation anyway? (y/n): " -n 1 -r
            echo ""
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then exit 1; fi
        else
            print_info "Non-interactive mode — continuing anyway..."
        fi
    else
        print_success "Claude Code CLI found"
    fi

    USE_UV=false
    if command -v uv &> /dev/null; then
        USE_UV=true
        print_success "'uv' detected — will use it for a faster install"
    fi

    # ---- Resolve source ----
    SCRIPT_DIR=""
    if [ -n "${BASH_SOURCE[0]:-}" ] && [ "${BASH_SOURCE[0]}" != "bash" ]; then
        SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)" || true
    fi

    if [ -n "$SCRIPT_DIR" ] && [ -f "$SCRIPT_DIR/geo/SKILL.md" ]; then
        print_info "Installing from local directory: $SCRIPT_DIR"
        SOURCE_DIR="$SCRIPT_DIR"
    else
        print_info "Cloning from repository..."
        git clone --depth 1 "$REPO_URL" "$TEMP_DIR/repo" || {
            print_error "Failed to clone repository."
            exit 1
        }
        SOURCE_DIR="${TEMP_DIR}/repo"
    fi

    # ---- Directories ----
    print_info "Creating directories..."
    mkdir -p "$SKILLS_DIR" "$AGENTS_DIR" "$GEO_INSTALL_DIR"
    mkdir -p "$GEO_INSTALL_DIR/scripts" "$GEO_INSTALL_DIR/schema" "$GEO_INSTALL_DIR/hooks"
    print_success "Directory structure created"

    # ================================================================
    # GEO-SEO SUITE
    # ================================================================
    echo ""
    echo -e "${BLUE}━━━ Installing GEO-SEO Suite ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    print_info "Installing main GEO skill..."
    cp -r "$SOURCE_DIR/geo/"* "$GEO_INSTALL_DIR/"
    print_success "Main skill → ${GEO_INSTALL_DIR}/"

    print_info "Installing GEO sub-skills..."
    GEO_SKILL_COUNT=0
    for skill_dir in "$SOURCE_DIR/skills"/geo-*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            target_dir="${SKILLS_DIR}/${skill_name}"
            mkdir -p "$target_dir"
            cp -r "$skill_dir"* "$target_dir/"
            GEO_SKILL_COUNT=$((GEO_SKILL_COUNT + 1))
            print_success "  ${skill_name}"
        fi
    done
    echo "  → ${GEO_SKILL_COUNT} GEO sub-skills installed"

    print_info "Installing GEO subagents..."
    GEO_AGENT_COUNT=0
    for agent_file in "$SOURCE_DIR/agents/"geo-*.md; do
        if [ -f "$agent_file" ]; then
            cp "$agent_file" "$AGENTS_DIR/"
            GEO_AGENT_COUNT=$((GEO_AGENT_COUNT + 1))
            print_success "  $(basename "$agent_file")"
        fi
    done
    echo "  → ${GEO_AGENT_COUNT} GEO subagents installed"

    if [ -d "$SOURCE_DIR/scripts" ]; then
        print_info "Installing GEO scripts..."
        cp -r "$SOURCE_DIR/scripts/"* "$GEO_INSTALL_DIR/scripts/"
        print_success "GEO scripts → ${GEO_INSTALL_DIR}/scripts/"
    fi

    if [ -d "$SOURCE_DIR/schema" ]; then
        print_info "Installing GEO schema templates..."
        cp -r "$SOURCE_DIR/schema/"* "$GEO_INSTALL_DIR/schema/"
        print_success "Schema templates → ${GEO_INSTALL_DIR}/schema/"
    fi

    if [ -d "$SOURCE_DIR/hooks" ] && [ "$(ls -A "$SOURCE_DIR/hooks" 2>/dev/null)" ]; then
        print_info "Installing GEO hooks..."
        cp -r "$SOURCE_DIR/hooks/"* "$GEO_INSTALL_DIR/hooks/"
        chmod +x "$GEO_INSTALL_DIR/hooks/"* 2>/dev/null || true
        print_success "Hooks → ${GEO_INSTALL_DIR}/hooks/"
    fi

    # ---- GEO venv ----
    print_info "Creating isolated Python environment → ${VENV_DIR}"
    rm -rf "$VENV_DIR"

    if [ "$USE_UV" = true ]; then
        uv venv "$VENV_DIR" --python "$PYTHON_CMD" --quiet || { print_error "uv venv failed."; exit 1; }
    else
        if ! $PYTHON_CMD -m venv "$VENV_DIR" 2>/dev/null; then
            print_error "Failed to create virtual environment."
            echo "  Debian/Ubuntu: sudo apt install python3-venv"
            echo "  Or install uv: https://docs.astral.sh/uv/"
            exit 1
        fi
    fi
    print_success "Virtual environment created"

    print_info "Installing Python dependencies..."
    if [ ! -f "$SOURCE_DIR/requirements.txt" ]; then
        print_warning "requirements.txt missing — skipping."
    elif [ "$USE_UV" = true ]; then
        uv pip install --python "$VENV_PY" -r "$SOURCE_DIR/requirements.txt" --quiet || { print_error "Dependency install failed."; exit 1; }
    else
        "$VENV_PY" -m pip install --upgrade pip --quiet
        "$VENV_PY" -m pip install -r "$SOURCE_DIR/requirements.txt" --quiet || { print_error "Dependency install failed."; exit 1; }
    fi
    print_success "Dependencies installed (isolated venv — system Python untouched)"
    cp "$SOURCE_DIR/requirements.txt" "$GEO_INSTALL_DIR/" 2>/dev/null || true

    print_info "Pinning script shebangs to venv interpreter..."
    SHEBANG_COUNT=0
    for f in "$GEO_INSTALL_DIR/scripts/"*.py; do
        [ -f "$f" ] || continue
        sed_inplace "1s|^#!.*|#!${VENV_PY}|" "$f"
        chmod +x "$f"
        SHEBANG_COUNT=$((SHEBANG_COUNT + 1))
    done
    print_success "${SHEBANG_COUNT} script(s) pinned to venv"

    print_info "Rewriting skill & agent references to use the venv..."
    patch_md() {
        local f="$1"
        sed_inplace 's|python3 ~/\.claude/skills/geo/scripts/|~/.claude/skills/geo/scripts/|g' "$f"
        sed_inplace "s|python3 -c |${VENV_MD_PY} -c |g" "$f"
        sed_inplace "s|python3 -m |${VENV_MD_PY} -m |g" "$f"
    }
    PATCH_COUNT=0
    for f in "$GEO_INSTALL_DIR/SKILL.md" "$SKILLS_DIR"/geo-*/SKILL.md "$AGENTS_DIR"/geo-*.md; do
        if [ -f "$f" ]; then
            patch_md "$f"
            PATCH_COUNT=$((PATCH_COUNT + 1))
        fi
    done
    print_success "${PATCH_COUNT} markdown file(s) rewritten"

    # ================================================================
    # AI MARKETING SUITE
    # ================================================================
    echo ""
    echo -e "${BLUE}━━━ Installing AI Marketing Suite ━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

    MARKET_INSTALL_DIR="${SKILLS_DIR}/market"
    mkdir -p "$MARKET_INSTALL_DIR/scripts" "$MARKET_INSTALL_DIR/templates"

    if [ -f "$SOURCE_DIR/market/SKILL.md" ]; then
        cp "$SOURCE_DIR/market/SKILL.md" "$MARKET_INSTALL_DIR/SKILL.md"
        print_success "Main market skill installed"
    else
        print_warning "market/SKILL.md not found — skipping"
    fi

    print_info "Installing marketing sub-skills..."
    MARKET_SKILL_COUNT=0
    for skill_dir in "$SOURCE_DIR/skills"/market-*/; do
        if [ -d "$skill_dir" ]; then
            skill_name=$(basename "$skill_dir")
            target_dir="${SKILLS_DIR}/${skill_name}"
            mkdir -p "$target_dir"
            cp -r "$skill_dir"* "$target_dir/"
            MARKET_SKILL_COUNT=$((MARKET_SKILL_COUNT + 1))
            print_success "  ${skill_name}"
        fi
    done
    echo "  → ${MARKET_SKILL_COUNT} marketing sub-skills installed"

    print_info "Installing marketing subagents..."
    MARKET_AGENT_COUNT=0
    for agent_file in "$SOURCE_DIR/agents/"market-*.md; do
        if [ -f "$agent_file" ]; then
            cp "$agent_file" "$AGENTS_DIR/"
            MARKET_AGENT_COUNT=$((MARKET_AGENT_COUNT + 1))
            print_success "  $(basename "$agent_file")"
        fi
    done
    echo "  → ${MARKET_AGENT_COUNT} marketing subagents installed"

    if [ -d "$SOURCE_DIR/market/scripts" ]; then
        print_info "Installing marketing scripts..."
        cp -r "$SOURCE_DIR/market/scripts/"* "$MARKET_INSTALL_DIR/scripts/"
        chmod +x "$MARKET_INSTALL_DIR/scripts/"*.py 2>/dev/null || true
        print_success "Marketing scripts → ${MARKET_INSTALL_DIR}/scripts/"
    fi

    if [ -d "$SOURCE_DIR/market/templates" ]; then
        print_info "Installing marketing templates..."
        cp -r "$SOURCE_DIR/market/templates/"* "$MARKET_INSTALL_DIR/templates/"
        print_success "Templates → ${MARKET_INSTALL_DIR}/templates/"
    fi

    # Check reportlab for PDF reports
    if "$VENV_PY" -c "import reportlab" 2>/dev/null; then
        print_success "reportlab available — PDF reports ready"
    else
        print_warning "reportlab not installed — PDF reports will be unavailable"
        echo "  Install: ${VENV_PY} -m pip install reportlab"
    fi

    # ================================================================
    # OPTIONAL: Playwright
    # ================================================================
    if [ "$INTERACTIVE" = true ]; then
        echo ""
        read -p "Install Playwright browsers for screenshots? (y/n): " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            print_info "Installing Playwright Chromium into venv..."
            if "$VENV_PY" -m playwright install chromium 2>/dev/null; then
                print_success "Playwright Chromium installed"
            else
                print_warning "Playwright install failed — screenshots unavailable."
                echo "  Retry: ${VENV_PY} -m playwright install chromium"
            fi
        fi
    else
        print_info "Skipping Playwright (non-interactive). Run later:"
        echo "    ${VENV_PY} -m playwright install chromium"
    fi

    # ================================================================
    # VERIFY
    # ================================================================
    echo ""
    print_info "Verifying installation..."
    VERIFY_OK=true
    verify() {
        local label="$1"; shift
        if "$@"; then print_success "$label"
        else print_error "$label missing"; VERIFY_OK=false; fi
    }

    agent_count=0
    for f in "$AGENTS_DIR"/geo-*.md "$AGENTS_DIR"/market-*.md; do
        [ -f "$f" ] && agent_count=$((agent_count + 1))
    done

    verify "GEO main skill"           test -f "$GEO_INSTALL_DIR/SKILL.md"
    verify "GEO sub-skills"           test -d "${SKILLS_DIR}/geo-audit"
    verify "Marketing main skill"     test -f "$MARKET_INSTALL_DIR/SKILL.md"
    verify "Marketing sub-skills"     test -d "${SKILLS_DIR}/market-audit"
    verify "Subagents"                test "$agent_count" -gt 0
    verify "Venv interpreter"         test -x "$VENV_PY"

    [ "$VERIFY_OK" = false ] && print_warning "One or more files are missing. Install may be incomplete."

    # ================================================================
    # SUMMARY
    # ================================================================
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║           Installation Complete!                  ║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════╝${NC}"
    echo ""
    echo "  GEO skills:        ${GEO_SKILL_COUNT}"
    echo "  Marketing skills:  ${MARKET_SKILL_COUNT}"
    echo "  Subagents:         ${agent_count}"
    echo "  Venv:              ${VENV_DIR}"
    echo ""
    echo -e "${CYAN}GEO-SEO Commands:${NC}"
    echo "  /geo audit <url>       Full GEO + SEO audit"
    echo "  /geo quick <url>       60-second visibility snapshot"
    echo "  /geo report <url>      Client-ready GEO report"
    echo "  /geo report-pdf        Generate PDF report"
    echo ""
    echo -e "${CYAN}Marketing Commands:${NC}"
    echo "  /market audit <url>    Full marketing audit"
    echo "  /market copy <url>     Generate optimized copy"
    echo "  /market emails <topic> Email sequences"
    echo "  /market social <topic> 30-day social calendar"
    echo "  /market report-pdf <url> PDF marketing report"
    echo ""
    echo "  Start a new Claude Code session to use the skills."
    echo ""
}

main "$@"
