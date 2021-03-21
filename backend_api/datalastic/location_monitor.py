# -*- coding: utf-8 -*-
from . import main


class Location_monitor(main.Datalastic):
    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        self.endpoint = "api/v0/vessel_inradius"

    def get_location_by_lat_lon(self, radius, lat, lon):
        parameters = {"api-key": self.api_key, "lat": lat, "lon": lon, "radius": radius}
        return self._get_results(f"{self.url}{self.endpoint}", params=parameters)

    def get_location_by_uuid(self, radius: str, uuid: str):
        parameters = {"api-key": self.api_key, "radius": radius, "uuid": uuid}
        return self._get_results(f"{self.url}{self.endpoint}", params=parameters)

    def get_location_by_mmsi(self, radius: str, mmsi: str):
        parameters = {"api-key": self.api_key, "radius": radius, "mmsi": mmsi}
        return self._get_results(f"{self.url}{self.endpoint}", params=parameters)

    def get_location_by_imo(self, radius: str, imo: str):
        parameters = {"api-key": self.api_key, "radius": radius, "imo": imo}
        return self._get_results(f"{self.url}{self.endpoint}", params=parameters)

    def get_location_by_port_uuid(self, radius: str, uuid: str):
        parameters = {"api-key": self.api_key, "radius": radius, "port_uuid": uuid}
        return self._get_results(f"{self.url}{self.endpoint}", params=parameters)

    def get_location_by_port_unlocode(self, radius: str, port_unlocode: str):
        parameters = {
            "api-key": self.api_key,
            "radius": radius,
            "port_unlocode": port_unlocode,
        }
        return self._get_results(f"{self.url}{self.endpoint}", params=parameters)


if __name__ == "__main__":
    api = Location_monitor()
