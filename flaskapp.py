from flask import Flask
import json
import urllib.request
import webbrowser
import os
import requests


#base_url = "https://pub.gamezop.com/v3/games?id="
#base_url2 = "35.200.156.47"
    

#pub_id = input ("Enter Pub ID: ")
#final_url = base_url + pub_id    

#response_status = requests.get(final_url)
#response_code = response_status.status_code

#print (response_code)
    
#data_api = response_status.json()

#for game in (data_api["games"]):
#    print (game["name"]["en"])


app = Flask(__name__)

@app.route("/")

def index():
    return "Games: "

#@app.route("/PubID/<ID>")

#def PubID(ID):
    
#    base_url = "https://pub.gamezop.com/v3/games?id="
#    pub_id = input ("Enter Pub ID: ")
#    final_url = base_url + pub_id
#    response_status = requests.get(final_url)
#    response_code = response_status.status_code

#    data_api = response_status.json()

#    gamename = []
#    for game in (data_api["games"]):
#        gamename.append(game["name"]["en"])

#    data_api2 = gamename        

#    def  writeToJSONFile (path, fileName, data):
#        FilePathName = "./" + path + "/" + fileName + ".json"
#        with open(FilePathName, "w+") as jsonf:
#            json.dump(data, jsonf)


#    path = "./"
#    fileName = pub_id
#    data = data_api2
#    fname = pub_id + ".json"

#    return fname


if __name__ == "__main__":
    app.run(debug = True)