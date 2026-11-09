"""Fail if any tracked file looks like survey microdata.

Data-use agreements for the study's sources prohibit redistribution, so
microdata must never enter the repository. This guard runs in CI and can be
used as a pre-commit hook. CSVs under ``metadata/`` are allowed.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import PurePosixPath

BLOCKED_EXT = {
    ".dta", ".sav", ".zsav", ".por", ".sas7bdat", ".xpt", ".rds", ".rdata",
    ".parquet", ".feather", ".zip", ".7z", ".gz", ".csv", ".tsv",
}
ALLOWED_DIRS = ("metadata/",)
MAX_BYTES = 5 * 1024 * 1024  # anything larger needs a human look


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True)
    return [p for p in out.stdout.decode().split("\0") if p]


def main() -> int:
    problems = []
    for path in tracked_files():
        p = PurePosixPath(path)
        if path.startswith(ALLOWED_DIRS):
            continue
        if p.suffix.lower() in BLOCKED_EXT:
            problems.append(f"{path}: blocked file type {p.suffix}")
        if path.startswith("data/") and p.name != ".gitkeep":
            problems.append(f"{path}: files under data/ must not be tracked")
    sizes = subprocess.run(
        ["git", "ls-files", "--format=%(objectsize) %(path)"],
        capture_output=True, text=True,
    )
    if sizes.returncode == 0:
        for line in sizes.stdout.splitlines():
            size, _, path = line.partition(" ")
            if size.isdigit() and int(size) > MAX_BYTES:
                problems.append(f"{path}: {int(size) // 1024} KB exceeds size limit")

    for msg in problems:
        print(f"ERROR: {msg}")
    print(f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
