from Utility.gr_headers import num_headers
from Utility.sortFuncs import sortEntryNumberTracking
from Utility.utility import findFirstEmptyRow, copy_alignment, copy_border, copy_font


def addCarNums(wb, series, all_entries):
    entryDict = sortEntryNumberTracking(series, all_entries)

    if series == 'GR':
        sheet = wb['GR Nums']

        entries = entryDict['GR Nums']

        first_empty_row = findFirstEmptyRow(sheet)
        first_cell = sheet.cell(row=2, column=1)

        for entry in entries:
            for i, header in enumerate(num_headers, start=1):
                new_cell = sheet.cell(row=first_empty_row, column=i)
                new_cell.value = entry.get(header, '')

                # set formatting of cell
                new_cell.font = copy_font(first_cell.font)
                new_cell.alignment = copy_alignment(first_cell.alignment)
                new_cell.border = copy_border(first_cell.border)

            first_empty_row += 1
