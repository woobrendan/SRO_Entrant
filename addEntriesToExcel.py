import openpyxl
from datetime import datetime
from Utility.fetch_responses import fetch_responses
from Utility.answersToDict import processAllResponses
from Utility.sortFuncs import filterEntriesById
from Utility.utility import getAllId, getMostRecentDate, addValuesToExcel
from Utility.addCarNums import addCarNums
from headers import gr_headers, headers, mcl_headers


def addEntriesToExcel():
    seriesList = ['SRO', "GR Cup", "McLaren"] # add in McLaren
    wb = openpyxl.load_workbook(f'../2025/2025 Vehicle Registrations.xlsx')
    running_count = 0

    for series in seriesList:
        sheet = wb[series]

        # Fetch respones exit if no new respones, if responses process them to own dict, then filter removing duplicate ids
        recent_date = getMostRecentDate(sheet, series, '2025')
        entries = fetch_responses(recent_date, series)

        if len(entries) == 0:
            continue

        # Take all entries, covnert answers to dicts, filter
        all_entries = processAllResponses(entries, series, '2025')
        existing_ids = getAllId(sheet, series, '2025')
        filtered_entries = filterEntriesById(existing_ids, all_entries)


        #### Handle Numbers Tabs######

        # with filtered entries, process to add to car reg, and number tracking
        if series == 'GR Cup':
            header_title = gr_headers.headers
        elif series == 'McLaren':
            header_title = mcl_headers.headers
        else:
            header_title = headers.headers

        count = addValuesToExcel(header_title, filtered_entries, sheet)
        running_count += count
        addCarNums(wb, series, filtered_entries)

        print(f'{count} entries have been added to {series} document')
        
    if running_count:
        wb.save(f'../2025/2025 Vehicle Registrations Latest.xlsx')


if __name__ == '__main__':
    addEntriesToExcel()
