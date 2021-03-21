# -*- coding: utf-8 -*-
from loguru import logger
from dotenv import load_dotenv
from traceback import format_exc
from typing import Tuple
from weather_api.weather_api import Weather_api
from datalastic.historical_data import Historical_data
from datalastic.location_monitor import Location_monitor
from datalastic.port_finder import Port_finder
from datalastic.ship_tracker import Ship_tracker
from datalastic.vessel_info import Vessel_info
from datalastic.vessel_search import Vessel_search
import os


class API_router:
    def __init__(self) -> None:
        self.weather_api = Weather_api(self._get_api_key("OPENWEATHER_KEY"))
        datalastic_key = self._get_api_key("DATALASTIC_KEY")
        self.historical_data = Historical_data(datalastic_key)
        self.location_monitor = Location_monitor(datalastic_key)
        self.port_finder = Port_finder(datalastic_key)
        self.ship_tracker = Ship_tracker(datalastic_key)
        self.vessel_info = Vessel_info(datalastic_key)
        self.vessel_search = Vessel_search(datalastic_key)

    def _get_api_key(self, key: str):
        load_dotenv(verbose=True)
        return os.getenv(key)

    def _generate_error_message(self, message: str):
        error = {"message": message, "success": False}
        return error

    def get_weather(self) -> Tuple[dict, int]:
        weather = self.weather_api.get_weather()
        if weather:
            status_code = 200
        else:
            status_code = 400
        return weather, status_code

    def get_vessel_history(
        self, imo: str = None, mmsi: str = None, days: str = None
    ) -> Tuple[dict, int]:
        status_code = 200
        try:
            if (imo and mmsi) or (not imo and not mmsi):
                status_code = 400
                response = self._generate_error_message()
            elif imo:
                response = self.historical_data.imo_history(imo, days)
            else:
                response = self.historical_data.mmsi_history(mmsi, days)
        except Exception:
            logger.error(format_exc)
            response = self._generate_error_message("GET PORT - API ERROR")
            status_code = 400
        finally:
            return response, status_code

    def get_location_data(
        self,
        radius: str,
        lat: str = None,
        lon: str = None,
        uuid: str = None,
        mmsi: str = None,
        imo: str = None,
        port_uuid: str = None,
        port_unlocode: str = None,
    ):
        status_code = 200
        try:
            if lat and lon:
                response = self.location_monitor.get_location_by_lat_lon(
                    radius, lat, lon
                )
            if uuid:
                response = self.location_monitor.get_location_by_uuid(radius, uuid)
            if mmsi:
                response = self.location_monitor.get_location_by_mmsi(radius, mmsi)
            if imo:
                response = self.location_monitor.get_location_by_imo(radius, imo)
            if port_uuid:
                response = self.location_monitor.get_location_by_port_uuid(
                    radius, port_uuid
                )
            if port_unlocode:
                response = self.location_monitor.get_location_by_port_unlocode(
                    radius, port_unlocode
                )
        except Exception:
            logger.error(format_exc)
            response = self._generate_error_message("GET PORT - API ERROR")
            status_code = 400
        finally:
            return response, status_code

    def get_port(
        self,
        name: str = None,
        country_iso: str = None,
        port_type: str = None,
        fuzzy: int = None,
        lat: str = None,
        lon: str = None,
        radius: str = None,
    ):
        status_code = 200
        response = {}
        try:
            if name or country_iso or fuzzy:
                response = self.port_finder.get_port_by_name(name, country_iso, fuzzy)
            if lat and lon and radius:
                response = self.port_finder.get_port_by_lat_lon_radius(
                    lat, lon, radius, country_iso, port_type
                )
        except Exception:
            logger.error(format_exc())
            response = self._generate_error_message("GET PORT - API ERROR")
            status_code = 400
        finally:
            return response, status_code

    def ship_tracker(self, uuid: str = None, mmsi: str = None, imo: str = None):
        status_code = 200
        try:
            if uuid:
                response = self.ship_tracker.track_vessel_by_uuid(uuid)
            if mmsi:
                response = self.ship_tracker.track_vessel_by_mmsi(mmsi)
            if imo:
                response = self.ship_tracker.track_vessel_by_imo(imo)
        except Exception:
            logger.error(format_exc)
            response = self._generate_error_message("GET PORT - API ERROR")
            status_code = 400
        finally:
            return response, status_code

    def get_vessel_info(self, uuid: str = None, mmsi: str = None, imo: str = None):
        status_code = 200
        try:
            if uuid:
                response = self.vessel_info.get_vessel_info_by_uuid(uuid)
            if mmsi:
                response = self.vessel_info.get_vessel_info_by_mmsi(mmsi)
            if imo:
                response = self.vessel_info.get_vessel_info_by_imo(imo)
        except Exception:
            logger.error(format_exc)
            response = self._generate_error_message("GET PORT - API ERROR")
            status_code = 400
        finally:
            return response, status_code

    def search_vessel(
        self,
        name: str = None,
        fuzzy: int = None,
        port_type: str = None,
        country_iso: str = None,
        gross_tonnage_min: str = None,
        gross_tonnage_max: str = None,
        deadweight_min: str = None,
        deadweight_max: str = None,
        length_min: str = None,
        length_max: str = None,
        breadth_min: str = None,
        breadth_max: str = None,
        year_build_min: str = None,
        year_build_max: str = None,
    ):
        status_code = 200
        try:
            response = self.vessel_search.get_port_by_name(
                name,
                fuzzy,
                port_type,
                country_iso,
                gross_tonnage_min,
                gross_tonnage_max,
                deadweight_min,
                deadweight_max,
                length_min,
                length_max,
                breadth_min,
                breadth_max,
                year_build_min,
                year_build_max,
            )
        except Exception:
            logger.error(format_exc)
            response = self._generate_error_message("GET PORT - API ERROR")
            status_code = 400
        finally:
            return response, status_code


if __name__ == "__main__":
    apis = API_router()
    apis.get_weather()
