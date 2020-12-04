import os
from deta import Deta


class database():
    def __init__(self, DB_Name):
        # authentication
        deta = Deta(os.environ['DETA_PROJECT_KEY'])
        self.db = deta.Base(DB_Name)

    def dump(self, record, key='latest'):
        self.db.put(record, key)

    def fetch(self, key='latest'):
        return self.db.get(key)


if __name__ == '__main__':
    # Trend list Database.
    TrendDB_name = 'TrendDB'
    TrendDB = database(TrendDB_name)
    print(TrendDB.fetch())

    # Sentiment Database.
    SentimentDB_name = 'SentimentDB'
    SentimentDB = database(SentimentDB_name)
