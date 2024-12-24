from .iris_model import IrisModel

class ModelFactory:
    @staticmethod
    def create_model(model_type: str):
        if model_type.lower() == "iris":
            return IrisModel()
        raise ValueError(f"Unknown model type: {model_type}")