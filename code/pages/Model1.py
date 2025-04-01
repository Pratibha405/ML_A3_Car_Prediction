import dash
from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import joblib  # For loading the trained model
import numpy as np  # For numerical operations
import pandas as pd


dash.register_page(__name__, path="/Model1")

# Load model
model1 = joblib.load('./model/car_price_model.model')  # Adjust the path if needed

layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H1("Car Price Prediction (Model 1)", className="text-center"),
            html.P("Enter values for year, mileage, and max power to predict car prices.", className="text-center"),
            
            # Form inputs for year, mileage, and max power
            html.Div([
                dbc.Label("Year", html_for="x_1"),
                dbc.Input(id="x_1", type="number", placeholder="Enter year"),
                dbc.FormText("This is the value for year", color="secondary"),
            ], className="mb-3"),

            html.Div([
                dbc.Label("Mileage", html_for="x_2"),
                dbc.Input(id="x_2", type="number", placeholder="Enter mileage"),
                dbc.FormText("This is the value for mileage", color="secondary"),
            ], className="mb-3"),

            html.Div([
                dbc.Label("Max Power (bhp)", html_for="x_3"),
                dbc.Input(id="x_3", type="number", placeholder="Enter max power"),
                dbc.FormText("This is the value for max power (bhp)", color="secondary"),
            ], className="mb-3"),

            # Prediction button and output
            html.Div([
                dbc.Button(id="submit_model", children="Calculate Price", color="primary", className="me-1"),
                dbc.Label("Predicted Price: "),
                html.Div(id="y_model1", children=""),
            ], style={'marginTop': '10px'})
        ], width=6),
        className="d-flex justify-content-center align-items-center", style={"minHeight": "100vh"}
    )
], fluid=True)

# Callback for model prediction
@callback(
    Output("y_model1", "children"),  # Unique ID here
    [State("x_1", "value"), State("x_2", "value"), State("x_3", "value")],
    Input("submit_model", "n_clicks"),
    prevent_initial_call=True
)
def calculate_y_model(x_1, x_2, x_3, submit):
    if None in [x_1, x_2, x_3]:
        return "Please enter all values"
    
    try:
        # Ensure inputs are in the correct format
        features = pd.DataFrame([[x_1, x_2, x_3]], columns=["year", "mileage", "max_power"])
        
        # Predict using Model 1
        prediction = model1.predict(features)
        
        # Reverse log transformation if applied
        predicted_price = np.exp(prediction[0])
        
        return f"The predicted car price = {predicted_price:.2f} Baht"
    
    except Exception as e:
        return f"An error occurred: {e}"
    
