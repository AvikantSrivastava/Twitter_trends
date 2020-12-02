from flask import Flask, jsonify
import datetime
app = Flask(__name__)


@app.route('/')
def api():
  # dummy data, will fetch this data from a database.
    data = {
        'date': datetime.datetime.now(),
        'top_trends': [
            {'name': 'Trend Name 1',
             'positive': 56,
             'negative': 12,
             },

             {'name': 'Trend Name 2',
             'positive': 56,
             'negative': 12,
             },

             {'name': 'Trend Name 3',
             'positive': 23,
             'negative': 54,
             },
        ]
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
