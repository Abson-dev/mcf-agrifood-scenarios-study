import sys
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

OUT = sys.argv[1]
V = "Checked 9 Nov 2026 (catalog page)"

cols = ["Country", "Group", "Source (survey)", "Agency", "Instrument type", "Round",
        "Reference period / fieldwork", "Sample size", "Catalog / host & ID",
        "Access status", "What access requires", "Most recent round?",
        "Caveats in documentation", "Flag for John", "Verification", "Evidence URL"]

R = []
def r(*a): R.append(a)

# ---------------- Seven unknowns ----------------
r("Uganda", "Focus", "Labour Market Survey (LMS) 2025", "UBOS (co-producer MoFPED)",
  "Labour market survey: household labour-supply module + establishment labour-demand module. New series; NLFS was 5-yearly standalone LFS.",
  "2025", "Fieldwork Mar–Sep 2025 (CAPI); quarterly reference periods Q1 Mar–May, Q2 Jun–Aug",
  "~10,350 HH designed (1,035 EAs x 10); 96.2% HH response; 2,985 formal + 4,951 informal establishments",
  "UBOS NADA microdata.ubos.org:7070 catalog/106; DDI-UGA-UBOS-LMS-2025-V01",
  "Registration, then download — but posted HH file is a 10% anonymised sample only",
  "Free UBOS account gives 10% sample (LMS_HH_10%percent_1_Anonymized, 4,887 cases, 476 vars). Full file requires request to UBOS (ubos@ubos.org); procedure/fees not documented online.",
  "Yes",
  "Weights only for Q1 and Q2 although fieldwork ran to Sept; age bands differ by indicator (15+, 14–64, 15–24, 18–30); ICLS standard not cited; earnings content not documented (keyword 'Wages' only); achieved HH count not stated.",
  "Full-sample file not public — formal request needed. Instrument differs from NLFS series (adds establishment module).",
  V, "http://microdata.ubos.org:7070/index.php/catalog/106")
r("Uganda", "Focus", "National Labour Force Survey (NLFS) 2021 — previous round, recorded for reference only", "UBOS",
  "Standalone labour force survey (20th ICLS)", "2021", "2021",
  "8,668 HH completed (95%); 39,522 individuals",
  "UBOS NADA catalog/98; DDI-UGA-UBOS-NLFS-2021-v01",
  "Registration; posted file is 10% sample (NLFS_2021_10PERCENT, 4,780 cases, 833 vars)",
  "As LMS 2025: full file by request to UBOS",
  "No — superseded by LMS 2025",
  "Page reports unweighted sample 47,690 vs 39,522 completed interviews — unresolved; estimates reliable to 15 sub-regions only; weighting formula in separate technical report.",
  "Not a substitute for LMS 2025.", V, "http://microdata.ubos.org:7070/index.php/catalog/98")

r("Mozambique", "Ag programming", "Inquérito sobre Orçamento Familiar (IOF) 2022", "INE Moçambique",
  "Household budget survey with employment module (persons 5+). No regular LFS: last was IFTRAB 2004/05.",
  "2022 (WIDER labels it 2022/23)", "Year 2022 only on catalog; months not stated. 7-day continuous household visit.",
  "15,732 HH (9,072 urban; 6,660 rural)",
  "INE NADA mozdata.ine.gov.mz catalog/79; MOZ-INE.IOF2022.V5.C321",
  "Formal request to INE (per CIPMoz 2026: IOF 2019/20 and 2022 microdata 'mediante pedido formal')",
  "Formal application to INE (info@ine.gov.mz); get-microdata page shows no terms. Alternative derivative: UNU-WIDER harmonised labour dataset 1996–2023 via online form (harmonised, not raw).",
  "Yes",
  "Version mismatch (header V5, metadata V6); fieldwork window not stated — IOF 2019/20 ran 13 months/4 quarters, so seasonal coverage of 2022 is unconfirmed; urban stratum boosted vs 2019/20; comparability with 2019/20 not addressed.",
  "Not openly downloadable — formal INE request. Check seasonality before comparing to 2019/20.",
  V, "https://mozdata.ine.gov.mz/index.php/catalog/79")
r("Mozambique", "Ag programming", "IOF 2019/20 — previous round, recorded for reference only", "INE Moçambique",
  "Household budget survey with employment module", "2019/20", "Full year, 21 fortnightly periods",
  "Not stated on page (1,320 PSUs; 9–12 HH per EA)", "INE NADA catalog/88; MOZ-INE.IOF2019-20.V5.C321",
  "Formal request (as above)", "As above", "No",
  "Doc ID says V4 vs V5; weights adjusted to Aug 2020 population.", "Not a substitute for IOF 2022.",
  V, "https://mozdata.ine.gov.mz/index.php/catalog/88")

r("Ethiopia", "Focus", "National Integrated Household Survey (NIHS) 2024/25 — Labour Force Module", "Ethiopian Statistical Service (ESS)",
  "Integrated household survey with labour force module (first NIHS; module built into HH questionnaire)",
  "2024/25", "Fieldwork from 25 Sep 2024; key-findings report Sep 2026",
  "Not confirmed (report PDF could not be read)",
  "ESS key findings report only; no microdata entry found on ESS, WB MDL or ILO surveyLib",
  "Microdata not released (not found)", "Formal request to ESS; expect restricted",
  "Yes",
  "Coverage table exists in report but not read — Tigray/conflict-area coverage unverified. Headline: LF 80.1m, LFPR 67.8%.",
  "Most recent round has no public microdata. Need ESS request and coverage check.",
  "Checked 9 Nov 2026 (report listing; PDF not readable)",
  "https://ess.gov.et/wp-content/uploads/2026/09/final_-version_nihs_lf_key_findings_15_september_2026.pdf")
r("Ethiopia", "Focus", "Labour Force and Migration Survey (NLFS) 2021 — previous round, recorded for reference only", "ESS",
  "Standalone labour force survey", "2021", "2021",
  "File ETH_NLFS_2021_FULL: 174,615 cases, 279 vars (ILO metadata)",
  "ILO surveyLib catalog/7982 (metadata); ESS report",
  "External access not confirmed", "ESS request", "No", "", "Not a substitute for NIHS 2024/25.",
  V, "https://webapps.ilo.org/surveyLib/index.php/catalog/7982")

r("Ghana", "Focus", "Quarterly Labour Force Survey (QLFS) 2025, Q1–Q3", "Ghana Statistical Service (GSS), WB TA",
  "Standalone quarterly labour force survey (household panel over 3 quarters)",
  "2025 Q1–Q3", "Q1–Q3 2025; dates not stated",
  "13,920 HH; 1,160 EAs; 16 regions. File 2025QLFS_Q2-Q3: 121,665 cases, 524 vars",
  "GSS NADA microdata.statsghana.gov.gh catalog/132; DDI-GHA-GSS-QLFS-2025Q1-Q3-v1.1",
  "Registration, then download", "Free GSS account",
  "Yes",
  "Only a Q2–Q3 file is posted although study title says Q1–Q3; sample designed for regional unemployment rate; v1.1 vs 1.0 mismatch; GSS Q2 2025 unemployment reported as 13.1% then 12.6% in later release.",
  "Q1 2025 file missing from catalog — ask GSS.", V, "https://microdata.statsghana.gov.gh/index.php/catalog/132")
r("Ghana", "Focus", "Annual Household Income and Expenditure Survey (AHIES) 2022–2024", "GSS",
  "Quarterly household panel income/expenditure survey with labour module", "2022–2024",
  "Quarterly 2022–2024",
  "10,800 HH; 600 EAs. Files: 2022 (209,943), 2023 (196,953), 2024 (188,500) cases, 838 vars",
  "GSS NADA catalog/128; DDI-GHA-GSS-AHIES-2022-2024-v1.1",
  "Registration, then download", "Free GSS account",
  "No for labour (QLFS 2025 is newer); latest AHIES",
  "Catalog says v1.1 is 'raw sample data… for office use only'; ICLS not cited.",
  "Different instrument from QLFS — choice of series is John's.", V,
  "https://microdata.statsghana.gov.gh/index.php/catalog/128")

r("Rwanda", "Focus", "Labour Force Survey (LFS) 2025", "NISR with MINECOFIN",
  "Standalone labour force survey; 4 quarterly rounds pooled to annual (design since Feb 2019)",
  "2025", "4 quarters of 2025",
  "File RW_LFS2025: 100,852 persons, 207 vars (HH count not stated)",
  "NISR NADA microdata.statistics.gov.rw catalog/125; RWA-NISR-RLFS-2025-v0.1",
  "Public use; registration, then download", "Free NISR account; accept public-use terms",
  "Yes",
  "Working age is 16+ (not 15+) — affects comparability; catalog year field '0'; version 0.1; excludes institutions, seasonal dwellings, workers living at work-sites; income from employment collected.",
  "", V, "https://microdata.statistics.gov.rw/index.php/catalog/125")

r("Tanzania", "Ag programming", "Integrated Labour Force Survey (ILFS) 2025", "NBS Tanzania",
  "Standalone labour force survey (Mainland + Zanzibar), 4 quarterly rounds",
  "2025", "1 Jan–31 Dec 2025",
  "14,232 HH (10,584 Mainland; 3,648 Zanzibar); 99.63% response. File ILFS2025_URT_For_Public: 60,889 cases, 559 vars",
  "NBS NADA microdata.nbs.go.tz catalog/65; TZA-NBS-2025-v01",
  "Public use; registration + confidentiality declaration", "Free account; confidentiality declaration under Statistics Act Cap. 351",
  "Yes",
  "ICLS not cited explicitly (ILO technical guidance noted); own-use agricultural production treatment not documented; ILFS 2024 also exists (catalog/63).",
  "", V, "https://microdata.nbs.go.tz/index.php/catalog/65")

r("Malawi", "Ag programming", "Labour Force Survey (LFS) 2024", "NSO Malawi with Ministry of Labour",
  "Standalone labour force survey (second ever; previous 2013); working age 15–64",
  "2024", "2024 (dates not confirmed)", "Not confirmed",
  "NSO report published; ILO surveyLib metadata (MWI_2024_LFS_v01_M_ILO_VAR); no microdata found on NSO, WB MDL or IHSN",
  "Microdata not released (not found)", "Request to NSO Malawi",
  "Yes",
  "Working-age definition 15–64 in report.",
  "Most recent LFS has no public microdata. NSO request needed.",
  "Checked 9 Nov 2026 (report + ILO listing)",
  "https://cms.nsomalawi.mw/api/download/651/Malawi-Labor-Force-Survey-Report---2024.pdf")
r("Malawi", "Ag programming", "Sixth Integrated Household Survey (IHS6) 2024/25", "NSO Malawi",
  "Integrated household survey (LSMS) with time-use and labour module", "2024/25",
  "23 Jul 2024 – 16 Jul 2025", "Not stated on page (99.9% response)",
  "WB MDL catalog/8507; MWI_2024-2025_IHS-VI_v01_M",
  "Registration, then download (use within organisation only; no third parties)", "Free WB MDL account; accept terms",
  "Yes (for IHS series)",
  "Agriculture refers to last completed season (2022/23 or 2023/24) not survey year; refugee weights uncalibrated; access terms ask users to cite IHS5 (apparent error).",
  "Different instrument from LFS 2024 — record both; series choice is John's.", V,
  "https://microdata.worldbank.org/catalog/8507")

# ---------------- WAEMU EHCVM-2 ----------------
E3 = "EHCVM-3 (2025/26) fielded across WAEMU (wave 1 Oct–Dec 2025, wave 2 Apr–Jun 2026); regional cleaning Oct 2026; results expected ~Dec 2026, microdata not yet released."
common = "Clusters reused from 2018/19 frame; two waves each covering half the sample; sampling text partly copied from 2018/19 docs."
ehcvm = [
 ("Senegal", "ANSD", "Nov 2021–Jan 2022 / Apr–Sep 2022", "7,120 HH (3,922 urban; 3,198 rural)", "6278", "SEN", "2013 census frame; abstract says ~7,100."),
 ("Côte d'Ivoire", "INS", "Nov 2021–Jan 2022 / Apr–Jul 2022", "13,693 HH (5,675 urban; 8,018 rural)", "6273", "CIV", "2014 census frame; clusters with <12 HH supplemented."),
 ("Burkina Faso", "INSD", "Sep–Nov 2021 / Apr–Jun 2022", "7,176 HH (of 7,200)", "6277", "BFA", "Panel component separate (WB MDL catalog/6224); security-related gaps not stated on page — check PDF."),
 ("Mali", "INSTAT", "Oct–Dec 2021 / Apr–Jul 2022", "6,143 HH (of 6,708 planned)", "6275", "MLI", "Insecurity: Kidal, Ménaka, Taoudénit not covered in wave 1; 7 EAs in Timbuktu/Mopti replaced; no rural Bamako."),
 ("Niger", "INS", "Nov 2021–Feb 2022 / Jun–Aug 2022", "6,622 HH (2,511 urban; 4,111 rural)", "6276", "NER", "504 EAs x 12 HH = 6,048, not 6,622 — inconsistency."),
 ("Benin", "INSAE (now INStaD)", "Nov 2021–Jan 2022 / Apr–Jul 2022", "8,032 HH (3,952 urban; 4,080 rural)", "6272", "BEN", "2013 census frame; collection end date shown as 2026-11-09 (metadata error)."),
 ("Togo", "INSEED", "Oct 2021–Jan 2022 / Apr–Jul 2022", "6,462 HH (abstract says ~6,100)", "6279", "TGO", "2010 census frame; rural coverage of Lomé Commune unclear."),
 ("Guinea-Bissau", "INE Guiné-Bissau", "Nov 2021–Jan 2022 / Apr–Aug 2022", "5,351 HH", "6274", "GNB", "2009 census frame; Bissau urban only; replacement households used."),
]
for c, ag, fw, n, cid, iso, cav in ehcvm:
    conf = "Confirmed in programme (new)" if c in ("Benin", "Togo", "Guinea-Bissau") else ""
    r(c, "WAEMU", "EHCVM-2 (Enquête Harmonisée sur les Conditions de Vie des Ménages)", ag + " with WB and WAEMU Commission",
      "Harmonised living-conditions survey with employment module (not an LFS)", "2021/22, two waves", fw, n,
      f"WB MDL catalog/{cid}; {iso}_2021_EHCVM-2_v01_M; also WAEMU portal phmecv.uemoa.int/nada",
      "Registration, then download", "Free WB MDL account; accept confidentiality terms",
      "No — EHCVM-3 2025/26 fielded, not yet released",
      cav + " " + common,
      ("Benin/Togo/GB confirmed in EHCVM-2. " if conf else "") + E3,
      V, f"https://microdata.worldbank.org/index.php/catalog/{cid}")

# ---------------- Nigeria, Kenya ----------------
r("Nigeria", "Focus", "Nigeria Labour Force Survey (NLFS) Q1 2024", "NBS Nigeria",
  "Labour force survey (quarterly)", "Q1 2024", "31 Jan – 20 Mar 2024", "8,836 HH (target 8,880/quarter)",
  "NBS NADA microdata.nigerianstat.gov.ng catalog/151; NGA-NBS-NLFS-Q12024-v1.0",
  "Registration + confidentiality declaration, then download", "NBS account; signed confidentiality declaration (NBS says full access policy still being developed)",
  "Yes",
  "100% response and 'no deviations' reported — verify; weighting method not described; sampling error national only (~1%).",
  "", V, "https://microdata.nigerianstat.gov.ng/index.php/catalog/151")
r("Nigeria", "Focus", "NLFS Q2 2024 – Q2 2025", "NBS Nigeria",
  "Labour force survey (quarterly series)", "Q2 2024 – Q2 2025", "Collection dates given only as 2024", "8,836 HH per quarter",
  "NBS NADA catalog/152; NGA-NBS-NLFS-Q22024-v1.0",
  "Registration + confidentiality declaration, then download", "As Q1 2024",
  "Yes — no later quarter found in catalog",
  "Version notes describe only the cleaned Q2 2024 dataset; Q3 2024–Q2 2025 files named in abbreviation may not all be in v1.0 — confirm on download; sampling text refers to Q1 2024.",
  "Confirm all 5 quarters are in the release.", V, "https://microdata.nigerianstat.gov.ng/index.php/catalog/152")
r("Kenya", "Focus", "Kenya Continuous Household Survey Programme (KCHSP) 2022 — quarterly labour module", "KNBS",
  "Continuous household survey with quarterly labour module (not a standalone LFS)", "2022",
  "Quarterly 2022", "Not checked",
  "KeNADA statistics.knbs.or.ke/nada catalog/131",
  "Registration, then download", "KeNADA account",
  "Latest KCHS released — but KNBS quarterly labour reports stop at Q4 2022, and 2026 ILFS now in field",
  "Catalog year field blank; nothing after 2022 on KeNADA.",
  "Kenya 2026 Integrated Labour Force Survey (second ever, first since 1998) fielded Jun–Sep 2026; results/microdata not yet released. 'No standalone LFS since 1998/99' is now out of date.",
  V, "https://statistics.knbs.or.ke/nada/index.php/catalog/131")

wb = Workbook()
ws = wb.active
ws.title = "Source matrix"
ws.append(["Source matrix — working copy for Phase 2 registers, Sheet 3"])
ws.append(["Compiled 9 Nov 2026 from live catalog pages. Not yet merged into the Phase 2 workbook. 'Previous round' rows are kept for reference only and are not substitutes."])
ws.append(cols)
for row in R:
    ws.append(list(row))

hdr = PatternFill("solid", fgColor="1F3864")
amber = PatternFill("solid", fgColor="FFF2CC")
thin = Side(style="thin", color="BFBFBF")
ws["A1"].font = Font(bold=True, size=13)
ws["A2"].font = Font(italic=True, color="595959")
for c in ws[3]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = hdr
    c.alignment = Alignment(wrap_text=True, vertical="center")
widths = [13, 12, 34, 22, 34, 14, 26, 30, 34, 28, 36, 22, 50, 44, 20, 40]
for i, w in enumerate(widths, 1):
    ws.column_dimensions[get_column_letter(i)].width = w
for row in ws.iter_rows(min_row=4, max_row=ws.max_row):
    flagged = bool(row[13].value)
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")
        c.border = Border(top=thin, bottom=thin, left=thin, right=thin)
        if flagged and c.column == 14:
            c.fill = amber
ws.freeze_panes = "D4"
ws.auto_filter.ref = f"A3:{get_column_letter(len(cols))}{ws.max_row}"

# ---- Flags sheet ----
fl = wb.create_sheet("Flags for John")
fl.append(["#", "Country", "Issue", "What exists", "What it would take", "Decision needed"])
flags = [
 ("WAEMU (all 8)", "EHCVM-2 2021/22 is not the most recent round", "EHCVM-3 2025/26 fully fielded; cleaning Oct 2026; results expected ~Dec 2026", "Wait for release, or ask WAEMU Commission / NSOs / WB LSMS for early access", "Proceed on EHCVM-2 for Week 5 and swap later, or wait for EHCVM-3?"),
 ("Kenya", "Standalone ILFS 2026 now exists", "Fieldwork Jun–Sep 2026; no release date found; KCHS labour reports stop at Q4 2022", "Ask KNBS for release timing", "Plan on KCHS 2022, or wait for ILFS 2026?"),
 ("Uganda", "Full LMS 2025 sample not public", "Only 10% anonymised HH file posted (4,887 cases)", "Formal request to UBOS (ubos@ubos.org); procedure not published", "Approve lodging the request now"),
 ("Mozambique", "IOF 2022 by formal request only", "15,732 HH; employment module 5+; no LFS since 2004/05", "Formal application to INE (info@ine.gov.mz)", "Approve request; who signs for IFPRI?"),
 ("Ethiopia", "NIHS 2024/25 labour module microdata not released", "Key findings report only (Sep 2026)", "Request to ESS; expect restricted", "Approve request; check conflict-area coverage"),
 ("Malawi", "LFS 2024 microdata not released", "Report only; IHS6 2024/25 (labour module) is downloadable on WB MDL", "Request to NSO for LFS 2024", "Which instrument is the baseline: LFS 2024 or IHS6?"),
 ("Ghana", "QLFS 2025 Q1 file missing", "Only Q2–Q3 file posted; AHIES 2022–24 also available", "Ask GSS for Q1", "Which series is the baseline: QLFS or AHIES?"),
 ("Rwanda", "Working age is 16+", "LFS 2025 public use", "Re-derive 15+ where possible", "Note for comparability"),
 ("Nigeria", "Q2 2024–Q2 2025 release may not include all quarters", "v1.0 notes mention only Q2 2024", "Verify on download", "None yet"),
]
for i, f in enumerate(flags, 1):
    fl.append([i, *f])
for c in fl[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = hdr
for i, w in enumerate([4, 16, 40, 48, 44, 44], 1):
    fl.column_dimensions[get_column_letter(i)].width = w
for row in fl.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")

# ---- Registration / download checklist ----
rg = wb.create_sheet("Accounts & downloads")
rg.append(["Portal", "URL", "Needed for", "Account status", "Download status"])
regs = [
 ("World Bank Microdata Library", "https://microdata.worldbank.org", "EHCVM-2 x8 (catalog 6272–6279, 6224 panel); Malawi IHS6 (8507)", "Not registered", "Blocked on account"),
 ("WAEMU household survey portal", "https://phmecv.uemoa.int/nada", "EHCVM documentation; second route to files", "Not registered", "—"),
 ("Kenya KeNADA", "https://statistics.knbs.or.ke/nada", "KCHSP 2022 (131)", "Not registered", "Blocked on account"),
 ("Nigeria NBS NADA", "https://microdata.nigerianstat.gov.ng", "NLFS Q1 2024 (151); Q2 2024–Q2 2025 (152)", "Not registered", "Blocked on account + confidentiality declaration"),
 ("UBOS microdata archive (extra)", "http://microdata.ubos.org:7070", "LMS 2025 10% file (106); then full-file request", "Not registered", "—"),
 ("GSS microdata catalog (extra)", "https://microdata.statsghana.gov.gh", "QLFS 2025 (132); AHIES 2022–24 (128)", "Not registered", "—"),
 ("NISR microdata (extra)", "https://microdata.statistics.gov.rw", "LFS 2025 (125)", "Not registered", "—"),
 ("NBS Tanzania TNADA (extra)", "https://microdata.nbs.go.tz", "ILFS 2025 (65)", "Not registered", "—"),
 ("INE Moçambique (formal request)", "https://mozdata.ine.gov.mz", "IOF 2022 (79)", "Request not lodged", "—"),
 ("ESS Ethiopia (formal request)", "https://ess.gov.et", "NIHS 2024/25 labour module", "Request not lodged", "—"),
 ("NSO Malawi (formal request)", "https://nsomalawi.mw", "LFS 2024", "Request not lodged", "—"),
]
for x in regs:
    rg.append(list(x))
for c in rg[1]:
    c.font = Font(bold=True, color="FFFFFF"); c.fill = hdr
for i, w in enumerate([32, 40, 50, 20, 34], 1):
    rg.column_dimensions[get_column_letter(i)].width = w
for row in rg.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical="top")

wb.save(OUT)
print("rows:", len(R))
