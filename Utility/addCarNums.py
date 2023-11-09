def addCarNums(wb, series, all_entries):
    entries = {}

    if series == 'SRO':
        entries['GT Nums'] = []
        entries['TC Nums'] = []
    else:
        entries['GR Nums'] = []

    for entry in all_entries:
        if series == 'GR':
            entries['GR Nums'].append(entry)

        elif entry['Series'] == 'TC America':
            entries['TC Nums'].append(entry)

        else:
            entries['GT Nums'].append(entry)
