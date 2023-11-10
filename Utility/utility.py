from datetime import datetime
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

    return most_recent.strftime('%Y-%m-%dT%H:%M:%SZ')
