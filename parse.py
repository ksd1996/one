import requests
import json

base_url = ("https://pub.gamezop.com/v3/games?id=")
pub_id = input ("Enter ID: ")
final_url = base_url + pub_id
response_status = requests.get(final_url)
data = response_status.json()

for game in data["games"]:
    print (game['name']['en'])
