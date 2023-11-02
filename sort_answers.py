def getAnswerValue(answer):
    ans_type = answer['type']

    if ans_type == 'choice':
        return answer['choice']['label']

    if ans_type == 'boolean':
        return 'Yes' if answer['boolean'] else 'No'

    # phone, email, text
    return answer[ans_type]


# Take in answers array from fetched response

def process_answers(answers):
    entry = {
        'Team': getAnswerValue(answers[0]),
        'Season Type': getAnswerValue(answers[1]),
        'Entrant License Name': getAnswerValue(answers[2]),
        'Primary Contact': f'{getAnswerValue(answers[3])} + {getAnswerValue(answers[4])}',
        'Team Contact Phone Number': getAnswerValue(answers[5]),
        'Primary Email': getAnswerValue(answers[6]),
        'Street Address': getAnswerValue(answers[7]),
        'City': getAnswerValue(answers[8]),
        'State': getAnswerValue(answers[9]),
        'Zip/Postal': getAnswerValue(answers[10]),
        'Country': getAnswerValue(answers[11]),
        'isShipping': getAnswerValue(answers[12]),
    }

    if not answers[12]['boolean']:
        shipping = {
            'Shipping Address': getAnswerValue(answers[13]),
            'Shipping City': getAnswerValue(answers[14]),
            'Shipping State': getAnswerValue(answers[15]),
            'Shipping Zip': getAnswerValue(answers[16]),
            'Shipping Country': getAnswerValue(answers[17]),
        }

        entry.update(shipping)
    else:
        vehicle = {

        }
