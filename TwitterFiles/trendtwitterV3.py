import tweepy
import os
import json
import sys
sys.path.append("..")
from tweepy.auth import OAuthHandler
import twitter
import credentials, settings
import tweepy

auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

locationlist = ['world',
                'india',
                'newyork',
                'toronto',
                # 'delhi',
                'sydney',
                'london',
              #  'berlin',
                'madrid',
                'paris',
                ]

woe_id = {
    'world' :1 ,
    'india' :23424848 ,
    'newyork' : 2459115,
    'toronto' :4118 ,
    'sydney' : 1105779,
    'london' : 44418,
    'madrid' : 766273,
    'paris' :615702 ,
}


# world_woe_id = 1
# india_woe_id = 23424848
# newyork_woe_id = 2459115
# toronto_woe_id = 4118
# delhi_woe_id = 2295019
# sydney_woe_id = 1105779
# london_woe_id = 44418
# berlin_woe_id = 638243
# madrid_woe_id = 766273
# paris_woe_id = 615702


trends = {}
for location in locationlist:
    trends[location] = api.trends_place(woe_id[location])
    print(location)



# class getTrends():
class Trends():

    def __init__(self,cityname,Trends):
        self.cityname = cityname
        self.cityTrends = Trends[self.cityname]
        self.trendlist = []


    def getTrends(self):
        for value in self.cityTrends:
            for trend in value['trends']:
                self.trendlist.append(trend['name'])
        trends_trunc = [x[1:] if x.startswith('#') else x for x in self.trendlist]
        return trends_trunc[:10]

if __name__ == '__main__':
    obj_list = {}
    # setting objejcts
    for location in locationlist:
        obj_list[location] = Trends(location, trends)

    # getting objects/ printing objects
    for location in locationlist:
        print(f'Trends for {location} are')
        for num, trend in enumerate(obj_list[location].getTrends()):
            print(f'{num + 1} : {trend}')
        print("________")