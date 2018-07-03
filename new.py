import json
import urllib.request
import webbrowser
import os
import requests


pub_id = input("Enter PubID: ")
base_url = "https://pub.gamezop.com/v3/games?id=" + pub_id
response_status = requests.get(base_url)
response_code = response_status.status_code
data_api = response_status.json()

gamename = []
for game in (data_api["games"]):
    gamename.append(game["name"]["en"])

data_api2 = gamename        

def  writeToJSONFile (path, fileName, data):
    FilePathName = "./" + path + "/" + fileName + ".json"
    with open(FilePathName, "w+") as jsonf:
        json.dump(data, jsonf)
    def games():
        return fname


path = "./"
fileName = pub_id
data = data_api2
fname = pub_id + ".json"

