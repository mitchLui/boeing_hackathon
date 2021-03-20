# -*- coding: utf-8 -*-
import requests

class Datalastic:

    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
        self.url = "http://api.datalastic.com/"

    def _get_results(self, url: str, params = {}):
        r = requests.get(url=url, params=params)
        results = r.json() if r.status_code == 200 else {}
        return results