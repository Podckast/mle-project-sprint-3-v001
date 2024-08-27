# Инструкции по запуску микросервиса

Каждая инструкция выполняется из директории репозитория mle-sprint3-completed
Если необходимо перейти в поддиректорию, напишите соотвесвтующую команду

## 1. FastAPI микросервис в виртуальном окружение
```python
# команды создания виртуального окружения
# и установки необходимых библиотек в него
sudo apt-get install python3.10-venv
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install uvicorn["standard"]
pip install --upgrade fastapi
pip install --upgrade starlette

# команда перехода в директорию
cd services
cd ml_service

#Так как модель весит слишком много и запушить её в гитхаб нельзя, модель придётся импортировать из хранилища 

#Команды установки модели на локальную машину (перед этим надо выйти из директорий ml_service и services)

pip install mlflow
pip install psycorg2-binary
pip install boto3
cd services
sh server.sh
python3 model_import.py







# команда запуска сервиса с помощью uvicorn
```
uvicorn price_app:app  --reload --port 8000 --host 127.0.0.1

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/prices?user_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "build_year": 2001,
    "building_type_int": 2, 
    "latitude": 55.695980, 
    "longitude": 37.811546,
    "ceiling_height": 2.60, 
    "flats_count": 153, 
    "floors_total": 24, 
    "has_elevator": true, 
    "floor": 17,
    "kitchen_area": 10.0, 
    "living_area": 35.000000,
    "rooms": 2,
    "is_apartment": false, 
    "total_area": 58.000000
}'
```


## 2. FastAPI микросервис в Docker-контейнере

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

#вероятно, здесь имелось в виду в режиме БЕЗ docker compose (так как в задании написано именно так)
#нужно находится в директории services

```
docker image build . --tag ml_service:1
docker container run --publish 8000:1702 --env-file .env --volume=./volume:/services/models ml_service:1

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/prices?user_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "build_year": 2001,
    "building_type_int": 2, 
    "latitude": 55.695980, 
    "longitude": 37.811546,
    "ceiling_height": 2.60, 
    "flats_count": 153, 
    "floors_total": 24, 
    "has_elevator": true, 
    "floor": 17,
    "kitchen_area": 10.0, 
    "living_area": 35.000000,
    "rooms": 2,
    "is_apartment": false, 
    "total_area": 58.000000
}'
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию
cd services
# команда для запуска микросервиса в режиме docker compose

docker compose up --build

#Если портов 3000 и 9090 нет, их необходимо указать вручную в ports

```



### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/prices?user_id=123' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "build_year": 2001,
    "building_type_int": 2, 
    "latitude": 55.695980, 
    "longitude": 37.811546,
    "ceiling_height": 2.60, 
    "flats_count": 153, 
    "floors_total": 24, 
    "has_elevator": true, 
    "floor": 17,
    "kitchen_area": 10.0, 
    "living_area": 35.000000,
    "rooms": 2,
    "is_apartment": false, 
    "total_area": 58.000000
}'
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует 50 запросов в течение 130 секунд

```
#команды необходимые для запуска скрипта
cd services
python3 check.py
#Далее следовать инструкции в программе
```

Адреса сервисов:
- микросервис (для первых двух частей проекта): http://127.0.0.1:8000
- микросервис (для 3 части проекта): http://localhost:1702
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000