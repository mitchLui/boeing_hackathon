# -*- coding: utf-8 -*-
from . import main

class Historical_data(main.Datalastic):

    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        self.endpoint = "api/v0/vessel_history" 

    def imo_history(self, imo, days = None):
        parameters = {"api-key": self.api_key, "imo": imo}
        if days:
            parameters.update({"days": days})
        return self._get_results(url=f"{self.url}{self.endpoint}", parameters=parameters)

    def mmsi_history(self, mmsi, days = None):
        parameters = {"api-key": self.api_key, "mmsi": mmsi}
        if days:
            parameters.update({"days": days})
        return self._get_results(url=f"{self.url}{self.endpoint}", parameters=parameters)

    
if __name__ == "__main__":
    api = Historical_data()
