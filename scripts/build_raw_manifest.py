"""Write ``metadata/raw_manifest.csv``: one row per file under ``data/raw/``.

The manifest records path, size and SHA-256 so that anyone holding the same
licensed files can confirm they match the versions used in the study. It
contains file names and hashes only, never data, so it is safe to commit.

    python scripts/build_raw_manifest.py
"""

from __future__ import annotations

import csv
import hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "metadata" / "raw_manifest.csv"
# Coverage groups of the study; every dataset folder sits under one of them.
GROUPS = ("focus-countries", "ag-programming", "waemu")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    rows = []
    for path in sorted(RAW.rglob("*")):
        if not path.is_file() or path.name == ".gitkeep":
            continue
        rel = path.relative_to(RAW).as_posix()
        parts = rel.split("/")
        if len(parts) < 3 or parts[0] not in GROUPS:
            raise SystemExit(f"{rel}: expected data/raw/<group>/<dataset>/..., group in {GROUPS}")
        group, dataset = parts[0], parts[1]
        mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
        rows.append([group, dataset, rel, path.stat().st_size, sha256(path), f"{mtime:%Y-%m-%d}"])

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["group", "dataset", "path", "bytes", "sha256", "file_date"])
        w.writerows(rows)
    print(f"Wrote {OUT.relative_to(ROOT)}: {len(rows)} files")


if __name__ == "__main__":
    main()
