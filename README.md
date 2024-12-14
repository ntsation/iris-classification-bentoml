# Iris Classifier with BentoML

This repository contains a simple iris classification service using an SVM model trained with the Iris dataset. The service is packaged and served using BentoML, making it easy to implement and deploy machine learning models.

## Project Files

- **model.py**: Trains and saves the SVM model using the Iris dataset.
- **service.py**: Defines the BentoML service that loads the trained model and provides an API for making predictions.
- **dockerfile**: Contains instructions for building the Docker image for the service.
- **bentofile.yaml**: BentoML-specific settings, including service and dependencies.
- **requirements.txt**: Lists the dependencies required for the project.

## How to Run the Service

### 1. Prepare the Environment

Make sure you have [Docker](https://www.docker.com/get-started) and [BentoML](https://bentoml.ai/docs/installation) installed in your environment.

### 2. Install Dependencies

Create a virtual environment and install the dependencies:

```bash
# Create a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate # For Linux/macOS
venv\Scripts\activate # For Windows

# Install dependencies
pip install -r requirements.txt
```

### 3. Train the Model

The SVM model is automatically trained when running the `model.py` script. Just run the following command:

```bash
python model.py
```

This will create an SVM model using the Iris dataset and save it to BentoML.

### 4. Serving the Model

To run the service and explore port 3000, you can use the BentoML command:

```bash
bentoml serves service.py
```

### 5. Build and Run with Docker

If you prefer to use Docker, follow these steps:

1. Build a Docker image:

```bash
docker build -t iris classifier.
```

2. Run the Docker container:

```bash
docker run -p 3000:3000 iris classifier
```

The service will be available at `http://localhost:3000`.

##API

### End point: `/sort`

This endpoint receives an array of characteristics from an Iris flower and returns the predicted class.

**Method:** `POST`  
**Request Body (JSON):**
```json
{
  "input_series": [[5.2, 2.3, 5.0, 0.7]]
}
```

**Response (JSON):**
```json
[2]
```

The answer will be the predicted class (0, 1 or 2), which represents the three species in the Iris dataset (Setosa, Versicolor and Virginica).

##Repository Structure

```plain text
/
├── bentofile.yaml # BentoML configuration file
├── dockerfile # Dockerfile to package and run the service
├── model.py # Script to train and save the model
├── requirements.txt # Python Dependencies
├── readme.md # This file
└── service.py #BentoML service definition
```


## Dependencies

- `bentoml`: Framework for packaging and serving machine learning models.
- `scikit-learn`: Library for machine learning.
- `joblib`: Library for model serialization.
- `pydantic`: Library for data validation and schema definition.