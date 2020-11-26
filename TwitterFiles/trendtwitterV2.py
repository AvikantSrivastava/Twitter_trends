import tweepy
import os
import json
import sys
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

trendlist_india = []
trendlist_world = []

class getTrends():
    def __init__(self):
        pass

    def getTrends_India(self):

        for value in india_trends:
            for trend in value['trends']:
                trendlist_india.append(trend['name'])
        trends_trunc_india = [x[1:] if x.startswith('#') else x for x in trendlist_india]
        return trends_trunc_india

    def getTrends_World(self):

        for value in world_trends:
            for trend in value['trends']:
                trendlist_world.append(trend['name'])
        trends_trunc_world = [x[1:] if x.startswith('#') else x for x in trendlist_world]
        return trends_trunc_world
