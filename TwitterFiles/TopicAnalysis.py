import mysql.connector
import pandas as pd
import time
import itertools
import math
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import datetime
import plotly.offline as py
import plotly.graph_objs as go
import sys
sys.path.append("..")
import credentials, settings

while True:
    db_connection = mysql.connector.connect(
        host="localhost",
        user="newuser",
        passwd="password",
        database="TwitterDB",
        charset = 'utf8'
    )

    timenow = (datetime.datetime.utcnow() - datetime.timedelta(hours=0, minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
    query = "SELECT id_str, text, created_at, polarity, user_location FROM {} WHERE created_at >= '{}' " \
                     .format(settings.TABLE_NAME, timenow)
    df = pd.read_sql(query, con=db_connection)

    df['created_at'] = pd.to_datetime(df['created_at'])

    result = df.groupby([pd.Grouper(key='created_at', freq='30s'), 'polarity']).count().unstack(fill_value=0).stack().reset_index()
    result = result.rename(columns={"id_str": "Num of '{}' mentions".format(settings.TRACK_WORDS), "created_at":"Time in UTC"})

    fig = px.line(result, x='Time in UTC', y="Num of '{}' mentions".format(settings.TRACK_WORDS), color='polarity')
    fig.show()
    time.sleep(60)
