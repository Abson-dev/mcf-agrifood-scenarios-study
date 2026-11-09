# Data management plan

## Scope

Survey microdata obtained from the World Bank Microdata Library, the WAEMU household
survey portal and national statistics offices (NBS Nigeria, KNBS, UBOS, ESS, GSS, NISR,
NBS Tanzania, NSO Malawi, INE Moçambique) for the agrifood scenarios study.

## Storage

| Location | Contents | Shared via git |
|---|---|---|
| `data/raw/<country>/<survey-round>/` | Files exactly as downloaded, with the catalog's documentation | No |
| `data/processed/` | Harmonised extracts | No |
| `metadata/`, `registers/` | Source descriptions, no respondent records | Yes |

- Keep raw files read-only. Never edit them in place.
- Store microdata only on IFPRI-approved storage, not on personal cloud accounts.
- One folder per survey round, named `<ISO3>_<survey>_<round>` (e.g. `NGA_NLFS_2024Q1`).

## Licences and terms of use

Each dataset is used under its producer's terms, recorded in `metadata/sources.csv`. Common
conditions:

- No redistribution to third parties. Access is personal or institutional, and colleagues
  register themselves.
- No attempt to identify respondents, and no publication of results that could do so.
- Confidentiality declarations where required (NBS Nigeria; NBS Tanzania under the
  Statistics Act Cap. 351).
- Citation in the producer's required form.

## Safeguards

- `.gitignore` excludes `data/` and microdata file types repository-wide.
- CI runs `scripts/check_no_microdata.py` on every push and pull request.
- If microdata is committed by mistake, do not just delete it in a new commit. Notify the
  repository owner so the history can be rewritten.

## Retention

Keep microdata for the life of the project and any period its licence requires. Delete
it at the end if the licence requires that, and record the deletion in the CHANGELOG.
