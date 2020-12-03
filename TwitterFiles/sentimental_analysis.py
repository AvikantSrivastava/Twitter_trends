from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
import tweepy
import sys
sys.path.append("..")
import credentials
from TwitterFiles.trendtwitterV2 import getTrends


authorizer = OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
authorizer.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(authorizer ,timeout=15)
all_tweets = []
trend_wise = getTrends()


top_1 = trend_wise.getTrends_India()
top_1 =top_1[0]

search_query = top_1

for tweet_object in tweepy.Cursor(api.search,q=search_query+" -filter:retweets",lang='en',result_type='recent').items(200):
    all_tweets.append(tweet_object.text)



positive = negative = 0
for tweet in all_tweets:

    analysis = TextBlob(tweet)
        # set sentiment
    if analysis.sentiment.polarity >= 0:
        positive+=1
    else:
        negative +=1
print("Positive tweets percent ", positive / len(all_tweets))
print("Negative tweets percent ", negative / len(all_tweets))
