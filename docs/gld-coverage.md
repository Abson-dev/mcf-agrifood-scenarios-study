# GLD coverage of the 17 study countries

Checked 9 Nov 2026 against the World Bank Global Labor Database repository
([github.com/worldbank/gld](https://github.com/worldbank/gld), last updated 6 Nov 2026).
Row-level detail: [`metadata/gld_coverage.csv`](../metadata/gld_coverage.csv).

## What GLD gives us

- **Harmonisation code, not data.** Harmonised files inherit the raw survey's licence and
  are mostly accessible to World Bank staff only. The Stata do-files are public (MIT
  licence plus the World Bank IGO rider). To use them, we run them on raw files we obtain
  ourselves.
- Each do-file maps a survey to the GLD variable set (ICLS labour status, ISCO
  occupation, ISIC industry, earnings, hours), which is the same work the study's
  crosswalk would otherwise do.

## Coverage

| | Countries | Implication |
|---|---|---|
| **GLD code for the register round** | Nigeria (NLFS 2024, 2025), Kenya (KCHS 2022), Mozambique (IOF 2022), Ghana (AHIES 2022–24 only) | Run GLD code directly once the files are in hand |
| **GLD code for an earlier round only** | Uganda (NLFS 2021), Ethiopia (LFS 2021), Rwanda (LFS 2021), Tanzania (ILFS 2020/21), Malawi (LFS 2013), Ghana (no QLFS 2025) | Adapt the latest script; the instrument changed for Uganda (LMS 2025) and Ethiopia (NIHS) |
| **No GLD code** | All 8 WAEMU states for EHCVM (Senegal's GLD coverage is ENES, not EHCVM) | Write one EHCVM harmonisation module. EHCVM is harmonised across the 8 states by design, so a single module serves all of them |

## Findings that change the register

1. **Senegal has a standalone quarterly labour force survey (ENES)** running from 2015
   to Q4 2025, which is newer and more labour-specific than EHCVM-2. It was not in the
   original register. Files are licensed, and requests go to the ANSD Director-General.
   Recorded in `sources.csv` and flagged (`flags.csv` item 11).
2. **Uganda:** GLD has a `UGA_2023_UNHS` script, but its header is inconsistent (titled
   "National Labour Force Survey", no sample size) and no matching 2023 UNHS appears in the
   UBOS catalog. Not recorded as a source until confirmed.

## Header discrepancies to check before reuse

- **Nigeria:** the 2024 and 2025 scripts carry identical sample sizes (17,627 HH /
  90,170 individuals). Confirm which quarters each script expects.
- **Mozambique:** the GLD header gives 15,385 households against 15,732 in the INE
  catalog. Reconcile once the files arrive.
- **Senegal ENES:** the GLD header says ICLS-13 (not ICLS-19). This matters for
  comparability with ICLS-19 surveys (Nigeria, Ghana, Uganda).
