from sort_answers import getAnswerValue
from headers import headers

# Process Individual Answer object


def process_answer(answer):
    ans_id = answer['field']['id']

    key = headers[ans_id]
    value = getAnswerValue(answer)

    return {key: value}


# Take in answers array from fetched response
def processAnswerById(answers):
    entry = {}

    for answer in answers:
        val = process_answer(answer)
        entry.update(val)
