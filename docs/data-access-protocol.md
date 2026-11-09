# Data access protocol

How sources for the agrifood employment baseline are identified, verified, requested and
recorded. Every comparability claim in the study rests on the source matrix, so the
matrix has to be complete, current and traceable.

## 1. Identify the most recent round

For each country, find the most recent **labour force survey or household survey with an
employment module**. Search, in order:

1. The national statistics office's own NADA catalog. It usually holds the newest round.
2. World Bank Microdata Library (LSMS and EHCVM collections).
3. WAEMU household survey portal (EHCVM documentation).
4. IHSN catalog and ILO surveyLib for discovery and variable metadata. ILO harmonised
   files are not a data source.
5. NSO publications and release calendars, to catch rounds that are fielded but not yet
   in any catalog.

Record rounds that are fielded but unreleased (for example EHCVM-3 2025/26, Kenya ILFS
2026). They determine whether the baseline will need updating.

## 2. Verify against the live catalog

A row counts as verified only when its fields come from the catalog entry itself (study
description, data dictionary, access page), not from a secondary source. Record the
check date in `Verification` and the page in `Evidence URL`. Where a field could not be
read, write "Not confirmed" rather than leaving it blank or estimating.

## 3. Record the instrument, not just the file

| Instrument | Example | Labour detail |
|---|---|---|
| Labour force survey | NLFS (Nigeria), ILFS (Tanzania), LFS (Rwanda) | Full ICLS framework |
| Labour market survey with establishment module | LMS 2025 (Uganda) | Labour supply and demand |
| Harmonised living-conditions survey | EHCVM (WAEMU) | Employment module, not an LFS |
| Continuous household survey module | KCHSP (Kenya) | Quarterly labour module |
| Integrated or budget household survey | IHS6 (Malawi), IOF (Mozambique), NIHS (Ethiopia) | Employment module |

Note deviations that affect comparability: working-age cut-off (e.g. Rwanda 16+), ICLS
version, reference period, seasonal coverage, geographic exclusions.

## 4. No silent substitution

If the most recent round is not obtainable:

1. Record what exists, who holds it and what access requires.
2. Add a row to `metadata/flags.csv` with the decision needed.
3. Older rounds may be listed as "previous round, recorded for reference only". They are
   **never** used in place of the latest round without the study lead's decision.

## 5. Request sequence

Slowest requests go first: formal NSO requests (Uganda full file, Mozambique, Ethiopia,
Malawi) before registrations, and registrations before downloads.
