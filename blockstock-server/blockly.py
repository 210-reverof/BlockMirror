from blockstock import *
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import pandas as pd

app = FastAPI()
origins = [
    "http://localhost:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RequestData(BaseModel):
    cmd: str

class ResponseData(BaseModel):
    answer: str

@app.post("/")
async def process_data(request_data: RequestData):
    global trade_signal

    exec(request_data.cmd, globals())
    response_data = {"answer": trade_signal}
    return response_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)