# -*- coding: utf-8 -*-
from loguru import logger
from typing import Tuple, Union
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
import requests
import gmplot
import json
import os

from requests.api import request

class Mapper:

    def __init__(self) -> None:
        self.config = self.load_config()
        self.port_ids = list(self.config["ports"].keys())

    def load_config(self, filename="config.json"):
        with open(filename, "r") as f:
            data = json.load(f)
        return data

    def _get_api_key(self) -> str:
        load_dotenv(verbose=True)
        return os.getenv("GMPLOT_KEY")    

    def get_data_thread(self) -> dict:
        with ThreadPoolExecutor(workers=5) as e:
            results = list(e.map())
        return results

    def get_data(self, ) -> Union[list, dict]:
        r = requests.get()

    def get_port_data(self): pass


    def get_html(self, city_id = "felixstowe") -> str:
        port_data = self.config["ports"].get(city_id, "felixstowe")
        starting_lat = port_data["lat"]
        starting_lng = port_data["lng"]
        gmap = gmplot.GoogleMapPlotter(starting_lat, starting_lng, 14, apikey=self._get_api_key())
        gmap.marker(starting_lat, starting_lng, color=port_data["colour"], info_window=port_data["name"])
        for port in self.config["ports"].values():
            gmap.marker(port["lat"], port["lng"], color=port["colour"], info_window=port["name"])
        return gmap.get()

    def main(self, city: str) -> Tuple[Union[str, dict], int]:
        return self.get_html(city), 200

if __name__ == "__main__":
    mapper = Mapper()
    
