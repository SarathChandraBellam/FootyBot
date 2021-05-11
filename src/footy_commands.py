""""
"""
import os
import discord
from src.util import load_json, DATA_PATH, prepare_embed
from src.codes import LEAGUE_TEAM_CODES, TOP_TEAM_CODES
from src.exception import InvalidLeagueCodeException

TEAMS = load_json(os.path.join(DATA_PATH, "teams.json"))
COMPETITIONS = load_json(os.path.join(DATA_PATH, "competitions.json"))


def get_team_codes(league_code):
    """
    Prepare embed of league specific team codes
    @param league_code: league code ( ex: premier league : PL)
    @return: Embed with teams and their codes
    """
    embed = discord.Embed()
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
            fields = [{"name": name, "value": value, "binary_format": "\n\u200b"} for name, value in league_teams.items()]
        embed = prepare_embed(title, description, fields)
    except InvalidLeagueCodeException as exp:
        print(exp)
    return embed










