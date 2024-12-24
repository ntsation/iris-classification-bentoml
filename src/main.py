import bentoml
from models.model_factory import ModelFactory
from data.data_loader import DataLoader
from data.data_preprocessor import DataPreprocessor
from config.config import Config

def train_and_save_model():
    # Create model instance
    model = ModelFactory.create_model(Config.MODEL_TYPE)
    
    # Load and preprocess data
    X, y = DataLoader.load_iris_data()
    X = DataPreprocessor.preprocess_input(X)
    
    # Train model
    model.train(X, y)
    
    # Save model using BentoML
    with bentoml.models.create("iris_sklearn") as bento_model:
        model.save(bento_model.path_of("model.pkl"))
    print(f"Model saved: {bento_model}")

if __name__ == "__main__":
    train_and_save_model()