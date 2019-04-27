import json
import sys

import geo
from pymongo import MongoClient, errors


with open('settings.json', 'r') as _settings:
    _data = json.load(_settings)
    _connection_string = _data['db_connection_str']


def connect_with_db():
    global _db
    try:
        _client = MongoClient(_connection_string)
        _db = _client['greetings_app'] \
            if "pytest" not in sys.modules \
            else _client['greetings_app_test']
    except errors.ConnectionFailure:
        print("Connection failure with DB ")

    return _db


connect_with_db()


def send_greetings(name, greeting):
    coll = _db['greetings']
    localization = geo.get_localization()

    greeting = {
        "name": name,
        "greeting": greeting,
        "location": {
            "type": "Point",
            "coordinates": [localization[0], localization[1].split('\n')[0]]
        }
    }
    coll.insert_one(greeting)

