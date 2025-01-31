from dash import html
import dash_bootstrap_components as dbc

experience = dbc.Row([
    dbc.Col([
        html.H2("Relevant Work Experience", style={"margin-bottom": "20px", "font-size": "28px", "font-weight": "bold"}),
        dbc.Row([
            dbc.Col([
                html.Img(
                    src="/assets/schneider-logo.png", 
                    className="img-fluid", 
                    style={
                        "max-width": "100%", 
                        "height": "auto", 
                    }
                )
            ], lg=2),
            dbc.Col([
                html.Div([
                    html.H4("Data Engineer at Schneider National (Jan 2024 – Present)", className="text-light"),
                    html.P([
                        "Developed process-based models, upgraded data pipelines, created APIs, deployed to Azure Kubernetes Service."
                    ], className="text-light"),
                ], className="mb-4"),
            ], lg=10),
            dbc.Col([
                html.Img(
                    src="/assets/schneider-logo.png", 
                    className="img-fluid", 
                    style={
                        "max-width": "100%", 
                        "height": "auto", 
                    }
                )
            ], lg=2),
            dbc.Col([
                html.Div([
                    html.H4("Data Science Intern at Schneider National (May 2023 – Aug 2023)", className="text-light"),
                    html.P([
                        "Implemented image filtering pipelines, developed prediction models, created dashboards, automated processes."
                    ], className="text-light"),
                ], className="mb-4"),
            ], lg=10),
            dbc.Col([
                html.Img(
                    src="/assets/schneider-logo.png", 
                    className="img-fluid", 
                    style={
                        "max-width": "100%", 
                        "height": "auto", 
                    }
                )
            ], lg=2),
            dbc.Col([
                html.Div([
                    html.H4("Teaching Assistant at UW-Madison ECE Department (Aug 2021 – Dec 2021)", className="text-light"),
                    html.P([
                        "Taught circuit analysis to over 80 students, focused on communication and critical thinking."
                    ], className="text-light"),
                ], className="mb-4"),
            ], lg=10),
        ], className="mb-4"),
    ], lg=8)
], justify="center", className="d-flex flex-wrap", style={
    "padding-left": "20px",
    "padding-left": "20px",
    "padding-right": "20px",
    "padding-top": "40px",
    "background-color": "#333333",
    "color": "white",
    "border-radius": "10px",
})