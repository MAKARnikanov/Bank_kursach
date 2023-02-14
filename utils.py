import requests
from pprint import pprint
def get_data(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.json(), "INFO: Данные получены успешно"
    except requests.exceptions.ConnectionError():
        return None, "ERROR: requests.exceptions.ConnectionError"
    except requests.exceptions.JSONDecodeError():
        return None, "ERROR: requests.exceptions.JSONDecodeError"

