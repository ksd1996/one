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
gamename = []
for game in (data_api["games"]):
    gamename.append(game["name"]["en"])    

data_api2 = gamename

def  writeToJSONFile (path, fileName, data):
    FilePathName = "./" + path + "/" + fileName + ".json"
    with open(FilePathName, "w+") as jsonf:
        json.dump(data, jsonf)

path = "./"
fileName = pub_id
data = data_api2
fname = pub_id + ".json"

writeToJSONFile (path, fileName, data)



def my_api():
    base_url = "http://localhost:80/"
    final_url = base_url + fileName + ".json"
    #webbrowser.open_new(final_url)
    print (data_api2)

my_api()


choice = input ("Do you want to save the file or delete it? (y/n) ")
if (choice == "y"):
    os.remove (fname)

if (choice == "n"):
    exit()