# -*- coding: utf-8 -*-
from loguru import logger
import requests

class Weather_api:

    def __init__(self, api_key) -> None:
        self.url = "http://api.openweathermap.org/"
        self.api_key = api_key
        self.api_version = "2.5"

    def format_answer(self, results: dict) -> dict:
        weather_data = {}
        if results:
            weather_data.update({
                "name": results["name"],
                "weather_name": results["weather"][0]["main"],
                "weather_icon": results["weather"][0]["icon"],
                "temp": results["main"]["temp"],
                "visibility": results["visibility"],
                "wind_speed": results["wind"]["speed"],
                "wind_deg": results["wind"]["deg"],
                "success": True
            })
        else:
            weather_data.update({
                "success": False
            })
        return weather_data

    def get_weather(self) -> dict: 
        """Gets weather for Bristol

        Returns:
            results [dict]: Weather data
        """
        results = {}
        logger.info(f"Querying weather for Bristol")
        endpoint = f"data/{self.api_version}/weather"
        parameters = {"id": "2654675", "appid": self.api_key, "units": "metric"}
        r = requests.get(url=f"{self.url}{endpoint}", params=parameters)
        logger.info(f"Weather API returned {r.status_code}")
        results = r.json() if r.status_code == 200 else {}
        return self.format_answer(results)

if __name__ == "__main__":
    api = Weather_api()
    print(api.get_weather())


     