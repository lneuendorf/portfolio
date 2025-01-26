import dash
import dash_bootstrap_components as dbc
from dash import html
# from pages import homepage
from components import navbar


app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.QUARTZ], #, "/assets/styles.css"],
    # use_pages=True
)

app.title = 'Luke Neuendorf'
app.layout = dbc.Container([
    navbar,
    html.Div(id="page-content")
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=False)

# Callback to handle navbar toggling
@app.callback(
    dash.dependencies.Output("navbar-collapse", "is_open"),
    dash.dependencies.Input("navbar-toggler", "n_clicks"),
    dash.dependencies.State("navbar-collapse", "is_open"),
)
def toggle_navbar(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

# Callback to dynamically update page content
@app.callback(
    dash.dependencies.Output("page-content", "children"),
    [dash.dependencies.Input("url", "pathname")]
)
def display_page(pathname):
    if pathname == "/homepage":
        return homepage.layout
    else:
        return html.Div("404 - Page not found")