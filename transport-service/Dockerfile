ARG ENV=default

FROM python:3.9 AS multi-tenant-default
# QA or PROD env, it should be lightwait.

FROM python:3.9 AS multi-tenant-dev
# DEV env it is useful to have psql installed.

RUN apt-get update && \
  apt-get -y install postgresql postgresql-contrib

FROM multi-tenant-${ENV}
# Include psql executable or nope.

ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
