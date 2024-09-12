from fastapi import FastAPI
from typing import Union
import pickle
from datetime import datetime
import time

app=FastAPI()

@app.get("/")
def read_root():
    return {"hello": "n15"}

@app.get("/food")
def food(name: str):
    # 시간 구하기
    time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    return {"food": name, "time": time}
