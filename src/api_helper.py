"""
Module to use util and create json of API data
"""
import json
import os
from util import get_data_from_api


HOME_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(HOME_DIR, "data")


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


def create_competitions_json():
    """

    @return:
    """
    data = get_data_from_api("competitions")
    countries = ["England", "Spain", "Germany", "France", "Italy", "Portugal", "Europe", "World"]
    res = []
    for each in data["competitions"]:
        if each["area"]["name"] in countries:
            league_details = {"id": each["id"], "area": each["area"]["name"], "area_id": each["area"]["id"],
                              "area_code": each["area"]["countryCode"], "competition": each["name"],
                              "ensignUrl": each["area"]["ensignUrl"]}
            res.append(league_details)
    create_file(res, "competitions")


create_competitions_json()