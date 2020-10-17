FROM python:3.8.5-slim-buster
ARG LINK_PYTHON_TO_PYTHON3=1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
RUN mkdir app
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY .env /app/
COPY . /app/
