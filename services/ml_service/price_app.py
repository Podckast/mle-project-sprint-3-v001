from fastapi import FastAPI
import pandas as pd
import json 
import pandas as pd
import joblib 
import sys
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Histogram
from prometheus_client import Counter


sys.path.append('/home/mle-user/mle_projects/mle-project-sprint-3-v001/services')

from ml_service.model_handler import FastApiHandler

 


app = FastAPI()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

ml_app_predictions = Histogram(
    # имя метрики
    "ml_app_predictions",
    #описание метрики
    "Histogram of predictions",
    #указаываем корзины для гистограммы
    buckets=(1, 2, 4, 5, 10)
)

ml_app_counter_pos = Counter("ml_app_counter_pos", "Count of positive predictions")

app.handler = FastApiHandler()


@app.post("/api/prices")
def get_prediction(user_id: str, model_params: dict):
    print(type(model_params))
    all_params = {"user_id": user_id, "model_params": model_params}
    prediction = app.handler.handle(all_params)
    ml_app_predictions.observe(prediction['prediction'])
    if prediction['prediction'] > 0:
        ml_app_counter_pos.inc()

    return prediction