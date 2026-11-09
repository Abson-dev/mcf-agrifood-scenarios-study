# MCF Agrifood Scenarios Study — data acquisition

Data acquisition and source documentation for the Mastercard Foundation agrifood
scenarios study (IFPRI). The study builds an agrifood employment baseline for
17 countries from national labour-force and household survey microdata.

**Countries**

- MCF focus countries (6): Nigeria, Kenya, Uganda, Ethiopia, Ghana, Rwanda
- Agriculture-programming countries (3): Malawi, Mozambique, Tanzania
- WAEMU member states (8): Benin, Burkina Faso, Côte d'Ivoire, Guinea-Bissau,
  Mali, Niger, Senegal, Togo

## Layout

```
registers/            Access register and source matrix (Excel)
  Data Access Register.xlsx                    routes, country register, action list
  Source matrix - working (Phase 2 Sheet 3).xlsx  verified sources, flags, account checklist
scripts/
  build_source_matrix.py                       regenerates the source matrix workbook
docs/questionnaires/  Survey questionnaires and documentation (PDFs from catalogs)
data/raw/             Downloaded microdata — NOT tracked in git
data/processed/       Harmonised extracts — NOT tracked in git
```

## Microdata policy

Microdata files are kept locally only. They are excluded by `.gitignore` because the
data-use terms of the World Bank Microdata Library, national statistics offices and
other hosts prohibit sharing files with third parties. Record each dataset's source,
round, sample and access status in the source matrix instead.

## Recording rules

- Record the **instrument type** (labour force survey, EHCVM living-conditions survey,
  continuous household survey module, …), not just the file. It determines how much
  labour detail is available.
- If the most recent round is not available, **do not substitute** an older round or a
  different survey. Record what exists and what access requires, and flag it.

## Regenerating the source matrix

```
python scripts/build_source_matrix.py "registers/Source matrix - working (Phase 2 Sheet 3).xlsx"
```

Requires `openpyxl`.
