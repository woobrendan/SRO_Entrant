import openpyxl
from datetime import datetime
from Utility.fetch_responses import fetch_responses
from Utility.answersToDict import processAllResponses
from Utility.sortFuncs import filterEntriesById
from Utility.utility import getAllId, getMostRecentDate, addValuesToExcel
from Utility.addCarNums import addCarNums
from Utility import headers, gr_headers


def addEntriesToExcel(series):
    excel_doc = 'GR Cup' if series == 'GR' else 'SRO'
    current_year = datetime.now().year

    wb = openpyxl.load_workbook(f'./2025/ 2025 {excel_doc} Vehicle Registrations.xlsx')


    # wb = openpyxl.load_workbook(
    #     f'../2024 {excel_doc} Vehicle Registrations.xlsx')

    sheet = wb['Car Registrations']

    recent_date = getMostRecentDate(sheet, series)
    existing_ids = getAllId(sheet, series)

    # Fetch respones exit if no new respones, if responses process them to own dict, then filter removing duplicate ids
    entries = fetch_responses(recent_date, series)

    if len(entries) == 0:
        return

    all_entries = processAllResponses(entries, series)
    filtered_entries = filterEntriesById(existing_ids, all_entries)

    # with filtered entries, process to add to car reg, and number tracking
    header_title = gr_headers.headers if series == 'GR' else headers.headers

    count = addValuesToExcel(header_title, filtered_entries, sheet)
    addCarNums(wb, series, filtered_entries)

    print(f'{count} entries have been added to {excel_doc} document')

    wb.save(f'../2024 {excel_doc} Vehicle Registrations Latest.xlsx')


if __name__ == '__main__':
    # fetch GR
    addEntriesToExcel(series='GR')

    # fetch SRO
    addEntriesToExcel(series='SRO')
