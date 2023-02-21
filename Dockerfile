FROM python:3.12.0a5-alpine3.17

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]