import datetime
import json
from TwitterFiles.TrendTwitter import TrendTwitter
from TwitterFiles.SentimentalAnalysis import SentimentEngine

import pprint

main_locations = ['india', 'world']

all_locations = ['world',
                 'india',
                 'newyork',
                 'toronto',
                 'sydney',
                 'london',
                 'madrid',
                 'paris',
                 ]


trending = {}

for location in all_locations:
    obj = TrendTwitter(location)
    trending[location] = obj.getTrends()

#print(json.dumps(trending, indent=4))
trendingMain = {}

for location in main_locations:
    obj = TrendTwitter(location)
    trendingMain[location] = obj.getTrends()

print(trendingMain)

senti = {}
#
# for location in main_locations:
#   senti[location] = SentimentEngine()
#
# Location_Trends = {}
# for location in main_locations:
#     print(f'Trends for {location} are')
#     Location_Trends[location] = TrendTwitter(location)
#     for num, trend in enumerate(Location_Trends[location].getTrends()):
#         print(f'{num + 1} : {trend}')
#     print("________")
