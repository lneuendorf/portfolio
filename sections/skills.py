from dash import html
import dash_bootstrap_components as dbc

skills = dbc.Row([
    dbc.Col([
        html.H2("Skills", style={"margin-bottom": "20px", "font-size": "28px", "font-weight": "bold"}),
        dbc.Row([
            dbc.Col([
                html.H4("Programming Languages", className="text-dark"),
                html.Ul([
                    html.Li("Python"),
                    html.Li("SQL"),
                    html.Li("C++"),
                    html.Li("Java"),
                    html.Li("R"),
                    html.Li("Matlab"),
                ], className="text-dark"),
            ], lg=4),
            dbc.Col([
                html.H4("Machine Learning", className="text-dark"),
                html.Ul([
                    html.Li("scikit-learn"),
                    html.Li("XGBoost"),
                    html.Li("PYMC"),
                    html.Li("Pytorch"),
                    html.Li("Numpy"),
                    html.Li("Pandas"),
                ], className="text-dark"),
            ], lg=4),
            dbc.Col([
                html.H4("Data Visualization", className="text-dark"),
                html.Ul([
                    html.Li("PowerBI"),
                    html.Li("Tableau"),
                    html.Li("Dash Plotly"),
                    html.Li("Matplotlib"),
                    html.Li("Seaborn"),
                ], className="text-dark"),
            ], lg=4),
        ], className="mb-4"),
    ], lg=8)
], justify="center", className="d-flex flex-wrap", style={
    "padding-left": "20px", 
    "padding-right": "20px", 
    "padding-top": "40px", 
    "background-color": "#e6eaea",
    "color": "black",  
    "border-radius": "10px", 
})