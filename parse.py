import requests
import json
import urllib.request 




def find_games():
    base_url = ("https://pub.gamezop.com/v3/games?id=")
    pub_id = input ("Enter publisher ID: ")

    # Generating complete URL 
    final_url = base_url + pub_id
    response_status = requests.get(final_url)
    response_code = response_status.status_code
    data = response_status.json()
    
    
    if (response_code == 200):
        for game in (data["games"]):
            print (game["name"]["en"])
        
    
    elif (response_code == 401):
        print ("The publisher ID you entered is wrong. Please check again and re-enter.")
        
        # Call the method again to allow re entry of publisher ID
        run_again = input ("Y to continue or n to terminate: ")
        if (run_again == "n"):
            return
        find_games()
    
    elif (response_code == 501):
        print ("The request was not completed. The server did not support the functionality required.")
    
    elif (response_code == 500):
        print ("The request was not completed. The server met an unexpected condition.")    
    
    elif (response_code == 502):
        print ("The remote server seems to be down. Please try after some time.")                
 
    run_again = input ("Do you want to check game names for any other publisher ID? Press y or n: ")
    if (run_again == "y"):
        find_games()
    if (run_again == "n"):
        return 0


def leaderboard():
    
    # Generating complete URL

    base_url = "https://pub.gamezop.com/v2/leaderboards/info?code="
    game_code = input ("Enter game code: ")
    final_url = base_url + game_code
    response_status = requests.get(final_url)
    respcode = response_status.status_code
    print (respcode)
    data = response_status.json()
    data_2 = response_status.json()

    # Printing game's leaderboard
    
    for name in (data["leaderboards"]):
        print (name["name"])
    for description in (data["leaderboards"]):
        print (description["description"])
    for leaderboardID in (data["leaderboards"]):
        print (leaderboardID["leaderboardId"])

def leaderboard_score():

    base_url = "https://pub.gamezop.com/v2/leaderboards/scores"
    Pub_ID = input ("Enter pub ID: ")
    Sub_ID = input ("Enter sub ID: ")
    Leaderboard_ID = input ("Enter leaderboard ID: ")
    
    # Generating sample request body

    data = {"id": Pub_ID,
            "sub": Sub_ID,
            "leaderboardId": Leaderboard_ID,
            "limit": 10}
    
    
    response_body = requests.post(url = "https://pub.gamezop.com/v2/leaderboards/scores", data = data)
    respcode = response_body.status_code
    if (respcode != 200):
        leaderboard_score()
    response_body_json = response_body.json()
    response_code = response_body
   
    # Printing all array elements 
    
    print (response_code)
    print (response_body_json["scores"][0]["sub"]) 
    print (response_body_json["scores"][0]["score"])
    print (response_body_json["scores"][0]["rank"])

# User input choice among three programs

choice = input ("Enter 1 to find games specific to pub ID; Enter 2 to get game's leaderboard; Enter 3 to get score: ")
if (choice == "1"):
    find_games()
if (choice == "2"):
    leaderboard()
if (choice == "3"):
    leaderboard_score()



