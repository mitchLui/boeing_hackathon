# -*- coding: utf-8 -*-
from . import main


class Ship_tracker(main.Datalastic):
    def __init__(self, api_key) -> None:
        super().__init__(api_key)
        self.endpoint = "api/v0/vessel"

    def track_vessel_by_uuid(self, uuid):
        parameters = {"api-key": self.api_key, "uuid": uuid}
        return self._get_results(
            url=f"{self.url}{self.endpoint}", params=parameters
        )

    def track_vessel_by_mmsi(self, mmsi):
        parameters = {"api-key": self.api_key, "mmsi": mmsi}
        return self._get_results(
            url=f"{self.url}{self.endpoint}", params=parameters
        )

    def track_vessel_by_imo(self, imo):
        parameters = {"api-key": self.api_key, "imo": imo}
        return self._get_results(
            url=f"{self.url}{self.endpoint}", params=parameters
        )


if __name__ == "__main__":
    api = Ship_tracker()
