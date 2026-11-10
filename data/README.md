# data/

Local microdata store. **Nothing in this folder except this README is tracked by git**
(see the [data management plan](../docs/data-management-plan.md)). File names, sizes and
SHA-256 checksums are recorded in [`metadata/raw_manifest.csv`](../metadata/raw_manifest.csv).
Regenerate the manifest after adding files:

```bash
python scripts/build_raw_manifest.py
```

## Layout

```
data/
├── raw/                             As released by the producer. Read-only, never edited.
│   ├── focus-countries/             Nigeria, Kenya, Uganda, Ethiopia, Ghana, Rwanda
│   ├── ag-programming/              Malawi, Mozambique, Tanzania
│   └── waemu/                       Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau,
│       │                            Mali, Niger, Senegal, Togo
│       └── <ISO3>_<SURVEY>_<ROUND>/
│           ├── <producer release folder>/   Unchanged, keeps the producer's version ID
│           └── documentation/               Basic information documents, manuals, reports
└── processed/                       Harmonised extracts built by scripts
```

Every dataset folder sits under exactly one coverage group. `build_raw_manifest.py` stops
with an error if it finds a folder outside the three groups.

## Holdings

### focus-countries/

| Folder | Release | Quarter | Files | Households | Individuals | Notes |
|---|---|---|---|---|---|---|
| `NGA_NLFS_2024Q1` | NGA-NBS-NLFS-Q12024-v1.0 (NBS catalog 151) | 2024Q1 | HH + indiv (.sav) | 8,821 | 45,318 | 21,724 coded main jobs (agriculture 7,008), in line with later quarters |
| `NGA_NLFS_2024Q2-2025Q2` | NGA-NBS-NLFS-Q22024-v1.0 (NBS catalog 152) | 2024Q2 | HH + indiv (.sav) | 8,806 | 44,852 | **Coding shortfall:** 12,455 coded main jobs vs 17,778–21,724 in other quarters (agriculture 4,000 vs 6,580–8,625). Specific to this quarter. Check before pooling |
| | | 2024Q3 | indiv only (.dta) | 8,802 | 43,955 | No household file; IDs and `popw` are in the individual file |
| | | 2024Q4 | indiv only (.dta) | 8,832 | 43,728 | No household file |
| | | 2025Q1 | HH + indiv (.dta) | 8,727 | 42,385 | |
| | | 2025Q2 | HH + indiv (.dta) | 8,346 | 39,934 | |

Nigeria layout: `<release>/<YYYYQn>/` holds the data per quarter, `documentation/` the Q2 2024
report and questionnaire, and `_download/` the original NBS zip for Q3 2024–Q2 2025, kept
unchanged for provenance. Weight `popw` is the population weight rescaled to NPC 2022, with
no missing values. Cleaned ISIC/ISCO codes are available for main and secondary jobs. The
catalog states 8,836 households per quarter.

Nigeria is complete: six consecutive quarters, Q1 2024 to Q2 2025.

| Folder | Release | Files | Households | Individuals | Notes |
|---|---|---|---|---|---|
| `RWA_LFS_2025` | RWA-NISR-RLFS-2025-v0.1 (`RW_LFS2025`) | .dta + .csv (identical) + variable list | 14,528 | 100,852 | Labour status derived for 14+ (so 15+ can be built). Annual weight `weight2`; no quarter ID. ISIC/ISCO 2-digit only, so food trade can't be split out of 46/47 |

| `KEN_KCHSP_2022` | KCHSP 2022 (KeNADA catalog 131) | 5 .dta: households, individuals, consumption aggregate, food items, non-food items | 17,894 | 71,239 | No year in file names; 2022 confirmed from the data. Annual labour weight `annual_indweight_labour`; quarterly `individual_weight_labour`; don't sum `weight_pop` over persons. Main-job 4-digit ISIC in `d23_isic`. Original individuals zip in `_download/`. `documentation/` holds the Kenya Poverty Report 2022 (no questionnaire yet) |
| `GHA_AHIES_2022-24` | AHIES 2024 Q1–Q4, GSS release 27 Aug 2025 (GSS catalog 128) | 1 .dta (person-quarter, 838 vars) | 39,298 HH-quarters (9,699–9,890 per quarter) | 188,500 person-quarters | **2024 only**: 2022 and 2023 not yet downloaded. `pop_weight` is quarterly (≈32M per quarter), so divide by 4 when pooling the year. Quarter in `quarter` (2024Q1–Q4). `hhid` changes every quarter, so it can't link households across quarters. Age `s1aq4y`. ISIC/ISCO coded at 4 and 6 digits for main and secondary jobs (`s4aq41a2`/`a3`), so food trade can be separated. Employed 15+ ≈12.0–12.7M per quarter. Labels are Latin-1 (read with `encoding="latin1"`). Original zip in `_download/`; `documentation/` holds the DDI study documentation (v2.1) |
| `GHA_QLFS_2025` | QLFS 2025 Q1–Q3 (GSS catalog 132) | — | — | — | **Data not yet downloaded.** `documentation/` holds the DDI study documentation only. The catalog lists one file, `2025QLFS_Q2-Q3` (121,665 cases, 524 vars): Q1 is still missing |

Still pending: Ghana QLFS 2025 data and AHIES 2022–2023; Uganda and Ethiopia formal
requests (see `metadata/portals.csv`).

### ag-programming/

| Folder | Release | Files | Households | Individuals | Notes |
|---|---|---|---|---|---|
| `MWI_IHS6_2024-25` | MWI_2024-2025_IHS-VI_v01_M_STATA14 | 81 .dta | 12,888 | 55,911 | Integrated household survey; labour module `hh_mod_e`. **Not** a substitute for the Malawi LFS 2024 |

| `TZA_ILFS_2025` | TZA-NBS-2025-v01 (`ILFS2025_URT_For_Sharing.sav`) | 1 .sav | ~14,217 (Zanzibar 3,647) | 60,889 | Annual weight: `weight` sums to the population over the 4 quarters, so quarterly estimates need ×4. Quarter in `qrt`. Labels in Swahili |

Mozambique (IOF 2022) and Malawi LFS 2024 are pending formal requests.

### waemu/

| Folder | Release | Files | Households | Individuals | Notes |
|---|---|---|---|---|---|
| `BEN_EHCVM-2_2021` | BEN_2021_EHCVM-2_v01_M_STATA14 | 60 .dta | 8,032 | 42,660 | |
| `BFA_EHCVM-2_2021` | BFA_2021_EHCVM-2_v01_M_Stata | 55 .dta | 7,176 | 47,090 | Welfare file is `ehcvm_welfare_2b_bfa2021.dta` |
| `CIV_EHCVM-2_2021` | CIV_2021_EHCVM-2_v01_M_STATA14 | 58 .dta | 12,965 | 64,491 | Catalog's 13,693 includes 728 non-completed interviews (`s00q08`=3); dedupe `ehcvm_menage` |
| `GNB_EHCVM-2_2021` | GNB_2021_EHCVM-2_v01_M_STATA14 | 60 .dta | 5,351 | 41,160 | |
| `MLI_EHCVM-2_2021` | MLI_2021_EHCVM-2_v01_M_STATA14 | 49 .dta | 6,143 | 43,472 | Security gaps in wave 1 (see sources.csv) |
| `NER_EHCVM-2_2021` | NER_2021_EHCVM-2_v01_M_STATA14 | 54 .dta | 6,622 | 38,753 | |
| `SEN_EHCVM-2_2021` | SEN_2021_EHCVM-2_v01_M_STATA14 | 58 .dta | 7,120 | 63,530 | |
| `TGO_EHCVM-2_2021` | TGO_2021_EHCVM-2_v01_M_STATA14 | 57 .dta | 6,462 | 28,815 | |
| `BFA_EHCVM-P_2021` | BFA_2021_EHCVM-P_v05_M_Stata | 55 .dta | 3,227 | 22,362 | Panel sub-sample (from EHCVM-1 2018/19); not the baseline sample |

EHCVM household counts come from the `ehcvm_welfare` file. All counts match the World Bank
catalog except where noted. The EHCVM employment module is in `s04a_me`–`s04c_me` for
every country.

**Provenance**

- EHCVM-2 cross-sections (v01): copied on 9 Nov 2026 from an earlier download held locally.
  The API confirms they are the current release (unchanged since 2 Aug 2024). Confirm that
  the original download's terms cover this project.
- BFA panel (v05) and Malawi IHS6 (v01): downloaded via the WB MDL API on 9 Nov 2026 with
  `scripts/wb_mdl_download.py`. The panel replaces the v02 copies held in other local folders.
