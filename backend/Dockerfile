# syntax = docker/dockerfile:1.0-experimental

FROM python:3.8.7-buster as base

ENV PYTHONWARNINGS ignore
ENV PYTHONUNBUFFERED 1


COPY requirements.txt .

RUN pip install -Ur requirements.txt --quiet

WORKDIR /webapps


FROM base as develop
ENTRYPOINT ["/webapps/entrypoint.sh"]


FROM base as prod
COPY . .
ENTRYPOINT ["/webapps/entrypoint.sh"]
