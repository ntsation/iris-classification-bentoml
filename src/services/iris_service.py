import bentoml
import numpy as np
from typing_extensions import Annotated
from pydantic import Field
from bentoml.validators import Shape
from .interfaces import ClassifierServiceInterface

@bentoml.service(
    resources={
        "cpu": "1",
        "memory": "2Gi",
    },
)
class IrisClassifierService(ClassifierServiceInterface):
    def __init__(self):
        self.iris_model = bentoml.models.get("iris_sklearn:latest")
        self.model = None
        self._load_model()
    
    def _load_model(self):
        import joblib
        self.model = joblib.load(self.iris_model.path_of("model.pkl"))
    
    @bentoml.api
    def classify(
        self,
        input_series: Annotated[np.ndarray, Shape((-1, 4))] = Field(
            default=[[5.2, 2.3, 5.0, 0.7]]
        ),
    ) -> np.ndarray:
        return self.model.predict(input_series)
