# -*- coding: utf-8 -*-
from typing import Text
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from mapper import Mapper

app = FastAPI()
mapperAPI = Mapper()

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

@app.get("/map")
async def demo(city: str = "felixstowe"):
    if city not in mapperAPI.port_ids: city = "felixstowe"
    response, code = mapperAPI.main(city)
    return HTMLResponse(response, code)

if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
