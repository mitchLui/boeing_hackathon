# -*- coding: utf-8 -*-
from dotenv import load_dotenv
from loguru import logger
import requests
import os

class Marine_api:

    def __init__(self) -> None:
        self.url = "http://api.openweathermap.org/"
        self.api_key = self._get_api_key()
        self.api_version = "2.5"
        
    def _get_api_key(self):
        load_dotenv(verbose=True)
        return os.getenv("OPENWEATHER_KEY")

    def get_weather(self, location):
        logger.info(f"Querying weather for location {location}")
        endpoint = f"data/{self.api_version}/weather"
        parameters = {"q": location, "appid": self.api_key}
        r = requests.get(url=f"{self.url}{endpoint}", params=parameters)
        logger.info(f"Weather API returned {r.status_code}")
        results = r.json() if r.status_code == 200 else {}
        return results

if __name__ == "__main__":
    api = Marine_api()
    print(api.get_weather("London"))


     