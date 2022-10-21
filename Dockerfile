FROM python:3.10-buster
ENV PYTHONUNBUFFERED=1
WORKDIR /froogle

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .