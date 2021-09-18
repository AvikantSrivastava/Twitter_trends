import os
from textblob import TextBlob
import tweepy
import yake


class SentimentEngine:
    # Authentication
    auth = tweepy.OAuthHandler(os.environ["API_KEY"], os.environ["API_SECRET_KEY"])

    auth.set_access_token(os.environ["ACCESS_TOKEN"], os.environ["ACCESS_TOKEN_SECRET"])

    api = tweepy.API(auth, timeout=15)
    keyword_extractor = yake.KeywordExtractor(
        n=5, dedupLim=0.4, dedupFunc="seqm", top=15
    )

    def __init__(self, TrendName):

        self.Trend = TrendName
        search_query = self.Trend
        self.Tweets = []

        for tweet_object in tweepy.Cursor(
            self.api.search,
            q=search_query + " -filter:retweets",
            lang="en",
            result_type="recent",
        ).items(100):
            self.Tweets.append(tweet_object.text)

    def sentimental_analysis(self):
        self.positive = self.negative = 0

        for tweet in self.Tweets:
            analysis = TextBlob(tweet)
            if analysis.sentiment.polarity >= 0.2:
                self.positive += 1
            elif analysis.sentiment.polarity <= -0.2:
                self.negative += 1
        if self.positive == 0 and self.negative == 0:
            self.PositiveScore = 0.50
            self.NegativeScore = 0.50
        else:
            self.PositiveScore = round(
                self.positive / (self.positive + self.negative), 2
            )
            self.NegativeScore = round(
                self.negative / (self.positive + self.negative), 2
            )

    def get_sentiment_scores(self):
        return self.PositiveScore, self.NegativeScore

    def keyword_extraction(self):
        combined_tweets = " ".join(self.Tweets)
        self.keywords = self.keyword_extractor.extract_keywords(combined_tweets)
        
    
    def get_keywords(self):
        return [word[0] for word in self.keywords]

if __name__ == "__main__":
    # mainly for testing

    eminem = SentimentEngine("eminem")
    eminem.sentimental_analysis()

    print(
        f"Score for Eminem Good {eminem.get_sentiment_scores()[0]} Bad {eminem.get_sentiment_scores()[1]}"
    )

    mkbhd = SentimentEngine("mkbhd")
    mkbhd.sentimental_analysis()
    print(
        f"Score for RCB Good {mkbhd.get_sentiment_scores()[0]} Bad {mkbhd.get_sentiment_scores()[1]}"
    )
