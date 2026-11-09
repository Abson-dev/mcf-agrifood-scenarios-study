# Changelog

All notable changes to the source register are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- EHCVM-2 2021/22 microdata for all 8 WAEMU states placed in `data/raw/` (WB MDL v01
  releases, copied from local archive). Household counts verified against the catalog.
- `metadata/raw_manifest.csv` with SHA-256 checksums; `scripts/build_raw_manifest.py`.
- `data/README.md` describing layout and holdings.
- Burkina Faso EHCVM panel 2021/22 **v05** (replaces local v02 copies) and Malawi IHS6
  2024/25, downloaded via the WB MDL API. Case counts verified against the catalog. IHS6 is
  recorded as a separate instrument and is not a substitute for the Malawi LFS 2024.
- EHCVM-2 (8 countries), BFA panel and IHS6 questionnaires in `docs/questionnaires/`.
- `scripts/wb_mdl_download.py` (API key read from git-ignored `.env`).

### Changed (layout)
- `data/raw/` split by coverage group: `focus-countries/`, `ag-programming/`, `waemu/`.
  `raw_manifest.csv` gains a `group` column; `build_raw_manifest.py` rejects folders
  outside the three groups.

### Flagged
- Côte d'Ivoire: catalog sample of 13,693 includes 728 non-completed interviews; 12,965 completed
  households are complete in all files. Initially misreported as a data gap (corrected).

### Changed
- Repository structure, data access protocol, data management plan, CI checks.
- `metadata/` CSVs as the single source of truth; the Excel source matrix is generated from them.

## 2026-11-09

### Added
- Verified sources for the seven previously unknown countries: Uganda (LMS 2025),
  Mozambique (IOF 2022), Ethiopia (NIHS 2024/25), Ghana (QLFS 2025), Rwanda (LFS 2025),
  Tanzania (ILFS 2025), Malawi (LFS 2024, IHS6 2024/25).
- Confirmed Benin, Togo and Guinea-Bissau in EHCVM-2 2021/22 (WB MDL 6272, 6279, 6274).

### Flagged
- EHCVM-3 2025/26 fielded across WAEMU and not yet released, so EHCVM-2 is not the latest round.
- Kenya ILFS 2026 fielded Jun–Sep 2026 (first standalone LFS since 1998).
- Uganda full LMS sample, Mozambique IOF 2022, Ethiopia NIHS and Malawi LFS 2024 need formal requests.
