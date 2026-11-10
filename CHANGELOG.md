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

### Added (Ghana)
- AHIES 2024 Q1–Q4 in `data/raw/focus-countries/GHA_AHIES_2022-24/`: 188,500 person-quarters,
  39,298 HH-quarters (= GLD 2024 header), quarterly `pop_weight`, 4/6-digit ISIC. 2022–2023
  not yet downloaded. DDI study documentation for AHIES and QLFS 2025.
- QLFS 2025 Q2–Q3 in `data/raw/focus-countries/GHA_QLFS_2025/`: 27,837 HH, 121,665 persons
  (= catalog), identical in .dta/.sav/.csv. No Q1 records despite the 'Q1–Q3' title (flag 7).
  The GSS site's account emails were failing on 10 Nov 2026; login later succeeded.
- Kenya Poverty Report 2022 added to `KEN_KCHSP_2022/documentation/`.

### Added (Kenya)
- KCHSP 2022 in `data/raw/focus-countries/KEN_KCHSP_2022/`: 17,894 HH, 71,239 persons,
  four quarters, 47 counties. Year confirmed from the data; 4-digit ISIC for main jobs.
  Questionnaire still to download.

### Added (Rwanda)
- LFS 2025 in `data/raw/focus-countries/RWA_LFS_2025/`: 14,528 HH, 100,852 persons
  (= catalog). Labour status is derived for 14+, so the 16+ working-age concern is
  resolved. New limit flagged: ISIC/ISCO 2-digit only and no quarter ID.

### Added (Tanzania)
- ILFS 2025 in `data/raw/ag-programming/TZA_ILFS_2025/`: 60,889 persons (= catalog), about
  14,217 HH, Mainland and Zanzibar. The 'For_Sharing' file has 434 vs 559 catalog variables;
  the difference is split text segments, not missing content. Annual pooled weight.

### Added (Nigeria)
- NLFS Q2 2024–Q2 2025, all 5 quarters, in `data/raw/focus-countries/NGA_NLFS_2024Q2-2025Q2/`,
  organised by quarter; original NBS zip kept in `_download/`. Counts and weights verified.
- NLFS Q1 2024 in `data/raw/focus-countries/NGA_NLFS_2024Q1/`: 8,821 HH, 45,318 persons.
  Nigeria now complete for Q1 2024–Q2 2025 (six quarters).
- Flagged: Q3/Q4 2024 have no household file; Q2 2024 has far fewer coded main jobs,
  mainly in agriculture. Q1 2024 (same format) is normal, so the shortfall is specific to
  Q2 2024. Issue #10 (completeness) resolved.

### Added (GLD)
- GLD coverage check for all 17 countries (`metadata/gld_coverage.csv`,
  `docs/gld-coverage.md`, "GLD coverage" sheet in the workbook).
- Senegal ENES 2025 (standalone quarterly LFS, licensed) added to `sources.csv`; flag 11.

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
