# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from api_router import API_router

app = FastAPI()
apis = API_router()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return PlainTextResponse("app is running", 200)


@app.get("/weather")
async def weather():
    response, status_code = apis.get_weather()
    return JSONResponse(response, status_code)


@app.get("/vessel_history")
async def get_vessel_history(imo: str = None, mmsi: str = None, days: str = None):
    response, status_code = apis.get_vessel_history(imo, mmsi, days)
    return JSONResponse(response, status_code)


@app.get("/location_data")
async def get_location_data(
    radius: str,
    lat: str = None,
    lon: str = None,
    uuid: str = None,
    mmsi: str = None,
    imo: str = None,
    port_uuid: str = None,
    port_unlocode: str = None,
):
    response, status_code = apis.get_location_data(
        radius, lat, lon, uuid, mmsi, imo, port_uuid, port_unlocode
    )
    return JSONResponse(response, status_code)


@app.get("/port")
async def get_port(
    name: str = None,
    country_iso: str = None,
    port_type: str = None,
    fuzzy: int = None,
    lat: str = None,
    lon: str = None,
    radius: str = None,
):
    response, status_code = apis.get_port(
        name, country_iso, port_type, fuzzy, lat, lon, radius
    )
    return JSONResponse(response, status_code)


@app.get("/track_vessel")
async def ship_tracker(uuid: str = None, mmsi: str = None, imo: str = None):
    response, status_code = apis.ship_tracker(uuid, mmsi, imo)
    return JSONResponse(response, status_code)


@app.get("/vessel_info")
async def get_vessel_info(uuid: str = None, mmsi: str = None, imo: str = None):
    response, status_code = apis.get_vessel_info(uuid, mmsi, imo)
    return JSONResponse(response, status_code)


@app.get("/search_vessel")
async def search_vessel(
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
    response, status_code = apis.search_vessel(
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
    return JSONResponse(response, status_code)


if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
