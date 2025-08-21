from dotenv import load_dotenv
import requests
import os

load_dotenv()

page_size = f'?page_size=100'


def fetch_responses_2026(date_str, series):

    form_ids = {
        'SRO': 'SRO_2026',
        # 'GR Cup': 'GR_FORM',
        # 'McLaren': 'MCLAREN',
    }

    form_str = form_ids.get(series)
    form_id = os.environ.get(form_str)
    token = os.environ.get('TOKEN')

    dateUrl = f'https://api.typeform.com/forms/{form_id}/responses?since={date_str}'
    url = f'https://api.typeform.com/forms/{form_id}/responses'

    usableURL = dateUrl if date_str else url

    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(usableURL, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data['total_items'] == 0:
            print(
                f'Fetch successful, no new entries from {form_str} since given date')

        return data['items']
    else:
        print('Error fetching TypeForm responses', response.status_code)
