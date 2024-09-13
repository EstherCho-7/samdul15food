from fastapi import FastAPI
from typing import Union
from datetime import datetime
import time
import os
import csv
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()


app = FastAPI()

origins = [
    "http://ec2-43-203-204-195.ap-northeast-2.compute.amazonaws.com.tiangolo.com",
    "https://ec2-43-203-204-195.ap-northeast-2.compute.amazonaws.com.tiangolo.com",
    "https://samdul15food.web.app",
    "https://samdul15food.web.app:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"hello": "n15"}

@app.get("/food")
def food(name: str):
    # 시간 구하기
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv

    file_path = "/code/data/food.csv"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode='a', newline='') as f:
        writer=csv.writer(f)
        writer.writerow([name, time])

    return {"food": name, "time": time}
