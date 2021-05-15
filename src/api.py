from src.util import get_data_from_api
# from util import get_data_from_api # local testing


def get_standings(league_id):
    suffix = f"competitions/{league_id}/standings"
    data = get_data_from_api(suffix)
    return data
