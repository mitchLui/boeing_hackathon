# -*- coding: utf-8 -*-
from loguru import logger
from typing import Tuple, Union
from dotenv import load_dotenv
import requests
import gmplot
import os

class Mapper:

    def __init__(self) -> None:
        self.gmap = gmplot.GoogleMapPlotter(51.4545, 2.5879, 14, apikey=self._get_api_key())

    def _get_api_key(self) -> str:
        load_dotenv(verbose=True)
        return os.getenv("GMPLOT_KEY")    

    def get_data(self) -> Union[list, dict]:
        pass

    def get_json(self) -> dict:
        data = {
            "lat": "test",
            "lng": "test"
        }
        return data

    def get_html(self) -> str:
        self.get_data()
        return self.gmap.get()

    def main(self, rtype: str) -> Tuple[Union[str, dict], int]:
        if rtype == "json": return {"ok", "ok"}, 200
        elif rtype == "html": return self.get_html(), 200
        else: return "Unsupported", 400

if __name__ == "__main":
    mapper = Mapper()
    
