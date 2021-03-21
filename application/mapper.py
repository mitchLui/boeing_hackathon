# -*- coding: utf-8 -*-
from warnings import simplefilter
from loguru import logger
from typing import Tuple, Union
from dotenv import load_dotenv
from concurrent.futures import ThreadPoolExecutor
from random import choice
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

    def get_data_thread(self, iter: list) -> None:
        with ThreadPoolExecutor(max_workers=20) as e:
            results = list(e.map(self.get_data, iter))
        logger.debug(results)
        return results

    def get_data(self, datum: dict) -> Union[list, dict]:
        r = requests.get(datum['url'], datum['params'])
        results = r.json() if r.status_code == 200 else {}
        return results

    def get_port_data(self):
        data = [
            {
                "url": f"{self.config['apis']['url']}{self.config['apis']['endpoints']['port']}",
                "params": {
                    "name": port_id.replace("_"," "),
                    "country_iso": self.config["ports"][port_id]["country"]
                }
            } for port_id in self.port_ids 
        ]
        results = self.get_data_thread(data)
        results = [x["data"][0] for x in results]
        for port_id in self.port_ids:
            for result in results:
                if port_id.replace("_", " ") == result["port_name"].lower():
                    self.config["ports"][port_id].update(result)


    def get_base(self, city_id = "felixstowe") -> str:
        port_data = self.config["ports"].get(city_id, "felixstowe")
        starting_lat = port_data["lat"]
        starting_lng = port_data["lon"]
        gmap = gmplot.GoogleMapPlotter(starting_lat, starting_lng, 14, apikey=self._get_api_key())
        info = f"""<a href='{port_data['website']}' target='_blank'>{port_data['name']}</a>
            <br><b>Latitude</b>: {starting_lat}
            <br><b>Longitude</b>: {starting_lng} 
            <br><b>Unlocode</b>: {port_data['unlocode']}
        """
        gmap.marker(starting_lat, starting_lng, color=port_data["colour"], info_window=info)
        for port in self.config["ports"].values():
            info = f"""<a href='{port['website']}' target='_blank'>{port['name']}</a>
                        <br><b>Latitude</b>: {port['lat']}
                        <br><b>Longitude</b>: {port['lon']} 
                        <br><b>Unlocode</b>: {port['unlocode']}
                    """
            gmap.marker(port["lat"], port["lon"], color=port["colour"], info_window=info, label="P")
        return gmap

    def find_vessels(self, gmap: gmplot.GoogleMapPlotter):
        data = [
            {
                "url": f"{self.config['apis']['url']}{self.config['apis']['endpoints']['location_data']}",
                "params": {
                    "port_unlocode": port["unlocode"],
                    "radius": 50
                }
            } for port in self.config["ports"].values()
        ]
        results = self.get_data_thread(data)
        for result in results:
            if result:
                colours = ["red", "orange", "yellow", "green", "blue", "purple"]
                vessels = result["data"]["vessels"]
                for vessel in vessels:
                    lat = vessel["lat"]
                    lon = vessel["lon"]
                    info = f"""
                    <b>{vessel['name']}</b>
                    <br><b>IMO</b>: {vessel['type']}
                    <br><b>Latitude</b>: {vessel['lat']}
                    <br><b>Longitude</b>: {vessel['lon']}
                    <br><b>Country</b>: {vessel['country_iso']}
                    <br><b>Type</b>: {vessel['type']}
                    <br><b>Speed</b>: {vessel['speed']}
                    <br><b>Course</b>: {vessel['course']}
                    <br><b>Heading</b>: {vessel['heading']}
                    """
                    gmap.marker(lat, lon, choice(colours), info_window=info)
        return gmap.get()

    def main(self, city: str) -> Tuple[Union[str, dict], int]:
        self.get_port_data()
        gmap = self.get_base(city)
        website = self.find_vessels(gmap)
        return website, 200

if __name__ == "__main__":
    mapper = Mapper()
    
