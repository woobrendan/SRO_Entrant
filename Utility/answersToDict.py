from Utility.sortFuncs import getAnswerValue
from headers import gr_headers, headers, mcl_headers, headers_2026
from Utility.fetch_responses import fetch_responses
import json

# Process Individual Answer object
def process_answer(answer, series, year):
    ans_id = answer['field']['id']

    #update for 2026 when year changes
    series_headers = {
        "GR Cup": {"2025": gr_headers.header_ids, "2026": gr_headers.header_ids},
        "McLaren": {"2025": mcl_headers.header_ids, "2026": mcl_headers.header_ids},
        "SRO": {"2025": headers.header_ids, "2026": headers_2026.header_ids}
    }

    if series == 'GR Cup':
        header_vals = gr_headers.header_ids
    elif series == 'McLaren':
        header_vals = mcl_headers.header_ids
    else:
        header_vals = headers.header_ids    

    key = header_vals.get(ans_id, '----Find later------')
    year_key = year if year == "2026" else "2025"
    all_headers = series_headers[series][year_key]
    key = all_headers.get(ans_id, '----Find later------')
    value = getAnswerValue(answer)

    return {key: value}


# Take in answers array from fetched response. This is a single entrant report
def processAnswersToDict(response, series, year):
    entry = {}
    entry['id'] = response['response_id']
    entry['Submitted_at'] = response['submitted_at']
    entry['2025 Confirmed Number'] = ''

    for answer in response['answers']:
        val = process_answer(answer, series, year)
        entry.update(val)

    return entry


# pass in param of all newest responses and process all
def processAllResponses(responses, series, year):
    all_entries = []

    for response in responses:
        new_response = processAnswersToDict(response, series, year)
        all_entries.append(new_response)

    return all_entries


if __name__ == '__main__':
    entries = fetch_responses()
    all_entries = processAllResponses(entries)

    for team in all_entries:
        print('entry~~~', json.dumps(team, indent=4))
