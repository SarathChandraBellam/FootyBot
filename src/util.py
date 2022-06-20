"""
Util.py is a python module to provide common methods like accessing the api and returning the response
data source : https://www.football-data.org/
"""
import os
import requests
import discord
import json
from dateutil import tz
from datetime import  datetime
from datetime import timedelta
from dotenv import load_dotenv
from src.codes import TEAM_LONG_NAME_CODES

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


def load_json(file):
    """
    load the json file
    @param file:
    @return: json file data
    """
    with open(file, "r") as comp_file:
        data = json.load(comp_file)
    return data


def get_embed_from_file(file_name):
    """
    Read the title , desc and fields from json and embed it for discord
    @param file_name: file name of the embed type ( Ex:  to embed help, file_name = "help_embed.json")
    @return: embed data from the file
    """
    file_path = os.path.join(DATA_PATH, file_name)
    data = load_json(file_path)
    title = data["title"]
    desc = data["desc"]
    fields = data["fields"]
    return prepare_embed(title, desc, fields)


def prepare_embed(title, description, fields, color= 0x3498db):
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
    url = f"{API_ORG}{url_suffix}"
    response = requests.get(url,headers=HEADERS)
    json_data = response.json()
    return json_data


def utc_to_ist(utc_str):
    """

    :param utc_str:
    :return:
    """
    dt_utc = datetime.strptime(utc_str, "%Y-%m-%dT%H:%M:%SZ")
    itc_time = dt_utc + timedelta(minutes=330)
    return itc_time.strftime("%Y/%m/%d %H:%M")


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


def format_data_into_table(resp):
    """

    @param resp:
    @return:
    """
    standings_format = '```\nLEAGUE: ' + str(resp['competition']['name']) + \
             ' ' * (45 - 2 - 8 - 10 - len(str(resp['competition']['name']))) + \
             'MATCHDAY: ' + str(resp['season']['currentMatchday']) + '\n'
    standings_format += '╔════╤══════╤════╤════╤════╤════╤═════╤═════╗\n'
    standings_format += '║ SN │ TEAM │ M  │ W  │ D  │ L  │ PTS │ GD  ║\n'
    standings_format += '╠════╪══════╪════╪════╪════╪════╪═════╪═════╣\n'
    for team in resp['standings'][0]['table']:
        text = '║ %-2d │ %-4s │ %-2d │ %-2d │ %-2d │ %-2d │ %-3d │ %+-3d ║\n' \
               % (team['position'], TEAM_LONG_NAME_CODES.get(team['team']['name'], team['team']['name'][:4])[:4], team['playedGames'],
                  team['won'],
                  team['draw'], team['lost'], team['points'], team['goalDifference'])
        standings_format += text


    standings_format += '╚════╧══════╧════╧════╧════╧════╧═════╧═════╝```'
    return standings_format








