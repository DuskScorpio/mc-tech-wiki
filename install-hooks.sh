#!/bin/bash
# install-hooks.sh — wire the pre-commit guardrail into this repo's .git/hooks.
# Run once after cloning:  bash install-hooks.sh
set -e
REPO="$(git rev-parse --show-toplevel)"
HOOK="$REPO/.git/hooks/pre-commit"
cp "$REPO/vault_lint.py" "$REPO/vault_lint.py"  # no-op, ensures file present
# Symlink (or copy) the hook so it survives and stays in sync with the repo.
cp "$REPO/.githooks/pre-commit" "$HOOK" 2>/dev/null || cp "$REPO/pre-commit.hook" "$HOOK" 2>/dev/null || true
# Fallback: write hook inline if no template present
if [ ! -x "$HOOK" ] && [ ! -f "$HOOK" ]; then
  cat > "$HOOK" <<'HOOK'
#!/bin/bash
set -e
REPO_DIR="$(git rev-parse --show-toplevel)"
LINT="$REPO_DIR/vault_lint.py"
PY="${PY:-python}"
[ -z "$OKF_SRC" ] && [ -d "C:/Hermes-Workspace/kc/okf/src" ] && export OKF_SRC="C:/Hermes-Workspace/kc/okf/src"
[ ! -f "$LINT" ] && { echo "vault_lint.py missing; skipping" >&2; exit 0; }
echo "Running vault_lint.py ..." >&2
"$PY" "$LINT" || { echo "vault_lint.py FAILED — commit BLOCKED. Fix, then recommit (or git commit --no-verify to bypass)." >&2; exit 1; }
HOOK
fi
chmod +x "$HOOK"
echo "Installed pre-commit hook at $HOOK"
