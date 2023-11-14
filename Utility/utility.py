from datetime import datetime, timedelta
import openpyxl


def copy_font(font):
    new_font = openpyxl.styles.Font(
        name=font.name, sz=font.sz, b=font.b, color=font.color)
    return new_font


def copy_alignment(align):
    new_align = openpyxl.styles.Alignment(
        horizontal=align.horizontal, vertical=align.vertical)
    return new_align


def copy_border(border):
    new_border = openpyxl.styles.Border(
        left=border.left, right=border.right, top=border.top, bottom=border.bottom
    )
    return new_border


def findFirstEmptyRow(sheet):
    for cell in sheet["A"]:
        if cell.value is None:
            return cell.row


def getAllId(sheet, series):
    ids = []

    column_id = 'BM' if series == 'SRO' else 'AZ'

    column = sheet[column_id]

    for cell in column[1:]:
        if cell.value is not None:
            ids.append(cell.value)
        else:
            break  # exit loop when cell is empty

    return ids


def getMostRecentDate(sheet, series):
    submit_dates = []

    column_id = 'BA' if series == 'GR' else 'BN'

    column = sheet[column_id]

    for cell in column[1:]:
        if cell.value is not None:
            submit_dates.append(cell.value)
        else:
            break

    # convert each date string into date obj, get max then return as str
    date_objs = [datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
                 for date in submit_dates]

    most_recent = max(date_objs)

    most_recent += timedelta(seconds=1)

    return most_recent.strftime('%Y-%m-%dT%H:%M:%SZ')


def addValuesToExcel(headers, entries, sheet):
    first_row = findFirstEmptyRow(sheet)
    first_cell = sheet.cell(row=2, column=1)
    count = 0

    for entry in entries:
        count += 1

        for i, header in enumerate(headers, start=1):
            new_cell = sheet.cell(row=first_row, column=i)
            val = entry.get(header, '')

            if header in ['Car # First Choice',  'Car # Second Choice', 'Car # Third Choice']:
                val = int(val)

            new_cell.value = val

            # set formatting of cell
            new_cell.font = copy_font(first_cell.font)
            new_cell.alignment = copy_alignment(first_cell.alignment)
            new_cell.border = copy_border(first_cell.border)

        first_row += 1

    return count
