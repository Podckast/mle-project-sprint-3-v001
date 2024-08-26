FROM python:3.11-slim

LABEL author = ${LABEL}

COPY . ./services 

COPY ./models/model.pkl /home/mle-user/mle_projects/mle-project-sprint-3-v001/services/models/model.pkl

WORKDIR services

RUN pip3 install -r requirements.txt

EXPOSE ${APP_PORT}

VOLUME /models

CMD uvicorn ml_service.price_app:app  --reload --port ${APP_PORT} --host 0.0.0.0