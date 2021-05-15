from src.util import get_data_from_api
# from util import get_data_from_api # local testing


def get_standings(league_id):
    suffix = f"competitions/{league_id}/standings"
    data = get_data_from_api(suffix)
    return data


def get_fixtures(code_id, code_type="LEAGUE"):
    """

    @param code_id:
    @param code_type:
    @return:
    """
    team_suffix = f"teams/{code_id}/matches/"
    league_suffix = f"competitions/{code_id}/matches"
    if code_type == "LEAGUE":
        fixtures = get_data_from_api(league_suffix)
    else:
        fixtures = get_data_from_api(team_suffix)
    return fixtures

print(get_fixtures(2021, code_type="LEAGUE"))




