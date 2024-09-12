from fastapi import FastAPI
from typing import Union
from datetime import datetime
import time
import os
import csv

app=FastAPI()

@app.get("/")
def read_root():
    return {"hello": "n15"}

@app.get("/food")
def food(name: str):
    # 시간 구하기
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv

    file_path = "data/food.csv"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode='a', newline='') as f:
        writer=csv.writer(f)
        writer.writerow([name, time])

    return {"food": name, "time": time}
