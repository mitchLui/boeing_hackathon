# -*- coding: utf-8 -*-
from loguru import logger
from dotenv import load_dotenv
from typing import Tuple
from weather_api.weather_api import Weather_api
from datalastic.historical_data import Historical_data
from datalastic.location_monitor import Location_monitor
from datalastic.port_finder import Port_finder
from datalastic.ship_tracker import Ship_tracker
from datalastic.vessel_info import Vessel_info
from datalastic.vessel_search import Vessel_search
import os

class API_router:

    def __init__(self) -> None:
        self.weather_api = Weather_api(self._get_api_key("OPENWEATHER_KEY"))
        datalastic_key = self._get_api_key("DATALASTIC_KEY")
        self.historical_data = Historical_data(datalastic_key)
        self.location_monitor = Location_monitor(datalastic_key)
        self.port_finder = Port_finder(datalastic_key)
        self.ship_tracker = Ship_tracker(datalastic_key)
        self.vessel_info = Vessel_info(datalastic_key)
        self.vessel_search = Vessel_search(datalastic_key)

    def _get_api_key(self, key: str):
        load_dotenv(verbose=True)
        return os.getenv(key)

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