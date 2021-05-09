"""
Module to use util and create json of API data
"""
import json
import os
from util import get_data_from_api, create_file


HOME_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(HOME_DIR, "data")


def create_competitions_json():
    """
    Get the competitions data from football API and format it.
    @return: None
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


def create_teams_json():
    """
    Get the football teams data from football API and write it to a json file
    @return: None
    """
    with open(os.path.join(DATA_PATH, "competitions.json"), "r") as json_read:
        competitions = json.load(json_read)
    res = []
    for each_comp in competitions:
        id = each_comp["id"]
        suffix = f"competitions/{id}/teams"
        data = get_data_from_api(suffix)
        if not "errorCode" in data:

            teams = data["teams"]
            print(teams)
            params = ["id", "name", "shortName", "crestUrl", "tla", "website"]
            for team in teams:
                team_data = {param:team[param] for param in params}
                res.append(team_data)
    create_file(res, "teams")



# create_competitions_json()
# create_teams_json()
