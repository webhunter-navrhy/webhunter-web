#!/bin/sh
# Build: purge unused CSS + minify assets/src/* -> assets/site.min.*, bump cache-busting version.
# Edit sources in assets/src/ and the HTML, then run: sh tools/build.sh
set -e
cd "$(dirname "$0")/.."
TMP=$(mktemp -d)
npx --yes purgecss@6 --config tools/purgecss.config.cjs --output "$TMP/" >/dev/null
npx --yes csso-cli@4 "$TMP/site.css" -o assets/site.min.css --no-restructure
npx --yes terser@5 assets/src/site.js -c -m -o assets/site.min.js
rm -rf "$TMP"
V=$(date +%s)
for f in index.html realizace.html; do
  sed -i '' -E "s#assets/site(\.min)?\.(css|js)(\?v=[0-9]+)?\"#assets/site.min.\2?v=$V\"#g" "$f"
done
ls -la assets/site.min.css assets/site.min.js | awk '{print $5, $9}'
