from Utility.gr_headers import num_headers
from Utility.headers import sro_num_headers
from Utility.sortFuncs import sortEntryNumberTracking
from Utility.utility import addValuesToExcel


def addCarNums(wb, series, all_entries):
    entryDict = sortEntryNumberTracking(series, all_entries)

    if series == 'GR':
        sheet = wb['GR Nums']

        entries = entryDict['GR Nums']

        addValuesToExcel(num_headers, entries, sheet)

    # handle SRO number tracking
    else:
        for key, entries in entryDict.items():
            sheet = wb[key]

            addValuesToExcel(sro_num_headers, entries, sheet)
