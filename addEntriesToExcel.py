import openpyxl
from fetch_responses import fetch_responses
from Utility.headers import headers
from answersToDict import processAllResponses


def addEntriesToExcel():
    wb = openpyxl.load_workbook('./2024 SRO Vehicle Registrations Test.xlsx')

    sheet = wb['Car Registrations']

    entries = fetch_responses()
    all_entries = processAllResponses(entries)

    first_empty_row = sheet.max_row + 1

    for entry in all_entries:
        for i, header in enumerate(headers, start=1):
            sheet.cell(row=first_empty_row, column=i,
                       value=entry.get(header, ''))

        first_empty_row += 1

    wb.save('./Updated/2024 SRO Vehicle Registrations Out.xlsx')


if __name__ == '__main__':
    addEntriesToExcel()
