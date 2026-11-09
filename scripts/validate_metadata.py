"""Validate the metadata CSVs before they are merged.

Checks that every source row has the fields the study's comparability claims
depend on, that evidence links are URLs, and that all 17 study countries are
covered. Exits non-zero on any error so it can run in CI.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

META = Path(__file__).resolve().parents[1] / "metadata"

COUNTRIES = {
    "Nigeria", "Kenya", "Uganda", "Ethiopia", "Ghana", "Rwanda",
    "Malawi", "Mozambique", "Tanzania",
    "Benin", "Burkina Faso", "Côte d'Ivoire", "Guinea-Bissau",
    "Mali", "Niger", "Senegal", "Togo",
}

REQUIRED = [
    "Country", "Source (survey)", "Agency", "Instrument type", "Round",
    "Sample size", "Catalog / host & ID", "Access status",
    "Most recent round?", "Verification", "Evidence URL",
]


def load(name: str) -> list[dict[str, str]]:
    with open(META / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def main() -> int:
    errors: list[str] = []
    sources = load("sources.csv")

    missing_cols = [c for c in REQUIRED if c not in sources[0]]
    if missing_cols:
        errors.append(f"sources.csv is missing columns: {missing_cols}")
    else:
        for i, row in enumerate(sources, start=2):
            for col in REQUIRED:
                if not (row.get(col) or "").strip():
                    errors.append(f"sources.csv line {i} ({row['Country']}): empty '{col}'")
            url = row["Evidence URL"].strip()
            if url and not url.startswith(("http://", "https://")):
                errors.append(f"sources.csv line {i}: Evidence URL is not a URL: {url!r}")
            if row["Country"] not in COUNTRIES:
                errors.append(f"sources.csv line {i}: unknown country {row['Country']!r}")

        missing = COUNTRIES - {r["Country"] for r in sources}
        if missing:
            errors.append(f"sources.csv has no row for: {sorted(missing)}")

    for name in ("flags.csv", "portals.csv"):
        if not load(name):
            errors.append(f"{name} is empty")

    for e in errors:
        print(f"ERROR: {e}")
    print(f"{len(sources)} sources checked, {len(errors)} error(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
