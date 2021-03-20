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

@app.get("/demo")
async def voice(rtype: str):
    if rtype == "json":
        response, code = mapperAPI.main(rtype)
        return JSONResponse(response, code)
    elif rtype == "html":
        response, code = mapperAPI.main(rtype)
        return HTMLResponse(response, code)
    else:
        response, code = mapperAPI.main(rtype)
        return PlainTextResponse(response, code)


if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
