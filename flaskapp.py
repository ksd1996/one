from flask import Flask
from flask import json
from flask import jsonify
import json
import urllib.request
import webbrowser
import os
import requests

app = Flask(__name__)

@app.route("/")

def index():
    return "Games: "

@app.route("/PubID/<ID>")

def PubID(ID):
    base_url = ("https://pub.gamezop.com/v3/games?id=") + ID
    response_status = requests.get(base_url)
    response_code = response_status.status_code
    data = response_status.json()
    gamename = []
    for game in (data["games"]):
        gamename.append(game["name"]["en"])
    json_str = json.dumps(gamename)
    return jsonify(json_str)
 

if __name__ == "__main__":
    app.run(debug = True)