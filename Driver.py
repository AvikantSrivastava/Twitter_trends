import datetime
import json
from TwitterFiles.TrendTwitter import TrendTwitter
from TwitterFiles.SentimentalAnalysis import SentimentEngine


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



TrendData = {}
TrendDB_name = 'TrendDB'
TrendDB = database(TrendDB_name)

for location in all_locations:
    obj = TrendTwitter(location)
    TrendData[location] = obj.getTrends()

TrendDB.dump(TrendData)

SentimentData = {}
SentimentDB_name = 'SentimentDB'
SentimentDB = database(SentimentDB_name)

for location in main_locations:
    obj = TrendTwitter(location)
    Trends = obj.getTrends()
    SentimentData[location] = []

    for num,Trendname in enumerate(Trends):
        Trend = SentimentEngine(Trendname)
        TrendScore = {}
        postive, negative = Trend.getScores()
        TrendScore['name'] = Trendname
        TrendScore['rank'] = num + 1
        TrendScore['positive'] = postive
        TrendScore['negative'] = negative

        SentimentData[location].append(TrendScore)
    
SentimentDB.dump(SentimentData)
