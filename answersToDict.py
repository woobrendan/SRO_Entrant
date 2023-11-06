from Utility.sortFuncs import getAnswerValue
from Utility.headers import header_ids
from fetch_responses import fetch_responses
import json


# Process Individual Answer object
def process_answer(answer):
    ans_id = answer['field']['id']

    key = header_ids.get(ans_id, '----Find later------')
    value = getAnswerValue(answer)

    return {key: value}


# Take in answers array from fetched response. This is a single entrant report
def processAnswersToDict(response):
    entry = {}
    entry['id'] = response['response_id']
    entry['Submitted_at'] = response['submitted_at']
    entry['2024 Confirmed Number'] = ''

    for answer in response['answers']:
        val = process_answer(answer)
        entry.update(val)

    return entry


# pass in param of all newest responses and process all
def processAllResponses(responses):
    all_entries = []

    for response in responses:
        new_response = processAnswersToDict(response)
        all_entries.append(new_response)

    return all_entries


if __name__ == '__main__':
    entries = fetch_responses()
    all_entries = processAllResponses(entries)

    for team in all_entries:
        print('entry~~~', json.dumps(team, indent=4))
