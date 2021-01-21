
from os import environ
class Config():
    
    CHROMEDRIVER_PATH ='./ressources/chromedrivers/mac/chromedriver'
    INSTAGRAM_URL     ='https://instagram.com/'
    LOGIN_URL         ='https://www.instagram.com/accounts/login/'
    
    API_PROFILE       = lambda x: "https://www.instagram.com/{0}/?__a=1".format(x)
    SESSION_ID        = "<YOUR_SESSION>"