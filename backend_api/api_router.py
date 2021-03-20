# -*- coding: utf-8 -*-
from loguru import logger
from typing import Tuple

from apis.weather_api import Weather_api

class API_router:

    def __init__(self) -> None:
        self.weather_api = Weather_api()

    def get_weather(self) -> Tuple[dict, int]:
        weather = self.weather_api.get_weather()
        if weather:
            status_code = 200
        else:
            status_code = 400
        return weather, status_code

if __name__ == "__main__":
    apis = API_router()
    apis.get_weather()