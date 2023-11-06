import openpyxl
from fetch_responses import fetch_responses
from Utility.headers import headers
from answersToDict import processAllResponses
from Utility.utility import copy_alignment, copy_border, copy_font, findFirstEmptyRow


def addEntriesToExcel():
    wb = openpyxl.load_workbook('./2024 SRO Vehicle Registrations Test.xlsx')

    sheet = wb['Car Registrations']

    entries = fetch_responses()
    all_entries = processAllResponses(entries)

    # first_empty_row = sheet.max_row + 1
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
