FROM python:3.11

WORKDIR /code

COPY src/samdul15food.main.py /code/

RUN pip install --no-cache-dir --upgrade git+https://github.com/EstherCho-7/samdul15food.git@0.1.0/kaishi

CMD ["uvicorn", "main.app", "--host", "0.0.0.0", "--port", "8080"]
