from dotenv import load_dotenv
import requests
import os

load_dotenv()

page_size = f'?page_size=100'


def fetch_responses(date_str, series):
    form_str = 'GR_FORM' if series == 'GR' else 'SRO_FORM'
    form_id = os.environ.get(form_str)
    token = os.environ.get('TOKEN')
    sro_form_str = os.environ.get('SRO_2025')

    # url = f'https://api.typeform.com/forms/{sro_form_str}/responses?since={date_str}'
    url = f'https://api.typeform.com/forms/{sro_form_str}/responses'

    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data['total_items'] == 0:
            print(
                f'Fetch successful, no new entries from {form_str} since given date')

        return data['items']
    else:
        print('Error fetching TypeForm responses', response.status_code)
