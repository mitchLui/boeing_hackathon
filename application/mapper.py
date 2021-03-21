# -*- coding: utf-8 -*-
from loguru import logger
from typing import Tuple, Union
from dotenv import load_dotenv
import requests
import gmplot
import json
import os

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

    def get_data(self) -> Union[list, dict]:
        pass

    def get_json(self) -> dict:
        data = {
            "lat": self.starting_lat,
            "lng": self.starting_lng
        }
        return data

    def get_html(self, city_id = "felixstowe") -> str:
        port_data = self.config["ports"].get(city_id, "felixstowe")
        starting_lat = port_data["lat"]
        starting_lng = port_data["lng"]
        gmap = gmplot.GoogleMapPlotter(starting_lat, starting_lng, 14, apikey=self._get_api_key())
        gmap.marker(starting_lat, starting_lng, color=port_data["colour"], label=port_data["name"])
        for port in self.config["ports"].values():
            gmap.marker(port["lat"], port["lng"], color=port["colour"], label=port["name"])
        return gmap.get()

    def main(self, rtype: str, city: str) -> Tuple[Union[str, dict], int]:
        if rtype == "json": return self.get_json(), 200
        elif rtype == "html": return self.get_html(city), 200
        else: return "Unsupported rtype", 400

if __name__ == "__main__":
    mapper = Mapper()
    
