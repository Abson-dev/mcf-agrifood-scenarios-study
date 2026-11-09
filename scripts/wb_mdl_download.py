"""Download resources from the World Bank Microdata Library API.

The API key is read from the ``WB_MDL_API_KEY`` environment variable or from
the git-ignored ``.env`` file at the repository root. Never commit the key.

Examples
--------
List a study's resources::

    python scripts/wb_mdl_download.py MWI_2024-2025_IHS-VI_v01_M --list

Download questionnaires (resource type doc/qst) into docs/::

    python scripts/wb_mdl_download.py TGO_2021_EHCVM-2_v01_M --type doc/qst \
        --dest docs/questionnaires/EHCVM-2_2021/TGO

Download and unpack the Stata release into data/raw/::

    python scripts/wb_mdl_download.py BFA_2021_EHCVM-P_v05_M --match "*_Stata.zip" \
        --dest data/raw/waemu/BFA_EHCVM-P_2021 --extract
"""

from __future__ import annotations

import argparse
import fnmatch
import json
import os
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
API = "https://microdata.worldbank.org/index.php/api"
UA = "mcf-agrifood-data-acquisition"


def api_key() -> str:
    key = os.environ.get("WB_MDL_API_KEY")
    env = ROOT / ".env"
    if not key and env.exists():
        for line in env.read_text(encoding="utf-8").splitlines():
            if line.startswith("WB_MDL_API_KEY="):
                key = line.split("=", 1)[1].strip()
    if not key:
        sys.exit("WB_MDL_API_KEY not set (environment or .env)")
    return key


def request(url: str, key: str):
    req = urllib.request.Request(url, headers={"X-API-KEY": key, "User-Agent": UA})
    return urllib.request.urlopen(req, timeout=120)


def resources(idno: str, key: str) -> list[dict]:
    with request(f"{API}/catalog/{idno}/resources", key) as f:
        return json.load(f)["resources"]


def download(idno: str, res: dict, dest: Path, key: str) -> Path:
    name = Path(res["filename"]).name
    out = dest / name
    with request(f"{API}/resources/download/{idno}/{res['resource_id']}", key) as f:
        size = int(f.headers.get("Content-Length") or 0)
        if out.exists() and size and out.stat().st_size == size:
            print(f"  skip (have) {name}")
            return out
        dest.mkdir(parents=True, exist_ok=True)
        tmp = out.with_suffix(out.suffix + ".part")
        with open(tmp, "wb") as w:
            while chunk := f.read(1 << 20):
                w.write(chunk)
    if size and tmp.stat().st_size != size:
        tmp.unlink()
        raise RuntimeError(f"incomplete download: {name}")
    tmp.replace(out)
    print(f"  got {name} ({out.stat().st_size / 1e6:.1f} MB)")
    return out


def safe_extract(zpath: Path, dest: Path) -> None:
    """Extract, refusing any member that would land outside ``dest``."""
    base = dest.resolve()
    with zipfile.ZipFile(zpath) as z:
        for m in z.infolist():
            target = (dest / m.filename).resolve()
            if base != target and base not in target.parents:
                raise RuntimeError(f"unsafe path in zip: {m.filename}")
        z.extractall(dest)
    print(f"  extracted {zpath.name} -> {dest}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("idno", help="study IDNO, e.g. TGO_2021_EHCVM-2_v01_M")
    ap.add_argument("--list", action="store_true", help="list resources and exit")
    ap.add_argument("--type", help="dctype code to select, e.g. doc/qst or dat/micro")
    ap.add_argument("--match", help="filename glob to select, e.g. '*_Stata*.zip'")
    ap.add_argument("--dest", type=Path, help="output folder")
    ap.add_argument("--extract", action="store_true", help="unpack zips into a folder named after the zip")
    a = ap.parse_args()

    key = api_key()
    res = resources(a.idno, key)
    if a.list:
        for r in res:
            print(r["resource_id"], r["dctype"], "|", r["title"], "|", r.get("filename"))
        return
    sel = [
        r for r in res
        if r.get("filename")
        and (not a.type or a.type in r["dctype"])
        and (not a.match or fnmatch.fnmatch(Path(r["filename"]).name.lower(), a.match.lower()))
    ]
    if not sel or not a.dest:
        sys.exit("nothing selected (check --type/--match) or --dest missing")
    for r in sel:
        out = download(a.idno, r, a.dest, key)
        if a.extract and out.suffix.lower() == ".zip":
            safe_extract(out, a.dest / out.stem)
            out.unlink()


if __name__ == "__main__":
    main()
