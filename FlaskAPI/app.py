from flask import Flask, jsonify
from flask_cors import CORS
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
    SentimentData = SentimentDB.fetch()
    Data = {
        'date': datetime.datetime.now(),
        'trends': SentimentData
    }

    return jsonify(Data)

@app.route('/alltrends')
def alltrends():
    TrendData = TrendDB.fetch()
    Data = {
        'date': datetime.datetime.now(),
        'trends': TrendData
    }

    return jsonify(Data)


@app.route('/alltrends/<location>', methods=['GET'])
def locationTrend(location):
    TrendData = TrendDB.fetch()
    Data = {
        'date': datetime.datetime.now(),
        'trends': TrendData[location]
    }

    return jsonify(Data)


if __name__ == '__main__':
    app.run(debug=True)
