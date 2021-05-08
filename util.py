"""
Util.py is a python module to provide common methods like accessing the api and returning the response
data source : https://www.football-data.org/
"""
import requests
from http import client
import json
#from footybot import logger
#from footybot import API_ORG, API_TOKEN

url = 'https://api.football-data.org/v2/competitions/BL1'
token = 'f8bc1470c34c47388c38ffb20a59a393'
headers = { 'X-Auth-Token': 'f8bc1470c34c47388c38ffb20a59a393' }

def get_football_api(url, token):
    """
    Method to load the data from api
    :param url: Api Endpoint
    :param token: token to access the api
    :return: API response
    """
    response = requests.get(url,headers=headers)
    json_data = response.json()
    return json_data
print(get_football_api(url,token))
print("=======================================================")

class botData:
    def __init__(self):
        # self.logger = logger
        self.base_url = 'https://api.football-data.org/v2/'
        self.team = {}

    def get_team(self):
        url = "{}teams/86/matches?status=SCHEDULED".format(
            self.base_url)
        response = requests.request("GET", url,headers=headers)
        self.team = json.loads(response.text)
        print(self.team)
        # self.logger.error("Get team response body {}".format(self.team))

        return self.team

if __name__ == "__main__":
    obj = botData()
    obj.get_team()