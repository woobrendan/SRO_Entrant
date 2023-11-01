# Take in answers array from fetched response

def process_answers(answers_arr):
    entry = {
        'Team': answers_arr[0]['text'],
        'Season Type': answers_arr[1]['choice']['label']
    }


def getAnswerValue(answer):
    if answer['type'] == 'text':
        return answer['text']
