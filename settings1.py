from TwitterFiles.trendtwitterV2 import getTrends

trend_wise = getTrends()
class Trackers():
    def __init__(self):
        pass

    def getTrackerIndia(self):
        trend_india = trend_wise.getTrends_India()
        return trend_india

    def getTrackerWorld(self):
        trend_world = trend_wise.getTrends_World()
        return trend_world


TRACK_WORDS = ["Maradona"]
TABLE_NAME = "Maradona"
TABLE_ATTRIBUTES = "id_str VARCHAR(255), created_at DATETIME, text VARCHAR(255), \
            polarity INT, subjectivity INT, user_created_at VARCHAR(255), user_location VARCHAR(255), \
            user_description VARCHAR(255), user_followers_count INT, longitude DOUBLE, latitude DOUBLE, \
            retweet_count INT, favorite_count INT"
t = Trackers()
print(t.getTrackerIndia())
