import os
from pymongo import MongoClient

class Connect(object):
    def __init__(self):
        self._mongo_uri = os.getenv('MONGO_URI')

    def get_connection(self):
        client = MongoClient(self._mongo_uri)
        return client['bookscrape']

client = Connect()
mongo = client.get_connection()