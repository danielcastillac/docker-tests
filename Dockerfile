FROM python:3.8-slim

WORKDIR /app_folder

COPY requirements.txt .
COPY main.py .

RUN pip3 install -r requirements.txt

CMD ["python3", "./main.py"]