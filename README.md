# MCF Agrifood Scenarios Study — Data Acquisition

[![CI](https://github.com/Abson-dev/mcf-agrifood-scenarios-study/actions/workflows/ci.yml/badge.svg)](https://github.com/Abson-dev/mcf-agrifood-scenarios-study/actions/workflows/ci.yml)

Survey microdata acquisition and source documentation for the Mastercard Foundation
agrifood scenarios study, implemented with IFPRI. The study builds an **agrifood
employment baseline for 17 African countries** from national labour force and household
survey microdata. This repository holds the access register, the verified source
matrix and the tooling that keeps them consistent. It never holds the microdata itself.

> **Status (9 Nov 2026):** all 17 countries identified against live catalogs. In hand:
> EHCVM-2 2021/22 for all 8 WAEMU states, the Burkina Faso EHCVM panel (v05) and Malawi
> IHS6 2024/25 (see [`data/README.md`](data/README.md)). Other countries are pending accounts
> and requests. Estimation starts Week 5.

## Coverage

| Group | Countries | Main instrument |
|---|---|---|
| MCF focus (6) | Nigeria, Kenya, Uganda, Ethiopia, Ghana, Rwanda | Labour force surveys (Kenya: continuous household survey module; Ethiopia: integrated household survey module) |
| Agriculture programming (3) | Malawi, Mozambique, Tanzania | LFS (Malawi, Tanzania); household budget survey with employment module (Mozambique) |
| WAEMU (8) | Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau, Mali, Niger, Senegal, Togo | EHCVM harmonised living-conditions survey with employment module |

### Access status by country

| Country | Most recent round | Access | Open issue |
|---|---|---|---|
| Nigeria | NLFS Q1 2024; Q2 2024–Q2 2025 | Registration | Confirm all quarters in release |
| Kenya | KCHSP 2022 | Registration | ILFS 2026 fielded, not released |
| Uganda | Labour Market Survey 2025 | 10% sample public; full file by request | Request to UBOS |
| Ethiopia | NIHS 2024/25 labour module | Not released | Request to ESS |
| Ghana | QLFS 2025 Q1–Q3 | Registration | Q1 file missing |
| Rwanda | LFS 2025 | Public use | Working age 16+ |
| Tanzania | ILFS 2025 | Public use | — |
| Malawi | LFS 2024 | Not released | Request to NSO. IHS6 2024/25 **in hand** as a separate instrument, not a substitute |
| Mozambique | IOF 2022 | Formal request | Request to INE |
| WAEMU ×8 | EHCVM-2 2021/22 | **In hand** (WB MDL v01) | EHCVM-3 2025/26 not released |

Full detail, caveats and evidence links: [`metadata/sources.csv`](metadata/sources.csv);
decisions pending: [`metadata/flags.csv`](metadata/flags.csv).

## Repository structure

```
.
├── metadata/                 Source of truth (CSV, reviewed via pull requests)
│   ├── sources.csv           One row per survey: agency, instrument, round, sample, access, caveats, evidence
│   ├── flags.csv             Gaps and decisions for the study lead
│   ├── portals.csv           Accounts and download checklist
│   └── raw_manifest.csv      Size and SHA-256 of every local microdata file (no data)
├── registers/                Excel deliverables
│   ├── Data Access Register.xlsx   Access routes, country register, sequenced actions
│   └── source_matrix.xlsx          Generated from metadata/ — do not edit by hand
├── scripts/
│   ├── build_source_matrix.py      metadata/*.csv → registers/source_matrix.xlsx
│   ├── validate_metadata.py        Completeness checks on sources.csv
│   ├── build_raw_manifest.py       data/raw → metadata/raw_manifest.csv
│   ├── wb_mdl_download.py          World Bank Microdata Library API downloads (key in .env)
│   └── check_no_microdata.py       Guard against committing microdata
├── docs/
│   ├── data-access-protocol.md     How sources are identified, verified and recorded
│   ├── data-management-plan.md     Storage, licences, confidentiality
│   └── questionnaires/             Survey instruments and catalog documentation
└── data/                     Local only — ignored by git (except data/README.md)
    ├── raw/                  Microdata as released, by coverage group
    │   ├── focus-countries/  NGA, KEN, UGA, ETH, GHA, RWA
    │   ├── ag-programming/   MWI, MOZ, TZA
    │   └── waemu/            BEN, BFA, CIV, GNB, MLI, NER, SEN, TGO
    └── processed/            Harmonised extracts
```

## Getting started

Requires Python 3.10+.

```bash
python -m pip install -r requirements.txt
python scripts/validate_metadata.py     # check the register
python scripts/build_source_matrix.py   # regenerate registers/source_matrix.xlsx
```

To download from the World Bank Microdata Library, put `WB_MDL_API_KEY=<key>` in a `.env`
file at the repository root. The file is git-ignored and must never be committed. Then run
`python scripts/wb_mdl_download.py <IDNO> --list`.

To record a new or updated source, edit `metadata/sources.csv`, run both scripts and open
a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Data governance

- **No microdata in git.** Data-use agreements of the World Bank Microdata Library and the
  national statistics offices prohibit redistribution. `.gitignore` and CI
  (`check_no_microdata.py`) enforce this. Details in the
  [data management plan](docs/data-management-plan.md).
- **No silent substitution.** If the most recent round is unavailable, it is recorded as a
  gap with what access would require — never replaced by an older round or another survey.
- **Instrument type is recorded** for every source, because it determines labour detail
  (LFS vs EHCVM employment module vs continuous household survey module).

See the [data access protocol](docs/data-access-protocol.md).

## Citation

See [CITATION.cff](CITATION.cff). Cite each dataset as required by its producer's terms
of use (listed in the catalog entry linked in `sources.csv`).

## Licence

Internal project repository — all rights reserved pending agreement with IFPRI on a
licence. Survey data and documentation remain the property of their producers.

## Contact

Aboubacar Hema — aboubacarhema94@gmail.com
