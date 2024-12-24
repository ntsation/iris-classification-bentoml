# Iris Classifier Service

This project implements an iris classification service using BentoML and scikit-learn, following SOLID principles.

## Project Structure

```
src/
├── models/               # Model layer
│   ├── __init__.py
│   ├── interfaces.py     # Abstract interfaces for models
│   ├── iris_model.py     # Iris model implementation
│   └── model_factory.py  # Factory for model creation
├── services/             # Service layer
│   ├── __init__.py
│   ├── interfaces.py     # Service interfaces
│   └── iris_service.py   # Iris service implementation
├── data/                 # Data layer
│   ├── __init__.py
│   ├── data_loader.py    # Data loading
│   └── data_preprocessor.py  # Data preprocessing
├── config/               # Configurations
│   └── config.py
└── main.py               # Entry point
```

## Applied SOLID Principles

1. **Single Responsibility Principle (SRP)**
   - Each class has a single responsibility
   - Clear separation between data, model, and service

2. **Open/Closed Principle (OCP)**
   - Extendable to new models via ModelFactory
   - Interfaces allow new implementations

3. **Liskov Substitution Principle (LSP)**
   - Well-defined interfaces for models and services
   - Implementations are interchangeable

4. **Interface Segregation Principle (ISP)**
   - Small and specific interfaces
   - Clear separation of responsibilities

5. **Dependency Inversion Principle (DIP)**
   - Dependencies injected via interfaces
   - High testability and low coupling

## Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Use

1. **Train the Model**:
```bash
python src/main.py
```

2. **Start the Server**:
```bash
bentoml serve src.services.iris_service:IrisClassifierService --reload
```

3. **Make Predictions**:

## API Endpoints

- **Swagger UI**: http://localhost:3000/docs
- **API Endpoint**: http://localhost:3000/classify
- **Metrics**: http://localhost:3000/metrics# Iris Classifier Service

This project implements an iris classification service using BentoML and scikit-learn, following SOLID principles.

## Project Structure

```
src/
├── models/               # Model layer
│   ├── __init__.py
│   ├── interfaces.py     # Abstract interfaces for models
│   ├── iris_model.py     # Iris model implementation
│   └── model_factory.py  # Factory for model creation
├── services/             # Service layer
│   ├── __init__.py
│   ├── interfaces.py     # Service interfaces
│   └── iris_service.py   # Iris service implementation
├── data/                 # Data layer
│   ├── __init__.py
│   ├── data_loader.py    # Data loading
│   └── data_preprocessor.py  # Data preprocessing
├── config/               # Configurations
│   └── config.py
└── main.py               # Entry point
```

## Applied SOLID Principles

1. **Single Responsibility Principle (SRP)**
   - Each class has a single responsibility
   - Clear separation between data, model, and service

2. **Open/Closed Principle (OCP)**
   - Extendable to new models via ModelFactory
   - Interfaces allow new implementations

3. **Liskov Substitution Principle (LSP)**
   - Well-defined interfaces for models and services
   - Implementations are interchangeable

4. **Interface Segregation Principle (ISP)**
   - Small and specific interfaces
   - Clear separation of responsibilities

5. **Dependency Inversion Principle (DIP)**
   - Dependencies injected via interfaces
   - High testability and low coupling

## Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Use

1. **Train the Model**:
```bash
python src/main.py
```

2. **Start the Server**:
```bash
bentoml serve src.services.iris_service:IrisClassifierService --reload
```

3. **Make Predictions**:

## API Endpoints

- **Swagger UI**: http://localhost:3000/docs
- **API Endpoint**: http://localhost:3000/classify
- **Metrics**: http://localhost:3000/metrics