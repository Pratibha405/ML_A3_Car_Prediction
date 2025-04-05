import dash
from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import joblib
import numpy as np
import pandas as pd
import os
import cloudpickle
import mlflow


# MLflow Setup
mlflow.set_tracking_uri("https://mlflow.ml.brain.cs.ait.ac.th")
os.environ["MLFLOW_TRACKING_USERNAME"] = "admin"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "password"

scaler_path = '../code/model/scaler.dump'
model_name = "st125041-a3-model"
client = mlflow.tracking.MlflowClient()

# Use alias instead of deprecated 'stages' approach
latest_version = client.get_model_version_by_alias(model_name, "staging").version

# Load model using that version
model = mlflow.pyfunc.load_model(model_uri=f"models:/{model_name}/{latest_version}")
scaler = cloudpickle.load(open(scaler_path, 'rb'))

# Feature columns and default values
num_cols = ['year', 'mileage', 'max_power']
default_vals = {'year': 2014.00, 'mileage': 21.14, 'max_power': 103.52}

# Price labels
y_map = {0: 'cheap', 1: 'average', 2: 'expensive', 3: 'very expensive'}

def get_X(year, mileage, max_power):
    features = {'year': year,
                'mileage': mileage,
                'max_power': max_power}
    
    # Ensure valid feature inputs and replace with default if necessary
    for feature in features:
        if not features[feature]:  # Blank input
            features[feature] = default_vals[feature]
        elif feature in num_cols and features[feature] < 0:  # Negative numerical input
            features[feature] = default_vals[feature]

    # Convert features to DataFrame for consistency
    X = pd.DataFrame(features, index=[0])
    
    return X, features

def get_y(X):
    # Ensure the model returns a single prediction value
    return model.predict(X)

def calculate_selling_price(year, mileage, max_power, submit):
    # Get scaled features and the corresponding original features
    X, features = get_X(year, mileage, max_power)
    
    # Predict the class label for the selling price category
    y = get_y(X)[0]
    
    # Return the selling price message along with the original feature values
    return [f"Selling price is: {y_map[y]}"] + list(features.values())