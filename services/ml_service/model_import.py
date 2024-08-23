TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000
import mlflow
from mlflow import MlflowClient
import os 
import joblib

os.environ["MLFLOW_S3_ENDPOINT_URL"] = 'https://storage.yandexcloud.net'
os.environ["AWS_ACCESS_KEY_ID"] = 'YCAJEryDs7iScbshPQ7BaUhes'
os.environ["AWS_SECRET_ACCESS_KEY"] = 'YCMl4tpgidAdLCoZRZ1lURSmOpgRQ12KhwO_tJkr'

mlflow.set_tracking_uri(f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}")
mlflow.set_registry_uri(f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}")


experiment_name = mlflow.get_experiment_by_name('baseline_improvement')

REGISTRY_MODEL_NAME = 'price_prediction_model'

version = '12'

client = MlflowClient()

model_uri = client.get_model_version_download_uri(REGISTRY_MODEL_NAME,version)

model = mlflow.sklearn.load_model(model_uri)

joblib.dump(model,'/home/mle-user/mle_projects/mle-project-sprint-3-v001/services/models/model.pkl')