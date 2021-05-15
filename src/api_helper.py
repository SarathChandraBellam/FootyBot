"""
Module to use util and create json of API data
"""
import json
import os
from util import get_data_from_api, create_file, DATA_PATH, load_json


def create_competitions_json():
    """
    Get the competitions data from football API and format it.
    @return: None
    """
    data = get_data_from_api("competitions")
    print(data)
    countries = ["England", "Spain", "Germany", "France", "Italy", "Portugal", "Europe", "World"]
    res = []
    for each in data["competitions"]:
        if each["area"]["name"] in countries:
            print(each)
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
        print(each_comp["competition"])
        suffix = f"competitions/{id}/teams"
        data = get_data_from_api(suffix)
        print(data)
        if not "errorCode" in data:
            teams = data["teams"]
            params = ["id", "name", "shortName", "crestUrl", "tla", "website"]
            for team in teams:
                print(team["name"], team["tla"])
                team_data = {param: team[param] for param in params}
                team_data["competition_name"] = data["competition"]["name"]
                team_data["competition_code"] = data["competition"]["code"]
                team_data["area"] = data["competition"]["area"]["name"]
                res.append(team_data)
    create_file(res, "teams")


def generate_league_team_codes():
    with open(os.path.join(DATA_PATH, "teams.json"), "r") as json_read:
        competitions = json.load(json_read)

    leagues = ["Premier League", "UEFA Champions League", "Ligue 1", "Bundesliga", "Serie A", "Primera Division"]
    res = {}
    for league in leagues:
        temp = {}
        x = [y for y in competitions if y["competition_name"] == league]
        for each in x:
            temp[each["shortName"]] = each["tla"]
        res[league] = temp
    print(res)


def generate_countries_team_codes():
    with open(os.path.join(DATA_PATH, "teams.json"), "r") as json_read:
        competitions = json.load(json_read)

    countries = ["England", "Spain", "Italy", "Germany", "France", "Europe"]
    res = {}
    for area in countries:
        temp = {}
        x = [y for y in competitions if y["area"] == area]
        for each in x:
            temp[each["shortName"]] = each["tla"]
        res[area] = temp
    print(res)

#
# # create_competitions_json()
# # create_teams_json()
# data = load_json(os.path.join(DATA_PATH, "teams.json"))
# res = []
# check = []
# team_map = {}
# for each in data:
#     if not each["name"] in check:
#         res.append(each)
#         team_map[each["name"]] = each["tla"]
#         check.append(each["name"])
# print(team_map)






