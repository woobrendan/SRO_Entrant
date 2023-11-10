from Utility.utility import findFirstEmptyRow, copy_alignment, copy_border, copy_font
from Utility import headers, gr_headers


def addToSheet(sheet, series, all_entries):
    # add filter to check if entry id exists in the sheet already
    first_empty_row = findFirstEmptyRow(sheet)
    first_cell = sheet.cell(row=2, column=1)

    header_title = gr_headers.headers if series == 'GR' else headers.headers

    count = 0

    for entry in all_entries:
        count += 1

        for i, header in enumerate(header_title, start=1):
            new_cell = sheet.cell(row=first_empty_row, column=i)
            new_cell.value = entry.get(header, '')

            # set formatting of cell
            new_cell.font = copy_font(first_cell.font)
            new_cell.alignment = copy_alignment(first_cell.alignment)
            new_cell.border = copy_border(first_cell.border)

        first_empty_row += 1

    return count
