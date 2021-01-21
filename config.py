from os import environ
import json

class Config():
    
    CHROMEDRIVER_PATH ='./ressources/chromedrivers/mac/chromedriver'
    INSTAGRAM_URL     ='https://instagram.com/'
    LOGIN_URL         ='https://www.instagram.com/accounts/login/'
    
    API_PROFILE       = lambda x: "https://www.instagram.com/{0}/?__a=1".format(x)
    
    with open('data/data.json') as json_file:
        data = json.load(json_file)
        SESSION_ID        = data['session_id']
    json_file.close()