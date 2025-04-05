import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from linearRegressionA3 import Normal,Ridge,RidgePenalty
from dash.dependencies import Input, Output

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
from pages.home import *

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Car Model A1", href="/Model1")),
        dbc.NavItem(dbc.NavLink("Car Model A3", href="/Model3")),
    ],
    brand="ML2025 Car Prediction Model",
    brand_href="/",
    color="primary",
    dark=True,
)

# Main layout
app.layout = html.Div([
    navbar,
    dash.page_container 
])

if __name__ == '__main__':
    app.run(debug=True)