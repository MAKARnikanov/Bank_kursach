import requests
from pprint import pprint
def get_data(url):
    response = requests.get(url).json()
    pprint(response)
