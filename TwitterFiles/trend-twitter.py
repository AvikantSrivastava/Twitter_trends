import tweepy
import os
import json
import sys
#import geocoder
sys.path.append("..")
from tweepy.auth import OAuthHandler
import twitter
import credentials, settings

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

world_woe_id = 1
india_woe_id = 23424848

world_trends = api.trends_place(id=world_woe_id)
india_trends = api.trends_place(id=india_woe_id)

trends = []

for value in india_trends:
    for trend in value['trends']:
        trends.append(trend['name'])
    #    print(trend['name'])
print(trends)
