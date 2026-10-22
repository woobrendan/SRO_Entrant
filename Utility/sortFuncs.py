def getAnswerValue(answer):
    ans_type = answer['type']

    if ans_type == 'choice':
        return answer['choice']['label']

    if ans_type == 'boolean':
        return 'Yes' if answer['boolean'] else 'No'

    # phone, email, text, number
    return answer[ans_type]


# takes in array of proccessed entries, sorts for number tracking
def sortEntryNumberTracking(series, all_entries):

    ## Create key in entries object for each series numbers, fetch appropriate series based on prop
    entries = {
        "SRO": {'GT Nums': [], 'TC Nums': []},
        'GR Cup': {'GR Nums': []},
        'McLaren': {"MCL Nums": []}
    }.get(series, {})

    ## loop through the entry array and place numbers in approproate series
    for entry in all_entries:
        if series == 'GR Cup':
            entries['GR Nums'].append(entry)

        elif series == 'McLaren':
            entries['MCL Nums'].append(entry)

        elif series == 'SRO':
            if entry.get('Series') == 'TC America': 
                entries['TC Nums'].append(entry)

            else:
                entries['GT Nums'].append(entry)

    return entries


def unique_id(entry, id_list):
    return entry['id'] not in id_list


def filterEntriesById(id_list, all_entries):
    return list(filter(lambda entry: unique_id(entry, id_list), all_entries))
