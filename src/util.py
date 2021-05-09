"""
Util.py is a python module to provide common methods like accessing the api and returning the response
data source : https://www.football-data.org/
"""
import os
import requests
import json
from dotenv import load_dotenv

# loading the environment variables
load_dotenv()
# Bot Auth Token
FOOTY_BOT_TOKEN = os.getenv("FOOTY_BOT_TOKEN")
# football API token
API_TOKEN = os.getenv("API_TOKEN")
# football API org
API_ORG = os.getenv("API_ORG")


HEADERS = {'X-Auth-Token': API_TOKEN}


def get_data_from_api(url_suffix: str):
    """
    Method to load the data from api
    """
    url = f"{API_ORG}{url_suffix}"
    response = requests.get(url,headers=HEADERS)
    json_data = response.json()
    return json_data


class ApiUtil:
    """

    """
    def __init__(self):
        """

        """
        self.base_url = API_ORG





