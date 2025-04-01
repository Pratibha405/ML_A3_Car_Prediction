import dash
from dash import Dash, html, dcc, callback, Output, Input, State
import dash_bootstrap_components as dbc
import joblib
import numpy as np
import pandas as pd
import traceback
from linearRegressionA3 import Normal,Ridge,RidgePenalty

# Initialize Dash app
dash.register_page(__name__, path="/Model3")

# Load trained model and scaler
model3 = joblib.load(r'./model/st125041_a3_model.pkl')
scaler = joblib.load('../code/model/scaler.dump')

# Define layout
layout = dbc.Container([  
    dbc.Row(
        dbc.Col([  # Define the columns in the row
            html.H1("Car Price Prediction", className="text-center"),
            html.P("Enter car details to predict the price and its category.", className="text-center"),
            
            # Input fields for year, mileage, and max power
            dbc.Label("Year"),
            dbc.Input(id="year", type="number", placeholder="Enter year"),
            dbc.FormText("Example: 2015"),
            
            dbc.Label("Mileage (kmpl)"),
            dbc.Input(id="mileage", type="number", placeholder="Enter mileage"),
            dbc.FormText("Example: 18.5"),
            
            dbc.Label("Max Power (bhp)"),
            dbc.Input(id="max_power", type="number", placeholder="Enter max power"),
            dbc.FormText("Example: 100"),
            
            dbc.Button("Predict Price", id="predict_button", color="primary", className="mt-3"),
            
            # Output div for prediction results
            html.Div(id="prediction_output", className="mt-3 text-center fw-bold")
        ], width=6), className="d-flex justify-content-center align-items-center", style={"minHeight": "100vh"}
    )
], fluid=True)

# Callback for prediction
@callback(
    Output("prediction_output", "children"),  # Corrected Output ID to match the layout
    Input("predict_button", "n_clicks"),  # Corrected Input ID to match the layout
    [State("year", "value"), State("mileage", "value"), State("max_power", "value")]  # Corrected State IDs
)
def predict_price(n_clicks_new, year, mileage, max_power):
    # Ensure all values are provided
    ctx = dash.ctx if hasattr(dash, 'ctx') else dash.callback_context
    if not ctx.triggered:
        return "Click a button to predict price."
    if None in [year, mileage, max_power]:
        return "Please provide all input values."

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    model = model3
    
    # Prepare input data
    input_data = pd.DataFrame({
        'year': [year],
        'mileage': [mileage],
        'max_power': [max_power],
    })

    try:
        # Scale the input data using the scaler
        scaled_data = scaler.transform(input_data)  
        pred = model.predict(scaled_data)  # Predict the price category
        pred_price = int(pred[0])  # Convert to integer if needed

        # Map predicted category to a human-readable label
        category_mapping = {
            0: "Category 0: Budget cars",
            1: "Category 1: Affordable cars",
            2: "Category 2: Mid-range cars",
            3: "Category 3: Premium cars"
        }

        category_label = category_mapping.get(pred_price, "Unknown category")
        return f"Predicted Price Category: {category_label}"

    except Exception as e:
        return f"Error in prediction: {e}"