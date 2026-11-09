# Contributing

## Workflow

1. Branch from `main`: `git switch -c <type>/<short-description>`, e.g.
   `source/uganda-lms-2025` or `docs/protocol-update`.
2. Make the change. For source records, edit `metadata/*.csv`, never the generated workbook.
3. Run the checks:
   ```bash
   python scripts/validate_metadata.py
   python scripts/check_no_microdata.py
   python scripts/build_source_matrix.py
   ```
4. Commit using the message prefixes below and open a pull request. CI must pass before
   merging.

## Commit messages

| Prefix | Use for |
|---|---|
| `source:` | Adding or updating a row in `sources.csv` |
| `flag:` | Raising or resolving an item in `flags.csv` |
| `access:` | Account, request or download status (`portals.csv`) |
| `docs:` | Protocol, data management plan, README |
| `build:` | Scripts, CI, tooling |

Example: `source: Ghana QLFS 2025 — Q1 file missing from catalog`

## Recording a source

Each row in `metadata/sources.csv` needs:

- **Source, agency, instrument type, round, reference period, sample size**, taken from
  the catalog entry
- **Catalog / host & ID**: portal plus study ID
- **Access status** and **what access requires**
- **Most recent round?**: if "No", say what is newer
- **Caveats** quoted or paraphrased from the documentation
- **Verification** (date and what was checked) and **Evidence URL**

Write "Not confirmed" where a field could not be verified. Follow the
[data access protocol](docs/data-access-protocol.md). In particular, never substitute an
older round silently.

## Never commit

Microdata, extracts, or anything containing respondent records. See the
[data management plan](docs/data-management-plan.md).
