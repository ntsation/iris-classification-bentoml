# Iris Classification with Random Forest and BentoML

This repository contains two Python scripts to train a Random Forest classifier on the Iris dataset and serve the trained model using BentoML.

## Repository Contents

- `model.py`: Script to train the Random Forest classifier and save the model using BentoML.
- `service.py`: Script to create a BentoML service that serves the trained model for making predictions.

## Requirements

Make sure you have the following libraries installed:

- `scikit-learn`
- `bentoml`
- `numpy`

You can install the required libraries using the following command:

```cmd
pip install scikit-learn bentoml numpy
```

## Training the Model

Run the model.py script to train the Random Forest classifier on the Iris dataset and save the model using BentoML.

```cmd
python model.py
```

This will output the accuracy of the model on the test dataset and save the trained model with BentoML.

## Serving the Model

Run the service.py script to create a BentoML service that serves the trained model for making predictions.

```cmd
python service.py
```

This will start a BentoML service that can be used to classify Iris flower data.

## Example Request

To make a prediction, send a POST request to the BentoML service with the Iris flower data in JSON format. Here is an example of how to make a request using curl:

```cmd
curl -X POST -H "Content-Type: application/json" \
    -d '{"data": [[5.1, 3.5, 1.4, 0.2]]}' \
    http://127.0.0.1:5000/classify
```

You should receive a response with the predicted class for the given data.
