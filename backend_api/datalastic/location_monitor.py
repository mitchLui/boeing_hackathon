# -*- coding: utf-8 -*-
from . import main 

class Location_monitor(main.Datalastic):

    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        self.endpoint = "api/v0/vessel_inradius"
    
    def get_location_by_data(self, radius, lat=None, lon=None, uuid=None, mmsi=None, imo=None, port_uuid=None, port_unlocode=None):
        parameters = {"api-key": self.api_key}
        if radius:
            parameters.update({"radius":radius})
        if lat:
            parameters.update({"lat":lat})
        if lon:
            parameters.update({"lon":lon})
        if uuid:
            parameters.update({"uuid":uuid})
        if mmsi:
            parameters.update({"mmsi":mmsi})
        if imo:
            parameters.update({"imo":imo})
        if port_uuid:
            parameters.update({"port_uuid":port_uuid})
        if port_unlocode:
            parameters.update({"port_unlocode":port_unlocode})
        return self._get_results(f"{self.url}{self.endpoint}", params=parameters)

    


if __name__ == "__main__":
    api = Location_monitor()