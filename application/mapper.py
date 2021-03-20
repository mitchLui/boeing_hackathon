# -*- coding: utf-8 -*-
from loguru import logger
from typing import Tuple
import gmplot

class Mapper:

    def __init__(self) -> None:
        pass

    def main(self, rtype: str) -> Tuple(str | dict, int):
        if rtype == "json": return {"ok", "ok"}, 200
        elif rtype == "html": return "ok", 200
        else: return "Unsupported", 400

if __name__ == "__main":
    mapper = Mapper()
    
