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
  'http://localhost:...' \
```


## 2. FastAPI микросервис в Docker-контейнере

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

#вероятно, здесь имелось в виду в режиме БЕЗ docker compose (так как в задании написано именно так)
#нужно находится в директории services

```
docker image build . --tag ml_service:1


### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:...' \
```

## 3. Docker compose для микросервиса и системы моониторинга

```bash
# команда перехода в нужную директорию

# команда для запуска микросервиса в режиме docker compose

```

### Пример curl-запроса к микросервису

```bash
curl -X 'POST' \
  'http://localhost:
```

## 4. Скрипт симуляции нагрузки
Скрипт генерирует <...> запросов в течение <...> секунд ...

```
# команды необходимые для запуска скрипта
...
```

Адреса сервисов:
- микросервис: http://localhost:<port>
- Prometheus: ...
- Grafana: ...