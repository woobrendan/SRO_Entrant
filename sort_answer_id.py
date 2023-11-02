from sort_answers import getAnswerValue

headers = {
    "CI2u1enwoqbZ": 'Team',
    '1rK745G7gN0S': 'Season Type'
}


# Process Individual Answer object
def process_answer(answer):
    ans_id = answer['field']['id']

    key = headers[ans_id]
    value = getAnswerValue(answer)

    return {key: value}


# Take in answers array from fetched response
def processAnswerById(answers):
    pass
