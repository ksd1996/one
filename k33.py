import requests
import json
url = ("https://pub.gamezop.com/v3/games?id=")
pubid = input ("Enter ID")
url2 = url + pubid
url3 = requests.get(url2)
data = url3.json()
for game in data["games"]:
    print (game['name']['en'])
