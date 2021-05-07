import requests


headers = { 'X-Auth-Token': 'f8bc1470c34c47388c38ffb20a59a393' }
resp = requests.get("https://api.football-data.org/v2/competitions", headers=headers)
print(resp.json())
