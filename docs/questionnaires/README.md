# Questionnaires

Survey instruments downloaded from the World Bank Microdata Library on 9 Nov 2026 using
`scripts/wb_mdl_download.py`. Use them to map variables to questions before harmonising.

| Folder | Survey | Contents |
|---|---|---|
| `EHCVM-2_2021/<ISO3>/` | EHCVM-2 2021/22, 8 WAEMU states | Household questionnaire, wave 1 and wave 2 (`*_vague1.pdf`, `*_vague2.pdf`); BFA also has the community questionnaire |
| `EHCVM-P_2021/BFA/` | Burkina Faso EHCVM panel 2021/22 (v05) | Household questionnaire waves 1–2, community questionnaire |
| `MWI_IHS6_2024-25/` | Malawi IHS6 2024/25 | Household, agriculture, fisheries and community questionnaires |

The employment section of the EHCVM household questionnaire is **Section 4** (data files
`s04a_me`–`s04c_me`). The IHS6 labour module is **Module E** (`hh_mod_e`).

Enumerator manuals, classification lists (ISIC/ISCO-type nomenclatures), basic
information documents and survey reports are kept with the data under
`data/raw/<dataset>/documentation/`.

To refresh or add instruments:

```bash
python scripts/wb_mdl_download.py <IDNO> --type doc/qst --dest docs/questionnaires/<folder>
```
