import os
import tweepy
import sys
sys.path.append("..")


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
            'world': 1,
            'india': 23424848,
            'newyork': 2459115,
            'toronto': 4118,
            'sydney': 1105779,
            'london': 44418,
            'madrid': 766273,
            'paris': 615702,
        }

        self.cityTrends = self.api.trends_place(self.woe_id[self.cityname])
        self.trendlist = []

    def getTrends(self):
        for value in self.cityTrends:
            for trend in value['trends']:
                self.trendlist.append(trend['name'])
        trends_trunc = [x[1:] if x.startswith(
            '#') else x for x in self.trendlist]
        return trends_trunc[:10]


if __name__ == '__main__':
# mainly for testing
    locationlist = ['world',
                    'india',
                    'newyork',
                    'toronto',
                    'sydney',
                    'london',
                    'madrid',
                    'paris',
                    ]

    obj_list = {}

    # getting objects/ printing objects
    for location in locationlist:
        print(f'Trends for {location} are')
        obj_list[location] = TrendTwitter(location)
        for num, trend in enumerate(obj_list[location].getTrends()):
            print(f'{num + 1} : {trend}')
        print("________")
