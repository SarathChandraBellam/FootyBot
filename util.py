"""
Util.py is a python module to provide common methods like accessing the api and returning the response
data source : https://www.football-data.org/
"""
import requests
from http import client
from footybot import API_ORG, API_TOKEN


def get_football_api(url, token):
    """
    Method to load the data from api
    :param url: Api Endpoint
    :param token: token to access the api
    :return: API response
    """
    response = requests.get(url)
    json_data = response.json()
    return json_data
