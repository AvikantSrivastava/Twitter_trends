import re
import tweepy
import mysql.connector
import pandas as pd
import string
from textblob import TextBlob
from nltk.corpus import stopwords
import sys
sys.path.append("..")
import credentials, settings
import nltk
nltk.download('stopwords')
stopwords = stopwords.words('english')

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):

        if status.retweeted:
            return False

        id_str = status.id_str
        created_at = status.created_at
        text = deEmojify(status.text)
        sentiment = TextBlob(text).sentiment
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity


        user_created_at = status.user.created_at
        user_location = deEmojify(status.user.location)
        user_description = deEmojify(status.user.description)
        user_followers_count = status.user.followers_count

        longitude = None
        latitude = None

        if status.coordinates:
            longitude = status.coordinates['coordinates'][0]
            latitude = status.coordinates['coordinates'][1]

        retweet_count = status.retweet_count
        favorite_count = status.favorite_count

        print(status.text)
        print(f"Longitude: {longitude}, Latitude: {latitude}")

        if mydb.is_connected():
            mycursor = mydb.cursor()
            sql = "INSERT INTO {} (id_str, created_at, text, polarity, subjectivity, user_created_at, user_location, user_description, user_followers_count, longitude, latitude, retweet_count, favorite_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)".format(settings.TABLE_NAME)
            val = (id_str, created_at, text, polarity, subjectivity, user_created_at, user_location, \
                user_description, user_followers_count, longitude, latitude, retweet_count, favorite_count)
            mycursor.execute(sql, val)
            mydb.commit()
            mycursor.close()

    def on_error(self, status_code):
        if status_code == 420:
            return False

#def remove_url(txt):
#    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

#def deEmojify(text):
#    if text:

    #    text_clean = [word for word in text if word not in string.punctuation and word not in stopwords]
    #    text = ''.join(text_clean)
    #
#        text = re.sub(r'^RT[\s]+', '', text)
#        text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
#        text = re.sub(r'#', '', text)
#        text = [remove_url(tweet) for tweet in text1]

#        regex_pattern = re.compile(pattern = "["
#            u"\U0001F600-\U0001F64F"
#            u"\U0001F300-\U0001F5FF"
#            u"\U0001F680-\U0001F6FF"
#            u"\U0001F1E0-\U0001F1FF"
#            "]+", flags = re.UNICODE)
#        return regex_pattern.sub(r'',text)
#    else:
#        return None


#def clean_tweet(self, tweet):
#    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \
#                                |(\w+:\/\/\S+)", " ", tweet).split())
def clean_tweet(self, tweet):
    '''
    Use sumple regex statemnents to clean tweet text by removing links and special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \
                                |(\w+:\/\/\S+)", " ", tweet).split())
def deEmojify(text):
    '''
    Strip all non-ASCII characters to remove emoji characters
    '''
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None

mydb = mysql.connector.connect(
    host="localhost",
    user="newuser",
    passwd="password",
    database="TwitterDB",
    charset = 'utf8'
)

if mydb.is_connected():
    mycursor = mydb.cursor()
    mycursor.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{}'
        """.format(settings.TABLE_NAME))
    if mycursor.fetchone()[0] != 1:
        mycursor.execute("CREATE TABLE {} ({})".format(settings.TABLE_NAME, settings.TABLE_ATTRIBUTES))
        mydb.commit()
    mycursor.close()


auth = tweepy.OAuthHandler(credentials.API_KEY, credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

myStreamListener = MyStreamListener()
mystream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
mystream.filter(languages=["en"], track = settings.TRACK_WORDS)

mydb.close()
