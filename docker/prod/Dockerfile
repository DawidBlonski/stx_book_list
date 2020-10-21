FROM python:3.8.5-slim-buster
ARG LINK_PYTHON_TO_PYTHON3=1
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
WORKDIR /app
RUN apt-get update && apt-get install -y libpq-dev gcc
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN pip install gunicorn==20.0.4 drf-yasg django_heroku
COPY .env /app/
COPY . /app/
CMD python manage.py collectstatic --noinput
CMD make migrate
CMD gunicorn stx_task.wsgi:application --bind 0.0.0.0:$PORT