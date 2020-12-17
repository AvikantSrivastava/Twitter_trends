import datetime
from Database.Database import database
from TwitterFiles.TrendTwitter import TrendTwitter
from TwitterFiles.SentimentalAnalysis import SentimentEngine

main_locations = ['India', 'World']

all_locations = ['World',
                 'India',
                 'Newyork',
                 'Toronto',
                 'Sydney',
                 'London',
                 'Madrid',
                 'Paris',
                 ]


TrendData = {}
TrendDB_name = 'TrendDB'
TrendDB = database(TrendDB_name)


for location in all_locations:
    obj = TrendTwitter(location)
    TrendData[location] = []
    TrendValues = {}
    TrendValues['trends'] =  obj.getTrends()
    TrendValues['volume'] = obj.getVolume()
    TrendValues['url'] = obj.getUrl()

    TrendData[location].append(TrendValues)

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
        TrendScore['volume'] = obj.getVolume()
        TrendScore['url'] = obj.getUrl()

        SentimentData[location].append(TrendScore)

SentimentDB.dump(SentimentData)
