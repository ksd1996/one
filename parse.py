import requests
import json
import urllib.request

choice = input ("Enter y to initiate or n to terminate: ")

def fgames():
    base_url = ("https://pub.gamezop.com/v3/games?id=")
    pub_id = input ("Enter ID: ")
    final_url = base_url + pub_id
    print (final_url)
    response_status = requests.get(final_url)
    print (response_status)
    response_code = response_status.status_code
    print (response_code)
    data = response_status.json()
    if (response_code == 200):
        for game in (data["games"]):
            print (game["name"]["en"])
    else:
        print ("Wrong PUB ID entered")      
        

while (choice == "y"):
    fgames()
    


    

    
