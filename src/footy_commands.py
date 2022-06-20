""""
"""
import os
import discord
from src.util import load_json, DATA_PATH, prepare_embed, format_data_into_table, utc_to_ist
from src.codes import LEAGUE_TEAM_CODES, TOP_TEAM_CODES, LEAGUE_CODES, TEAM_LONG_NAME_CODES
from src.exception import InvalidLeagueCodeException
from src.api import get_standings, get_fixtures

TEAMS = load_json(os.path.join(DATA_PATH, "teams.json"))
COMPETITIONS = load_json(os.path.join(DATA_PATH, "competitions.json"))


def get_team_codes(league_code):
    """
    Prepare embed of league specific team codes
    @param league_code: league code ( ex: premier league : PL)
    @return: Embed with teams and their codes
    """

    try:
        if league_code is None:
            title = "Codes of Top Clubs"
            description = "Top Teams Codes. To display league wise team codes, use command '.tc <league_code>'"
            fields = []
            for tc in TOP_TEAM_CODES:
                for team in TEAMS:
                    if tc.upper() == team["tla"]:
                        fields.append({"name": f"{team['shortName']}",
                                       "value": tc, "binary_format": "\n\u200b"})
        else:
            league_teams = LEAGUE_TEAM_CODES.get(league_code.upper(), None)
            if league_teams is None:
                raise InvalidLeagueCodeException(f"League code {league_code} is invalid")
            title = f" Team codes of League - {league_code}"
            description = "League specific team codes"
            fields = [{"name": name, "value": value, "binary_format": "\n\u200b"} for name, value
                      in league_teams.items() if value is not None]
        embed = prepare_embed(title, description, fields)
    except InvalidLeagueCodeException as exp:
        embed = discord.Embed(title=f" Team codes of League - {league_code}", description=exp)
        print(exp)
    return embed


def get_league_standings(league_code):
    """
    Prepare embed of league specific table and standings
    @param league_code: league code ( ex: premier league : PL)
    @return: Embed with teams and table
    """
    try:
        league_id = LEAGUE_CODES.get(league_code.upper(),None)
        if league_id is None:
            raise InvalidLeagueCodeException(f"League code {league_code} is invalid")
        standings_data = get_standings(league_id)
        str_out = format_data_into_table(standings_data)
        return str_out
    except InvalidLeagueCodeException as exp:
        print(exp)
        return None


def format_league_fixtures(matches, match_day):
    """

    :param matches:
    :param match_day:
    :return:
    """
    res = []
    current_match_day = int(matches[0]["season"]["currentMatchday"]) if match_day is None else int(match_day)
    res_matches = [{"home": match["homeTeam"]["name"], "away": match["awayTeam"]["name"],
                    "timestamp": utc_to_ist(match["utcDate"]), "result": match["score"]}
                   for match in matches if match["matchday"] == current_match_day]
    return res_matches, current_match_day


def get_league_matches(code_, match_day):
    """
    Prepare embed of league specific table and standings
    @param code_: league code ( ex: premier league : PL)
    @return: Embed with team or league fixtures
    """
    try:
        if code_ is None:
            raise InvalidLeagueCodeException("Code is Invalid. Give proper League code ")
        # if code_.upper() in TEAM_LONG_NAME_CODES.values():
        #     code_type = "TEAM"
        #     team = [team_de["id"] for team_de in TEAMS if team_de["tla"] is not None and code_.upper() == team_de["tla"].upper()]
        #     code_id = team[0] if len(team) >=1 else None
        #     print(code_id)
        elif code_.upper() in LEAGUE_CODES:
            code_type = "LEAGUE"
            code_id = LEAGUE_CODES.get(code_.upper())
        else:
            raise InvalidLeagueCodeException(f"League code {code_} is invalid")
        fixtures = get_fixtures(code_id, code_type)["matches"]
        format_league_fix, current_match_day = format_league_fixtures(fixtures, match_day)
        title = f"{code_} - league fixtures/matches"
        description = f"Match Day - {current_match_day}"
        fields = []
        for each_fix in format_league_fix:
            fields.append({"name" : f"{each_fix['home']} vs {each_fix['away']}",
                           "value": f"Kickoff: {each_fix['timestamp']}" })
        fixtures_embed = prepare_embed(title, description, fields)
        return fixtures_embed
    except InvalidLeagueCodeException as exp:
        print(exp)
        return discord.Embed(title=f" League fixtures - {code_}",
                                                   description=f"League code {code_} is invalid!!!")










