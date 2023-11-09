import openpyxl
from fetch_responses import fetch_responses
from Utility import headers, gr_headers
from answersToDict import processAllResponses
from Utility.utility import copy_alignment, copy_border, copy_font, findFirstEmptyRow, getAllId


def addEntriesToExcel(date_str, series):
    excel_doc = 'GR Cup' if series == 'GR' else 'SRO'
    wb = openpyxl.load_workbook(
        f'./templates/2024 {excel_doc} Vehicle Registrations.xlsx')

    sheet = wb['Car Registrations']

    # Fetch respones exit if no new respones, if responses process them to own dict
    entries = fetch_responses(date_str, series)
    if len(entries) == 0:
        return
    all_entries = processAllResponses(entries, series)

    # add filter to check if entry id exists in the sheet already
    first_empty_row = findFirstEmptyRow(sheet)
    first_cell = sheet.cell(row=2, column=1)

    header_title = gr_headers.headers if series == 'GR' else headers.headers
    existing_ids = getAllId(sheet, series)

    for entry in all_entries:
        if entry['id'] in existing_ids:
            continue
        for i, header in enumerate(header_title, start=1):
            new_cell = sheet.cell(row=first_empty_row, column=i)
            new_cell.value = entry.get(header, '')

            # set formatting of cell
            new_cell.font = copy_font(first_cell.font)
            new_cell.alignment = copy_alignment(first_cell.alignment)
            new_cell.border = copy_border(first_cell.border)

        first_empty_row += 1

    wb.save(f'./Updated/2024 {excel_doc} Vehicle Registrations Out.xlsx')


if __name__ == '__main__':

    # fetch GR
    gr_date = '2023-11-07T18:05:04Z'
    addEntriesToExcel(date_str=gr_date, series='GR')

    # fetch SRO
    sro_date = '2023-11-07T18:11:35Z'
    addEntriesToExcel(sro_date, series='SRO')
