from fastapi import FastAPI
from typing import Union
import pickle
import time

app=FastAPI()

@app.get("/")
def read_root():
    return {"hello": "n15"}

@app.get("/food")
def food(name: str):
    # 시간 구하기
    # 음식 이름과 시간을 csv로 저장 -> /code/data/food.csv
    return {"food": name, "time": time}
