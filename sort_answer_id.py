from sort_answers import getAnswerValue
from headers import headers
from fetch_responses import fetch_responses
import json

# Process Individual Answer object


def process_answer(answer):
    ans_id = answer['field']['id']

    key = headers.get(ans_id, 'Find later')
    value = getAnswerValue(answer)

    return {key: value}


# Take in answers array from fetched response
def processAnswerById(answers):
    entry = {}

    for answer in answers:
        val = process_answer(answer)
        entry.update(val)

    return entry


if __name__ == '__main__':
    entries = fetch_responses()
    all_entries = []
    for entry in entries:
        new_entry = processAnswerById(entry['answers'])
        all_entries.append(new_entry)

    for team in all_entries:
        print('entry~~~', json.dumps(team, indent=4))
