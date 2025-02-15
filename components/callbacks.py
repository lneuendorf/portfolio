import dash
from dash import Input, Output, State

def register_callbacks(app):
    @app.callback(
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")]
    )
    def toggle_navbar(n_clicks, is_open):
        if n_clicks:
            return not is_open
        return is_open
    
    @app.callback(
        Output('video-player', 'play'),
        Input('video-interval', 'n_intervals')
    )
    def play_video(n_intervals):
        if n_intervals == 1:
            return True
        return False
    
    @app.callback(
        [Output("collapse-masters", "is_open"), Output("collapse-button-masters", "children")],
        [Input("collapse-button-masters", "n_clicks")],
        [State("collapse-masters", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"
    
    @app.callback(
        [Output("collapse-masters-lg", "is_open"), Output("collapse-button-masters-lg", "children")],
        [Input("collapse-button-masters-lg", "n_clicks")],
        [State("collapse-masters-lg", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"
    
    @app.callback(
        [Output("collapse-bachelors", "is_open"), Output("collapse-button-bachelors", "children")],
        [Input("collapse-button-bachelors", "n_clicks")],
        [State("collapse-bachelors", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"
    
    @app.callback(
        [Output("collapse-bachelors-lg", "is_open"), Output("collapse-button-bachelors-lg", "children")],
        [Input("collapse-button-bachelors-lg", "n_clicks")],
        [State("collapse-bachelors-lg", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"
    
    @app.callback(
        [Output("collapse-data-eng", "is_open"), Output("collapse-button-data-eng", "children")],
        [Input("collapse-button-data-eng", "n_clicks")],
        [State("collapse-data-eng", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"

    @app.callback(
        [Output("collapse-data-eng-lg", "is_open"), Output("collapse-button-data-eng-lg", "children")],
        [Input("collapse-button-data-eng-lg", "n_clicks")],
        [State("collapse-data-eng-lg", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"

    @app.callback(
        [Output("collapse-data-science", "is_open"), Output("collapse-button-data-science", "children")],
        [Input("collapse-button-data-science", "n_clicks")],
        [State("collapse-data-science", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"

    @app.callback(
        [Output("collapse-data-science-lg", "is_open"), Output("collapse-button-data-science-lg", "children")],
        [Input("collapse-button-data-science-lg", "n_clicks")],
        [State("collapse-data-science-lg", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"

    @app.callback(
        [Output("collapse-marathon", "is_open"), Output("collapse-button-marathon", "children")],
        [Input("collapse-button-marathon", "n_clicks")],
        [State("collapse-marathon", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"

    @app.callback(
        [Output("collapse-marathon-lg", "is_open"), Output("collapse-button-marathon-lg", "children")],
        [Input("collapse-button-marathon-lg", "n_clicks")],
        [State("collapse-marathon-lg", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"

    @app.callback(
        [Output("collapse-teaching", "is_open"), Output("collapse-button-teaching", "children")],
        [Input("collapse-button-teaching", "n_clicks")],
        [State("collapse-teaching", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"

    @app.callback(
        [Output("collapse-teaching-lg", "is_open"), Output("collapse-button-teaching-lg", "children")],
        [Input("collapse-button-teaching-lg", "n_clicks")],
        [State("collapse-teaching-lg", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            return not is_open, "-" if not is_open else "+"
        return is_open, "+"
    
    @app.callback(
        [Output("collapse-nfl-25", "is_open"), 
        Output("collapse-button-nfl-25", "children"), 
        Output("brief-synopsis-nfl-25", "style")],  # Hide/show brief synopsis
        [Input("collapse-button-nfl-25", "n_clicks")],
        [State("collapse-nfl-25", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            # Toggle collapse and button text
            return not is_open, "-" if not is_open else "+", {"display": "none"} if not is_open else {"display": "block"}
        return is_open, "+", {"display": "block"}
    
    @app.callback(
        [Output("collapse-nfl-24", "is_open"), 
        Output("collapse-button-nfl-24", "children"),
        Output("brief-synopsis-nfl-24", "style")],  # Hide/show brief synopsis
        [Input("collapse-button-nfl-24", "n_clicks")],
        [State("collapse-nfl-24", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            # Toggle collapse and button text
            return not is_open, "-" if not is_open else "+", {"display": "none"} if not is_open else {"display": "block"}
        return is_open, "+", {"display": "block"}
    
    @app.callback(
        [Output("collapse-low-resource-mt", "is_open"),
        Output("collapse-button-low-resource-mt", "children"),
        Output("brief-synopsis-low-resource-mt", "style")],  # Hide/show brief synopsis
        [Input("collapse-button-low-resource-mt", "n_clicks")],
        [State("collapse-low-resource-mt", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            # Toggle collapse and button text
            return not is_open, "-" if not is_open else "+", {"display": "none"} if not is_open else {"display": "block"}
        return is_open, "+", {"display": "block"}
    
    @app.callback(
        [Output("collapse-sanguage", "is_open"),
        Output("collapse-button-sanguage", "children"),
        Output("brief-synopsis-sanguage", "style")],  # Hide/show brief synopsis
        [Input("collapse-button-sanguage", "n_clicks")],
        [State("collapse-sanguage", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            # Toggle collapse and button text
            return not is_open, "-" if not is_open else "+", {"display": "none"} if not is_open else {"display": "block"}
        return is_open, "+", {"display": "block"}
    

    @app.callback(
        [Output("collapse-ffcrystalball", "is_open"),
        Output("collapse-button-ffcrystalball", "children"),
        Output("brief-synopsis-ffcrystalball", "style")],  # Hide/show brief synopsis
        [Input("collapse-button-ffcrystalball", "n_clicks")],
        [State("collapse-ffcrystalball", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            # Toggle collapse and button text
            return not is_open, "-" if not is_open else "+", {"display": "none"} if not is_open else {"display": "block"}
        return is_open, "+", {"display": "block"}

    @app.callback(
        [Output("collapse-octoberodds", "is_open"),
        Output("collapse-button-octoberodds", "children"),
        Output("brief-synopsis-octoberodds", "style")],  # Hide/show brief synopsis
        [Input("collapse-button-octoberodds", "n_clicks")],
        [State("collapse-octoberodds", "is_open")],
    )
    def toggle_collapse(n_clicks, is_open):
        if n_clicks:
            # Toggle collapse and button text
            return not is_open, "-" if not is_open else "+", {"display": "none"} if not is_open else {"display": "block"}
        return is_open, "+", {"display": "block"}