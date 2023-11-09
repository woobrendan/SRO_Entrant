import openpyxl
from Utility.fetch_responses import fetch_responses
from Utility.answersToDict import processAllResponses
from Utility.addToSheet import addToSheet


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

    count = addToSheet(sheet, series, all_entries)
    print(f'{count} entries have been added to {excel_doc} document')

    wb.save(f'./Updated/2024 {excel_doc} Vehicle Registrations Out.xlsx')


if __name__ == '__main__':

    # fetch GR
    gr_date = '2023-11-07T18:05:04Z'
    addEntriesToExcel(date_str=gr_date, series='GR')

    # fetch SRO
    sro_date = '2023-10-07T18:11:35Z'
    addEntriesToExcel(sro_date, series='SRO')
