from fastapi import FastAPI
from model_handler import FastApiHandler
import pandas as pd
import json 
app = FastAPI()


all_params = {

        'build_year': 2001,
        'building_type_int': 2, 
        'latitude': 55.695980, 
        'longitude': 37.811546,
        'ceiling_height': 2.60, 
        'flats_count': 153, 
        'floors_total': 24, 
        'has_elevator': True, 
        'floor': 17,
        'kitchen_area': 10.0, 
        'living_area': 35.000000,
        'rooms': 2,
        'is_apartment': False, 
        'total_area': 58.000000
        
}

app.handler = FastApiHandler()
@app.post("/api/prices")
def get_prediction(user_id: str, model_params: dict):
    print(type(model_params))
    all_params = {"user_id": user_id, "model_params": model_params}
    prediction = app.handler.handle(all_params)
    print(type(prediction))
    return prediction

