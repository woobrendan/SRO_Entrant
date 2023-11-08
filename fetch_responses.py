from dotenv import load_dotenv
import requests
import os

load_dotenv()

page_size = f'?page_size=100'


def fetch_responses(date_str, series):
    form_str = 'GR_FORM' if series == 'GR' else 'SRO_FORM'
    form_id = os.environ.get(form_str)
    token = os.environ.get('TOKEN')

    url = f'https://api.typeform.com/forms/{form_id}/responses?since={date_str}'
    # url = f'https://api.typeform.com/forms/{form_id}/responses'

    headers = {
        'Authorization': f'Bearer {token}'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print('Error fetching TypeForm responses', response.status_code)


if __name__ == '__main__':

    # fetch GR
    gr_date = '2023-11-02T20:29:32Z'
    fetch_responses(date_str=gr_date, series='GR')

    # fetch SRO
    # sro_date = '2023-11-01T22:31:49Z'
    # fetch_responses(sro_date, series=None)
