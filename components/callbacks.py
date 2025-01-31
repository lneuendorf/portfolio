from dash import Input, Output, State

def register_callbacks(app):
    app.clientside_callback(
        """
        function(n_clicks, is_open) {
            if (n_clicks) {
                return !is_open;
            }
            return is_open;
        }
        """,
        Output("navbar-collapse", "is_open"),
        [Input("navbar-toggler", "n_clicks")],
        [State("navbar-collapse", "is_open")]
    )