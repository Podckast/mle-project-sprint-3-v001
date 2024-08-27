from fastapi import FastAPI
import pandas as pd
import json 
import pandas as pd
import joblib 
import sys
from prometheus_fastapi_instrumentator import Instrumentator

sys.path.append('/home/mle-user/mle_projects/mle-project-sprint-3-v001/services')

from ml_service.model_handler import FastApiHandler

 


app = FastAPI()

instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)


app.handler = FastApiHandler()
@app.post("/api/prices")
def get_prediction(user_id: str, model_params: dict):
    print(type(model_params))
    all_params = {"user_id": user_id, "model_params": model_params}
    prediction = app.handler.handle(all_params)
    print(type(prediction))
    return prediction