import dash
import dash_bootstrap_components as dbc
from dash import html
import sections
from components.navbar import navbar
from components.footer import footer
from components.callbacks import register_callbacks

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.QUARTZ, "/assets/styles.css"],
)

app.title = 'Luke Neuendorf'

# Make navbar fluid, so it spans the entire width
app.layout = html.Div([
    navbar,
    sections.tldr,
    footer
])

# Register callbacks
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=80)