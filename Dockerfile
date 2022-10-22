FROM python:3.11.0rc2-bullseye
ENV PYTHONUNBUFFERED=1
WORKDIR /froogle

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .