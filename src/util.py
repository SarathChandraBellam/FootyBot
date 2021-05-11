"""
Util.py is a python module to provide common methods like accessing the api and returning the response
data source : https://www.football-data.org/
"""
import os
import requests
import discord
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
HOME_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(HOME_DIR, "data")


def get_embed(title, description, fields, color=0xf58300):
    """
    Method to embed the fields data
    @param title: Title of the Embed
    @param description: Description of the embed
    @param fields: fields to be embed; list of fields where names are-
                Mandatory : Name, value
                Optional: binary format(\n\u200b, default is "", inline(True/False; default is True)
    [{"name": ":one: Laliga", "value": "SPA", "binary_format"=""}, "name": ":one: Bundesliga", "value": "BA", "binary_format"=""}]
    @param color: font color
    @return: Embed data
    """
    embed = discord.Embed(title=title, description=description, color=color)
    for field in fields:
        binary_format = field.get("binary_format", "")
        inline_ = field.get("inline", True)
        embed.add_field(name=field["name"], value=field["value"] + binary_format, inline=inline_)
    return embed


def get_data_from_api(url_suffix: str):
    """
    Method to load the data from api
    @param url_suffix: API suffix (ex : for competitions , url_suffix is competitions
                       (ref: https://www.football-data.org/)
    @return: Api response data
    """
    print(url_suffix)
    url = f"{API_ORG}{url_suffix}"
    response = requests.get(url,headers=HEADERS)
    print(response)
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





