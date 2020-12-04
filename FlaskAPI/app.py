from flask import Flask, jsonify
from flask_cors import CORS
from TwitterFiles.TrendTwitter import TrendTwitter
import datetime
from Database.Database import database
app = Flask(__name__)
CORS(app)

TrendDB_name = 'TrendDB'
TrendDB = database(TrendDB_name)

SentimentDB_name = 'SentimentDB'
SentimentDB = database(SentimentDB_name)


@app.route('/')
def api():
    TrendData = TrendDB.fetch()
    Data = {
        'date': datetime.datetime.now(),
        'trends': TrendData
    }

    return jsonify(Data)


@app.route('/<location>', methods=['GET'])
def locationTrend(location):
    TrendData = TrendDB.fetch()
    Data = {
        'date': datetime.datetime.now(),
        'trends': TrendData[location]
    }

    return jsonify(Data)


if __name__ == '__main__':
    app.run(debug=True)
