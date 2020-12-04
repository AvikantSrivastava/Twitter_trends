import datetime
from Database.Database import database
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
print(TrendData)




# SentimentDB = {}

# for location in main_locations:
#     obj = TrendTwitter(location)
#     SentimentDB[location] = obj.getTrends()

# print(SentimentDB)
