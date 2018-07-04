from flask import Flask
from flask import json
from flask import jsonify
from flask import request
import json
import urllib.request
import requests

app = Flask(__name__)

@app.route("/")
def index():    
    return json.dumps("No file here."), 200, {'content-type': 'application/json'}

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return "Invalid route."    

@app.route("/gamenames")
def gamenames():   
    if ("id" in request.args):
        pub_id = request.args["id"]
    else:
        return json.dumps("Key value does not exist. Enter id as key."), 400, {'content-type': 'application/json'}
    
    base_url = ("https://pub.gamezop.com/v3/games?id=") + pub_id
    response_status = requests.get(base_url)
    response_code = response_status.status_code
    
    if (response_code == 200):
        data = response_status.json()
        gamename = []
        for game in (data["games"]):
            gamename.append(game["name"]["en"])
        return json.dumps(gamename), 200, {'content-type': 'application/json'} 
    
    elif (response_code == 401):
        return json.dumps("Publisher ID entered is invalid."), 401, {'content-type': 'application/json'}
    
    elif (response_code == 500):
        return json.dumps ("The request was not completed. The server met an unexpected condition."), 500, {'content-type': 'application/json'}
    
    elif (response_code == 501):
        return json.dumps ("The remote server seems to be down. Please try after some time."), 501, {'content-type': 'application/json'}

if __name__ == "__main__":  
    app.run(host='0.0.0.0',port=80)