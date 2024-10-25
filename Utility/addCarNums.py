from headers.gr_headers import gr_num_headers
from headers.headers import sro_num_headers
from headers.mcl_headers import mcl_num_headers
from Utility.sortFuncs import sortEntryNumberTracking
from Utility.utility import addValuesToExcel


def addCarNums(wb, series, all_entries):
    entryDict = sortEntryNumberTracking(series, all_entries)

    # handle SRO number tracking
    if series == 'SRO':
        for key, entries in entryDict.items():
            sheet = wb[key]

            addValuesToExcel(sro_num_headers, entries, sheet)
    
    # handle GR and McLaren Nums
    else:
        seriesTab = 'GR Nums' if series == 'GR Cup' else 'MCL Nums'
        num_head = gr_num_headers if series == 'Gr Cup' else mcl_num_headers
        sheet = wb[seriesTab]

        entries = entryDict[seriesTab]

        addValuesToExcel(num_head, entries, sheet)
