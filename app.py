import dash
import dash_bootstrap_components as dbc
from dash import html
from pages import homepage
from components.navbar import navbar
from components.callbacks import register_callbacks

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.QUARTZ, "/assets/styles.css"],
)

app.title = 'Luke Neuendorf'

# Make navbar fluid, so it spans the entire width
app.layout = html.Div([
    navbar,
    dbc.Col([
        homepage.layout
    ], style={'padding': '20px', 'maxWidth': '2000px', 'margin': '0 auto'})
])

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False)

