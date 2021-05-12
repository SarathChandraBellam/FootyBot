from util import get_data_from_api

def get_standings(league_id):
    suffix = f"competitions/{league_id}/standings"
    data = get_data_from_api(suffix)
    print(data)

get_standings(2021)