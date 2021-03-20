# -*- coding: utf-8 -*-
from . import main


class Vessel_info(main.Datalastic):

    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        self.endpoint = "/api/v0/vessel_info"

    def get_vessel_info_by_imo(self, imo: int):
        parameters = {
            "api-key": self.api_key,
            "imo": imo
        }
        return self._get_results(url=f"{self.url}{self.endpoint}", parameters=parameters)

    def get_vessel_info_by_mmsi(self, mmsi: int):
        parameters = {
            "api-key": self.api_key,
            "mmsi": mmsi
        }
        return self._get_results(url=f"{self.url}{self.endpoint}", parameters=parameters)
    
    def get_vessel_info_by_uuid(self, uuid: str):
        parameters = {
            "api-key": self.api_key,
            "uuid": uuid
        }
        return self._get_results(url=f"{self.url}{self.endpoint}", parameters=parameters)


if __name__ == "__main__":
    api = Vessel_info() 
