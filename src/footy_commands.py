""""
"""
import os
import json
from src.util import get_embed, DATA_PATH


def get_competitions_codes():
    file_path = os.path.join(DATA_PATH, "competitions_top.json")
    with open(file_path, "r") as comp_file:
        competitions_data = json.load(comp_file)
    title = competitions_data["title"]
    desc = competitions_data["desc"]
    fields = competitions_data["fields"]
    return get_embed(title, desc, fields)
