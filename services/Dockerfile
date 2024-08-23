FROM python:3.11-slim

LABEL author = ${LABEL}

COPY . ./ml_service

COPY ./models/model.pkl /models/model.pkl

WORKDIR ml_service

RUN pip3 install -r requirements.txt

EXPOSE ${APP_PORT}

VOLUME /models


CMD uvicorn ml_service.price_app:app  --reload --port ${APP_PORT} --host 0.0.0.0
