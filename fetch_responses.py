from dotenv import load_dotenv
import requests
import os

load_dotenv()

form_id = os.environ.get('FORM')
token = os.environ.get('TOKEN')

url = f'https://api.typeform.com/forms/{form_id}/responses'

headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(response.status_code)
