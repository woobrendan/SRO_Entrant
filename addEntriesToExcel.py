import openpyxl
from fetch_responses import fetch_responses


def addEntriesToExcel():
    wb = openpyxl.load_workbook('./2024 SRO Vehicle Registrations Test.xlsx')

    sheet = wb['Car Registrations']

    entries = fetch_responses()

    max_row = sheet.max_row + 1

    sheet.cell(row=max_row, column=1, value='Hello')

    wb.save('./Updated/2024 SRO Vehicle Registrations Out.xlsx')


if __name__ == '__main__':
    addEntriesToExcel()
