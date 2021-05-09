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


def create_file(data, file_name):
    """
    Method to create a json file
    @param data: json data
    @param file_name: name of the json file
    @return: None, Creates a json in ./data folder
    """
    file_path = os.path.join(DATA_PATH, f"{file_name}.json")
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)


class ApiUtil:
    """

    """
    def __init__(self):
        """

        """
        self.base_url = API_ORG





