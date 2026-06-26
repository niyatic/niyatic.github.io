#!/usr/bin/env bash
# Fails if any served *.html lacks the /gate.js soft-gate. Run pre-deploy.
# NOTE: gate.js is obfuscation-grade, not real auth (see CONTENT-HUB-IA-PLAN).
set -euo pipefail
root="${1:-.}"
missing=0
while IFS= read -r f; do
  case "$f" in */.git/*|*/node_modules/*) continue;; esac
  grep -qi 'gate\.js' "$f" || { echo "UNGATED: $f"; missing=$((missing+1)); }
done < <(find "$root" -name '*.html' -not -path '*/.git/*')
if [ "$missing" -gt 0 ]; then
  echo "FAIL: $missing ungated page(s). Add <script src=\"/gate.js\"></script> to <head>."; exit 1
fi
echo "OK: every .html references gate.js"
