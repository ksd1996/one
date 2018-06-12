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
        print ("The request is OK.")
        for game in (data["games"]):
            print (game["name"]["en"])        
    if (response_code == 401):
        print ("The requested page needs a username and a password.")
    if (response_code == 501):
        print ("The request was not completed. The server did not support the functionality required.")
    if (response_code == 500):
        print ("The request was not completed. The server met an unexpected condition.")                
          
        

while (choice == "y"):
    fgames()
    


    

    
