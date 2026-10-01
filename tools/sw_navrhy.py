#!/usr/bin/env python3
"""Seznam návrhů Studentských Webů, u kterých /navrhy/<id> ukáže pruh „Líbí se mi / Chci něco změnit“.

    python3 tools/sw_navrhy.py            # synchronizace z CRM (štítek Studentské Weby + proposal_link)
    python3 tools/sw_navrhy.py <id> [...]  # navíc ručně přidat návrh (zapíše do tools/sw_navrhy_rucne.txt)
    python3 tools/sw_navrhy.py --dry       # jen vypíše, nic nezapíše

Výsledek je navrhy/sw.json (čte ho 404.html a backend funkce navrhReakce). Když se změní,
skript ho sám commitne a pushne (GitHub Pages ho zveřejní do ~1 min). Ostatní návrhy
(kampaně WebHunteru, reality) v seznamu nejsou a pruh se jim nikdy neukáže.
"""
import json, re, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "navrhy" / "sw.json"
MANUAL = ROOT / "tools" / "sw_navrhy_rucne.txt"
CRM = "https://app.base44.com/api/apps/6aa1b4252168f6515be64eba/entities/Client?limit=5000"
CRM_H = {"api_key": "3862a4e3751d48708e44ac6a1dee85b9", "X-App-Id": "6aa1b4252168f6515be64eba", "User-Agent": "Mozilla/5.0"}
APP = "6a366c8ba95efe01593d4844"
SKIP_PHASES = {"Odmítnuto", "Hotovo"}  # odmítnutým a hotovým webům pruh neukazujeme
ID = re.compile(r"^[a-f0-9]{24}$")


def get(url, headers):
    import ssl
    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx = ssl.create_default_context()
    return json.loads(urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60, context=ctx).read())


def proposal_ok(pid):
    try:
        return bool(get(f"https://base44.app/api/apps/{APP}/entities/Proposal/{pid}", {"X-App-Id": APP, "User-Agent": "Mozilla/5.0"}).get("url"))
    except Exception:
        return False


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry" in sys.argv
    manual = [l.split("#")[0].strip() for l in MANUAL.read_text().splitlines()] if MANUAL.exists() else []
    manual = [m for m in manual if m]
    for a in args:
        pid = a.rstrip("/").split("/")[-1]
        if not ID.match(pid) or not proposal_ok(pid):
            sys.exit(f"Neplatné nebo neexistující ID návrhu: {a}")
        if pid not in manual:
            manual.append(pid)
            if not dry:
                with MANUAL.open("a") as f:
                    f.write(f"{pid}\n")

    ids = set(manual)
    for c in get(CRM, CRM_H):
        if not any("student" in (l or "").lower() for l in (c.get("labels") or [])):
            continue
        if c.get("phase") in SKIP_PHASES:
            continue
        m = re.search(r"/navrhy/([a-f0-9]{24})", c.get("proposal_link") or "")
        if m:
            ids.add(m.group(1))

    ids = sorted(ids)
    old = json.loads(OUT.read_text()).get("ids", []) if OUT.exists() else []
    added, removed = sorted(set(ids) - set(old)), sorted(set(old) - set(ids))
    print(f"SW návrhů: {len(ids)} (+{len(added)} −{len(removed)})")
    for i in added:
        print("  +", i)
    for i in removed:
        print("  −", i)
    if dry or ids == old:
        return
    OUT.write_text(json.dumps({"ids": ids}, indent=0) + "\n")
    files = [str(OUT.relative_to(ROOT))] + ([str(MANUAL.relative_to(ROOT))] if MANUAL.exists() else [])
    subprocess.run(["git", "-C", str(ROOT), "add", *files], check=True)
    subprocess.run(["git", "-C", str(ROOT), "commit", "-m", f"SW návrhy: {len(ids)} (+{len(added)} −{len(removed)})", "--", *files], check=True)
    subprocess.run(["git", "-C", str(ROOT), "push", "-q", "origin", "main"], check=True)
    print("Zveřejněno (GitHub Pages do ~1 min).")


if __name__ == "__main__":
    main()
