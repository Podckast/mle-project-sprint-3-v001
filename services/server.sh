export MLFLOW_S3_ENDPOINT_URL=https://storage.yandexcloud.net
export AWS_ACCESS_KEY_ID=YCAJEryDs7iScbshPQ7BaUhes
export AWS_SECRET_ACCESS_KEY=YCMl4tpgidAdLCoZRZ1lURSmOpgRQ12KhwO_tJkr
export AWS_BUCKET_NAME=s3-student-mle-20240523-9a4b29d5bb


mlflow server \
  --registry-store-uri postgresql://mle_20240523_9a4b29d5bb:6829393035904b068e86b9d3e2bc2f6d@rc1b-uh7kdmcx67eomesf.mdb.yandexcloud.net:6432/playground_mle_20240523_9a4b29d5bb \
  --default-artifact-root s3://s3-student-mle-20240523-9a4b29d5bb \
  --backend-store-uri postgresql://mle_20240523_9a4b29d5bb:6829393035904b068e86b9d3e2bc2f6d@rc1b-uh7kdmcx67eomesf.mdb.yandexcloud.net:6432/playground_mle_20240523_9a4b29d5bb \
  --no-serve-artifacts