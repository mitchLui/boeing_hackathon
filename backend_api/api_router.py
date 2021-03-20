# -*- coding: utf-8 -*-
from loguru import logger

class APIs:

    def __init__(self) -> None:
        pass

    def get_weather(self, location: str) -> dict:
        return {}

    def main(self) -> str:
        return {"ok": "ok"}

if __name__ == "__main__":
    apis = APIs()
    apis.main()