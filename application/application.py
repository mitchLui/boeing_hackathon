# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from mapper import Mapper

app = FastAPI()
mapper = Mapper()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=200)
def root():
    return "app is running"


@app.get("/voice", status_code=200)
def voice():
    response = mapper.main()
    return Response(content=str(response), media_type="application/xml")


if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
