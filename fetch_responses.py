from dotenv import load_dotenv
import requests
import os

load_dotenv()

# Last upload - update with each get
date = '2023-11-07T22:17:09.613Z'

date_str = f'?since={date}'
page_size = f'?page_size=100'


def fetch_responses():
    form_id = os.environ.get('FORM')
    token = os.environ.get('TOKEN')

    url = f'https://api.typeform.com/forms/{form_id}/responses{date_str}'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print('Error fetching TypeForm responses', response.status_code)
