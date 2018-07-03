import json
import urllib.request
import webbrowser
import os
import requests


base_url = "https://pub.gamezop.com/v3/games?id="
    

pub_id = input ("Enter Pub ID: ")
final_url = base_url + pub_id    

response_status = requests.get(final_url)
response_code = response_status.status_code
    
print (response_code)
    
data_api = response_status.json()

for game in (data_api["games"]):
    print (game["name"]["en"])