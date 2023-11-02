from sort_answers import getAnswerValue

headers = {
    "CI2u1enwoqbZ": 'Team',
    '1rK745G7gN0S': 'Season Type',
    'FhYKXAVPkzaa': 'Entrant License Name',
    '6r2CqolmpepU': 'Primary Contact First Name',
    '4kIVm0yJCqFq': 'Primary Contact Last Name',
    '9OF0lWZEpNuR': 'Primary Phone Number',
    'xK89Tz19ICpG': 'Primary Email'

}


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
