import fastapi
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib 
import sys 

class FastApiHandler():

    def __init__(self) -> None:
        
        self.param_types = {
            "user_id": str,
            "model_params": dict
        }
        self.req_model_params = ['build_year', 'building_type_int', 'latitude', 'longitude', 'ceiling_height', 'flats_count', 'floors_total', 'has_elevator', 'floor', 'kitchen_area', 'living_area', 'rooms', 'is_apartment', 'total_area']
        self.model_path = '/home/mle-user/mle_projects/mle-project-sprint-3-v001/services/models/model.pkl'
        self.load_model(model_path = self.model_path)
        
    def load_model(self,model_path:str):

        try:
            self.model = joblib.load(model_path)
        except Exception as e:
            print(f"Failed to load model: {e}")
    
    def predict(self, model_params):
        return self.model.predict(model_params)
    
    def check_query_params(self, query_params):
        print(type(query_params["model_params"]))
        if "user_id" not in query_params or "model_params" not in query_params:
            return False
                
        if not isinstance(query_params["user_id"], self.param_types["user_id"]):
            print('error_user_id')
            return False
                
        if not isinstance(query_params["model_params"], self.param_types["model_params"]):
            print('error_model_params')
            return False
        return True
    
    def check_model_params(self, model_params):
        
        if set(model_params.keys()) == set(self.req_model_params):
            
            return True
        
        return False
    
    def validate_params(self, params):
        if self.check_query_params(params):
            print("all params exists")
        else:
            print("problems with query params")
            return False
        if self.check_model_params(params['model_params']):
            print("all params exists")
        else:
            print("problems with model_params")
            return False
        
        
        return True
    
    def handle(self,params):
        try:
            if not self.validate_params(params):
                response = {"Error":"Problems with params"}
            else:
                user_id = params["user_id"]
                model_params = params["model_params"]
                pd_model_params = pd.DataFrame(model_params,index=[0])
                predicted_price = float(self.predict(pd_model_params))
                print(predicted_price)
                response = {"user_id":user_id,"prediction":predicted_price}
        except Exception as e:
            print(f"Failed to handle: {e}")
        else:
            return response
