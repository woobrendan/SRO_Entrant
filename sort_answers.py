def getAnswerValue(answer):
    ans_type = answer['type']
    if ans_type == 'text':
        return answer['text']

    if ans_type == 'choice':
        return answer['choice']['label']

    if ans_type == 'phone_number':
        return answer['phone_number']
    if ans_type == 'email':
        return answer['email']


# Take in answers array from fetched response

def process_answers(answers):
    entry = {
        'Team': getAnswerValue(answers[0]),
        'Season Type': getAnswerValue(answers[1]),
        'Entrant License Name': getAnswerValue(answers[2]),
        'Primary Contact': f'{getAnswerValue(answers[3])} + {getAnswerValue(answers[4])}',
        'Team Contact Phone Number': getAnswerValue(answers[5])
    }
