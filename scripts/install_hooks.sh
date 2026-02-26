#!/usr/bin/env bash
# Install git hooks for this repository.
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOK_SRC="$REPO_ROOT/.git/hooks/pre-commit"

if [ ! -d "$REPO_ROOT/.git" ]; then
    echo "Error: not a git repository" >&2
    exit 1
fi

# Write the pre-commit hook
cat > "$HOOK_SRC" << 'HOOK'
#!/usr/bin/env bash
# Pre-commit hook: validate URLs in resources.json when it is staged.

if git diff --cached --name-only | grep -q '^resources\.json$'; then
    echo "resources.json staged — running URL validation..."
    uv run python scripts/validate_urls.py --force
fi
HOOK

chmod +x "$HOOK_SRC"
echo "Pre-commit hook installed at $HOOK_SRC"
