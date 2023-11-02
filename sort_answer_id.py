from sort_answers import getAnswerValue

headers = {
    "CI2u1enwoqbZ": 'Team',
    '1rK745G7gN0S': 'Season Type',
    'FhYKXAVPkzaa': 'Entrant License Name',
    '6r2CqolmpepU': 'Primary Contact First Name',
    '4kIVm0yJCqFq': 'Primary Contact Last Name',
    '9OF0lWZEpNuR': 'Primary Phone Number',
    'xK89Tz19ICpG': 'Primary Email',
    'EfGE75l0Boh7': 'Street Address',
    '5MpSspTvu4g1': 'City',
    'nx7RCtskler7': 'State',
    'UAadJT7CwKOT': 'Zip/Postal',
    'PDYzPKydUlta': 'Country',
    'VWorxkTstwgd': 'is Shipping Address?',
    '5RrYGTeKRdXg': 'Vehicle Model Year',
    'IMEA0t0c9kyQ': 'Vehicle Make',
    'ASWurX5GTtnv': 'Vehicle Model',
    'Bw8p4QECsDvD': 'Series',
    'qpIxQJlGsU8a': 'Class',
    'zgosMYsLCGMP': '2023 Registered Number',
    'e1R9xecDplrr': 'Car # First Choice',
    'qx4hoS0Vg3qp': 'Car # Second Choice',
    'Or4qETiPiW1s': 'Car # Third Choice',
    'l3XaoUZhURCO': 'Driver 1 First Name',  # double check this id later
    'kkdqAVRNWpxC': 'Driver 1 Last Name',
    'y3Y4IBZhU0Iv': 'Driver 1 Nationality',
    'XAgm4jYd0AKO': 'Driver 1 Hometown',
    'uorVE07hxoDO': 'Driver 1 Country',
    'LAmMqTDTQ1l0': 'Driver 1 Email'
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
