#!/bin/sh
# Deploy the committed site to Cloudflare Pages (project "webhunter"). Needs ~/.cf-token (Pages: Edit).
# Only tracked public files are uploaded — never _raw/ (private backups), tools/ or sources.
set -e
cd "$(dirname "$0")/.."
D=$(mktemp -d)
git archive HEAD | tar -x -C "$D"
rm -rf "$D/tools" "$D/assets/src" "$D/.gitignore" "$D/node_modules"
CLOUDFLARE_API_TOKEN=$(cat ~/.cf-token) CLOUDFLARE_ACCOUNT_ID=91c5bf467d30ea7e0c866ee7bcfd1e6f \
  npx --yes wrangler@3 pages deploy "$D" --project-name webhunter --branch main --commit-dirty=true
rm -rf "$D"
