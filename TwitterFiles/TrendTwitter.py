import os
import tweepy


class TrendTwitter():

    def __init__(self, cityname):

        # Authentication
        auth = tweepy.OAuthHandler(
            os.environ['API_KEY'],
            os.environ['API_SECRET_KEY'])

        auth.set_access_token(
            os.environ['ACCESS_TOKEN'],
            os.environ['ACCESS_TOKEN_SECRET'])

        self.api = tweepy.API(auth)

        self.cityname = cityname
        self.woe_id = {
            'World': 1,
            'India': 23424848,
            'Newyork': 2459115,
            'Toronto': 4118,
            'Sydney': 1105779,
            'London': 44418,
            'Madrid': 766273,
            'Paris': 615702,
        }

        self.cityTrends = self.api.trends_place(self.woe_id[self.cityname])
        self.trendlist = []
        self.volume = []
        self.url = []

    def getTrends(self):
        for value in self.cityTrends:
            for trend in value['trends']:
                self.trendlist.append(trend['name'])
        trends_trunc = [x[1:] if x.startswith(
            '#') else x for x in self.trendlist]
        return trends_trunc[:10]

    def getVolume(self):
        for value in self.cityTrends:
            for trend in value['trends']:
                self.volume.append(trend['tweet_volume'])
        return self.volume[:10]

    def getUrl(self):
        for value in self.cityTrends:
            for trend in value['trends']:
                self.url.append(trend['url'])
        return self.url[:10]

if __name__ == '__main__':
# mainly for testing
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

    Location_Trends = {}
    for location in main_locations:
        print(f'Trends for {location} are')
        Location_Trends[location] = TrendTwitter(location)
        for num, trend in enumerate(Location_Trends[location].getTrends()):
            print(f'{num + 1} : {trend}')
        print("________")
