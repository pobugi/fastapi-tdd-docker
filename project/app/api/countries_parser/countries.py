import requests
import json


class CountryData:

    def __init__(self) -> None:
        self.url = "https://restcountries.eu/rest/v2/all"

    def get_all_countries(self):
        response = requests.get(self.url)
        result = [{'name': country['name'], 'region': country['region']} for country in json.loads(response.text)[:7]]
        return result
