import bentoml
from bentoml.io import JSON
import numpy as np

iris_model = bentoml.sklearn.get('iris_rf_model:latest')

svc = bentoml.Service('iris_classifier', runners=[iris_model.to_runner()])


@svc.api(input=JSON(), output=JSON())
async def classify(data):
    input_array = np.array(data['data'])
    prediction = await svc.runners[0].predict.async_run(input_array)
    return {'prediction': prediction.tolist()}
