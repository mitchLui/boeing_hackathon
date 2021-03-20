# -*- coding: utf-8 -*-
from os import stat
from requests import api
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
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


@app.get("/", status_code=200)
async def root():
    return "app is running"

@app.get("/weather", status_code=200)
async def weather():
    response, status_code = apis.get_weather()
    return JSONResponse(response, status_code)


if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
