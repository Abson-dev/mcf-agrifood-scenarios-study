"""Build the source-matrix workbook from the CSV files in ``metadata/``.

The CSV files are the single source of truth: edit them, then run

    python scripts/build_source_matrix.py

to regenerate ``registers/source_matrix.xlsx`` (the Phase 2 registers, Sheet 3
working copy). Pass ``--out PATH`` to write elsewhere.
"""

from __future__ import annotations

import argparse
import csv
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
META = ROOT / "metadata"
DEFAULT_OUT = ROOT / "registers" / "source_matrix.xlsx"

HEADER_FILL = PatternFill("solid", fgColor="1F3864")
FLAG_FILL = PatternFill("solid", fgColor="FFF2CC")
THIN = Side(style="thin", color="BFBFBF")
BORDER = Border(top=THIN, bottom=THIN, left=THIN, right=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")

SOURCE_WIDTHS = [13, 12, 34, 22, 34, 14, 26, 30, 34, 28, 36, 22, 50, 44, 20, 40]
FLAG_WIDTHS = [4, 16, 40, 48, 44, 44]
PORTAL_WIDTHS = [32, 40, 50, 20, 34]


def read_csv(name: str) -> list[list[str]]:
    with open(META / name, newline="", encoding="utf-8") as f:
        return list(csv.reader(f))


def style_header(row) -> None:
    for cell in row:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = HEADER_FILL
        cell.alignment = Alignment(wrap_text=True, vertical="center")


def set_widths(ws, widths: list[int]) -> None:
    for i, width in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = width


def add_table(ws, rows: list[list[str]], header_row: int, widths: list[int]) -> None:
    for row in rows:
        ws.append(row)
    style_header(ws[header_row])
    set_widths(ws, widths)
    for row in ws.iter_rows(min_row=header_row + 1, max_row=ws.max_row):
        for cell in row:
            cell.alignment = WRAP
            cell.border = BORDER
    last_col = get_column_letter(len(rows[0]))
    ws.auto_filter.ref = f"A{header_row}:{last_col}{ws.max_row}"


def build(out: Path) -> None:
    wb = Workbook()

    ws = wb.active
    ws.title = "Source matrix"
    ws.append(["Source matrix — working copy for Phase 2 registers, Sheet 3"])
    ws.append([
        f"Generated {date.today():%d %b %Y} from metadata/sources.csv. "
        "'Previous round' rows are kept for reference only and are not substitutes."
    ])
    ws["A1"].font = Font(bold=True, size=13)
    ws["A2"].font = Font(italic=True, color="595959")
    sources = read_csv("sources.csv")
    add_table(ws, sources, header_row=3, widths=SOURCE_WIDTHS)
    flag_col = sources[0].index("Flag for John") + 1
    for row in ws.iter_rows(min_row=4, max_row=ws.max_row):
        if row[flag_col - 1].value:
            row[flag_col - 1].fill = FLAG_FILL
    ws.freeze_panes = "D4"

    add_table(wb.create_sheet("Flags for John"), read_csv("flags.csv"), 1, FLAG_WIDTHS)
    add_table(wb.create_sheet("Accounts & downloads"), read_csv("portals.csv"), 1, PORTAL_WIDTHS)

    out.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out)
    print(f"Wrote {out} ({len(sources) - 1} sources)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT, help="output .xlsx path")
    build(parser.parse_args().out)


if __name__ == "__main__":
    main()
