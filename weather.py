import os
import requests
import json

class Weather:
    def __init__(self, country, city):
        self.country = country
        self.city = city
        self.weather = self._getWeather()
    def _getWeather(self):
        URL = f"http://api.weatherstack.com/current?access_key={os.environ.get('WEATHER_KEY')}&query={self.city},{self.country}"
        response = requests.get(URL)
        return json.loads(response.current)
