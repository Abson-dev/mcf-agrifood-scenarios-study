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
│   └── <ISO3>_<SURVEY>_<ROUND>/
│       ├── <producer release folder>/   Unchanged, keeps the producer's version ID
│       └── documentation/               Basic information documents, questionnaires
└── processed/                       Harmonised extracts built by scripts
```

## Holdings

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
| `MWI_IHS6_2024-25` | MWI_2024-2025_IHS-VI_v01_M_STATA14 | 81 .dta | 12,888 | 55,911 | Integrated household survey; labour module `hh_mod_e`. **Not** a substitute for the Malawi LFS 2024 |

EHCVM household counts come from the `ehcvm_welfare` file. All counts match the World Bank
catalog except where noted. The EHCVM employment module is in `s04a_me`–`s04c_me` for
every country.

**Provenance**

- EHCVM-2 cross-sections (v01): copied on 9 Nov 2026 from an earlier download held locally.
  The API confirms they are the current release (unchanged since 2 Aug 2024). Confirm that
  the original download's terms cover this project.
- BFA panel (v05) and Malawi IHS6 (v01): downloaded via the WB MDL API on 9 Nov 2026 with
  `scripts/wb_mdl_download.py`. The panel replaces the v02 copies held in other local folders.
