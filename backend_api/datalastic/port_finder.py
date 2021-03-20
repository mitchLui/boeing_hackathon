# -*- coding: utf-8 -*-
from . import main

class Port_finder(main.Datalastic):

    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        self.endpoint = "/api/v0/port_find"
    
    def get_port_by_name_country_port_type(self, name , country_iso, port_type, fuzzy=None):
        parameters = {"api-key": self.api_key, "name": name,  "port_type":port_type, "country_iso": country_iso}
        if fuzzy:
            parameters.update({"fuzzy":fuzzy})
        return self._get_results(url=f"{self.url}{self.endpoint}", parameters=parameters)

    def get_port_by_lat_lon_radius(self, lat, lon, radius, country_iso=None, port_type=None):
        parameters = {"api-key": self.api_key, "lat": lat, "lon":lon,"radius":radius}
        if country_iso:
            parameters.update({"country_iso":country_iso})
        if port_type:
            parameters.update({"port_type":port_type})
        return self._get_results(f"{self.url}{self.endpoint}", parameters)

if __name__ == "__main__":
    api = Port_finder()
