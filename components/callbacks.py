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