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

    return entries


def unique_id(entry, id_list):
    return entry['id'] not in id_list


def filterEntriesById(id_list, all_entries):
    return list(filter(lambda entry: unique_id(entry, id_list), all_entries))
