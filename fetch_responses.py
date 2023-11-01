from dotenv import load_dotenv
import requests
import os

load_dotenv()

# Last upload - update with each get
date = '2023-11-01T19:13:49.643Z'

date_str = f'?since={date}'
page_size = f'?page_size=100'


def fetch_responses():
    form_id = os.environ.get('FORM')
    token = os.environ.get('TOKEN')

    url = f'https://api.typeform.com/forms/{form_id}/responses'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print('Error fetching TypeForm responses', response.status_code)
