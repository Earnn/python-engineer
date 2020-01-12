import tweepy

# Twitter's token 
CONSUMER_KEY= "0n9kCxq9kCE5pWyxZGbv0HU1B"
CONSUMER_SECRET="JWb77u5gjZq1Bet9iIuOKPMUY2siPO2EvZ327fFV5NfahA7hVa"
ACCESS_TOKEN = "298527382-0oGwXORPIOqXKOMVbogc9JUruAUYhU11bDnOES0r"
ACCESS_TOKEN_SECRET="toUYWyIU8AUnaLwyuZgaiRDPekKr7VGPTvGoyfxhuvzSI"



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True)