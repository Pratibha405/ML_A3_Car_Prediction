import dash
from dash import Dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from linearRegressionA3 import Normal,Ridge,RidgePenalty

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
from pages.home import *

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Car Model A1", href="/Model1")),
     #   dbc.NavItem(dbc.NavLink("Car Model A2", href="/Model2")),
        dbc.NavItem(dbc.NavLink("Car Model A3", href="/Model3")),
    ],
    brand="ML2025 Car Prediction Model",
    brand_href="/",
    color="primary",
    dark=True,
)


app.layout = html.Div([ 
    navbar,
    
    html.Div([
        html.H1("Welcome to the ML2025 Car Prediction Model", className="text-center mt-4"),
        
        html.P(
            "This web app contains three models: A1, A2, and A3, each used to predict car prices using different approaches.",
            className="text-center"
        ),
        
        html.H4("Model A1: Random Forest (Car Price Prediction A1 Assignment)", className="text-center fw-semibold"),
        html.P(
            "In Model A1, we use Random Forest to predict car prices. The model is evaluated using Mean Squared Error (MSE), which calculates the difference between predicted and actual values.",
            className="text-center"
        ),
        
     #   html.H4("Model A2: Linear Regression (Car Price Prediction A2 Assignment)", className="text-center fw-semibold"),
      #  html.P(
       #     "Model A2 applies Linear Regression to predict car prices. It determines the best model using the regression function and evaluates the model based on its ability to fit the data.",
        #    className="text-center"
        #),
        
        html.H4("Model A3: Classification Approach (Car Price Prediction A3 Assignment)", className="text-center fw-semibold"),
        html.P(
            "In Model A3, we use a classification approach to categorize car prices. The model is evaluated using metrics like Precision, Recall, F1-Score, Accuracy, Macro Average, and Weighted Average. We use Ridge Linear Regression to compute the best model, compare loss, and use that model to predict car prices.",
            className="text-center"
        ),
    ], className="mt-5"),
    
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)