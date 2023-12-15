from dotenv import load_dotenv
import requests
import os

load_dotenv()

page_size = f'?page_size=100'


def fetch_responses_23(date_str, series):
    form_id = os.environ.get('FORM_23')
    token = os.environ.get('TOKEN')

    url = f'https://api.typeform.com/forms/{form_id}/responses?since=2023-11-15T22:04:43Z'

    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data['total_items'] == 0:
            print(
                f'Fetch successful, no new entries from SRO_23 since given date')

        return data['items']
    else:
        print('Error fetching TypeForm responses', response.status_code)
