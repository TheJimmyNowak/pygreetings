import requests
import json

with open('settings.json', 'r') as _settings:
    _data = json.load(_settings)
    _geoApiUrl = _data['geo_localization_api']


def get_localization():
    response = requests.get(_geoApiUrl)

    if not response.status_code == requests.codes.ok:
        raise requests.exceptions.ConnectionError

    return response.content.decode('UTF-8').split(',')