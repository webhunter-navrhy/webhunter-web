#!/bin/sh
# Build: purge unused CSS + minify assets/src/* -> assets/site.min.*, bump cache-busting version.
# Edit sources in assets/src/ and the HTML, then run: sh tools/build.sh
set -e
cd "$(dirname "$0")/.."
python3 tools/gen_en.py
python3 tools/gen_legal.py
python3 tools/gen_pages.py
python3 tools/gen_blog.py
python3 tools/gen_seo_files.py
cp 404.html navrhy/index.html
TMP=$(mktemp -d)
npx --yes purgecss@6 --config tools/purgecss.config.cjs --output "$TMP/" >/dev/null
npx --yes csso-cli@4 "$TMP/site.css" -o assets/site.min.css --no-restructure
npx --yes terser@5 assets/src/site.js -c -m -o assets/site.min.js
npx --yes terser@5 assets/src/track.js -c -m -o assets/track.min.js
npx --yes terser@5 assets/src/admin.js -c -m -o assets/admin.min.js
npx --yes csso-cli@4 assets/src/admin.css -o assets/admin.min.css
rm -rf "$TMP"
V=$(date +%s)
for f in index.html realizace.html ochrana-osobnich-udaju/index.html 404.html $(find sluzby en obchodni-podminky blog -name "*.html" 2>/dev/null); do
  sed -i '' -E "s#assets/site(\.min)?\.(css|js)(\?v=[0-9]+)?\"#assets/site.min.\2?v=$V\"#g" "$f"
done
ls -la assets/*.min.* | awk '{print $5, $9}'
