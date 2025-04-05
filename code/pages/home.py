import dash
from dash import html
import dash_bootstrap_components as dbc


dash.register_page(__name__, path="/")

layout = html.Div([
    # Title Section
    html.Div([
        html.H1("Welcome to the ML2025 Car Prediction Model", className="text-center mt-4 mb-4 text-primary"),
        html.P(
            "This web app contains two models: A1 and A3, each used to predict car prices using different approaches.",
            className="text-center mb-5", style={'fontSize': '18px', 'color': '#333'}
        ),
    ], className="container"),

    # Model Cards Section
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Model A1: Random Forest", className="card-title text-center fw-semibold text-success"),
                    html.P(
                        "In Model A1, we use Random Forest to predict car prices. The model is evaluated using Mean Squared Error (MSE), which calculates the difference between predicted and actual values.",
                        className="text-center", style={'fontSize': '16px', 'color': '#555'}
                    ),
                ])
            ), width=12, lg=4, className="mb-4"
        ),
        
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Model A3: Classification Approach", className="card-title text-center fw-semibold text-info"),
                    html.P(
                        "In Model A3, we use a classification approach to categorize car prices. The model is evaluated using metrics like Precision, Recall, F1-Score, Accuracy, Macro Average, and Weighted Average. We use Ridge Linear Regression to compute the best model, compare loss, and use that model to predict car prices.",
                        className="text-center", style={'fontSize': '16px', 'color': '#555'}
                    ),
                ])
            ), width=12, lg=4, className="mb-4"
        ),
    ], className="container"),
])