import openpyxl
from fetch_responses import fetch_responses
from Utility.headers import headers
from answersToDict import processAllResponses
from Utility.utility import copy_alignment, copy_border, copy_font, findFirstEmptyRow

# Last upload - update with each get
date_str = '2023-11-07T22:17:09.613Z'


def addEntriesToExcel(series):
    excel_doc = 'GR Cup' if series == 'GR' else 'SRO'
    wb = openpyxl.load_workbook(
        f'.templates/2024 {excel_doc} Vehicle Registrations.xlsx')

    sheet = wb['Car Registrations']

    entries = fetch_responses(date_str, series=None)
    all_entries = processAllResponses(entries)

    # add filter to check if entry id exists in the sheet already
    first_empty_row = findFirstEmptyRow(sheet)
    first_cell = sheet.cell(row=2, column=1)

    for entry in all_entries:
        for i, header in enumerate(headers, start=1):
            new_cell = sheet.cell(row=first_empty_row, column=i)
            new_cell.value = entry.get(header, '')

            # set formatting of cell
            new_cell.font = copy_font(first_cell.font)
            new_cell.alignment = copy_alignment(first_cell.alignment)
            new_cell.border = copy_border(first_cell.border)

        first_empty_row += 1

    wb.save('./Updated/2024 SRO Vehicle Registrations Out.xlsx')


if __name__ == '__main__':
    addEntriesToExcel()
