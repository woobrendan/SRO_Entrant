def getAnswerValue(answer):
    ans_type = answer['type']

    if ans_type == 'choice':
        return answer['choice']['label']

    if ans_type == 'boolean':
        return 'Yes' if answer['boolean'] else 'No'

    # phone, email, text, number
    return answer[ans_type]
