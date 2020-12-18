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

    Location_Trends = {}
    for location in main_locations:
        print(f'Trends for {location} are')
        Location_Trends[location] = TrendTwitter(location)
        for num, trend in enumerate(Location_Trends[location].getTrends()):
            print(f'{num + 1} : {trend}')
        print("________")