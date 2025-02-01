from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

experience = (
    dbc.Row([
        html.H2(
            "Relevant Work Experience", 
            style={
                "margin-bottom": "30px", 
                "font-size": "32px", 
                "font-weight": "bold",
                "max-width": CONFIG['max-width'], 
                "margin": "0 auto",
                "padding-bottom": "25px",
            },
            className="text-md-start"
        ),

         # Divider Line
        html.Hr(style={"border-top": "2px solid white", "width": "100%", "max-width": CONFIG['max-width']}),
        
        # Data Engineer - Schneider National
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Img(
                        src="/assets/schneider-logo.png", 
                        className="img-fluid", 
                        style={"max-width": "140px", "height": "auto", "margin-bottom": "20px"}
                    )
                ], sm=12, md=2, className="align-self-center", style={"text-align": "center"}),

                dbc.Col([
                    dbc.Row([
                        dbc.Col(
                            html.H4(
                                "Data Engineer · Schneider National", 
                                className="text-light text-md-start text-center"
                            ), sm=12, md=6
                        ),
                        dbc.Col(
                            html.H4(
                                "Jan 2024 – Present", 
                                className="text-light text-md-end text-center date-text"
                            ), sm=12, md=6
                        ),
                    ], className="text-light"),
                    html.Ul([
                        html.Li("Developed a process-based model to classify late orders by cause, "
                                "deployed it to Azure Kubernetes Service, and automated reason tagging"
                                 " of daily late orders."),
                        html.Li("Upgraded a legacy Java data pipeline for appointment scheduling "
                                "model to Python using VSCode, GitHub Copilot, and SQL."),
                        html.Li("Created API’s using Flask."),
                    ], className="text-light"),
                ], sm=12, md=10),
            ],
            style={"max-width": CONFIG['max-width']}, 
            className="w-100 justify-content-center align-items-center"),
        ], xs=12, sm=12, md=12, lg=12, xl=12,
        className="d-flex align-items-center justify-content-center"),

        # Divider Line
        html.Div(style={"height": "10px"}),
        html.Hr(style={"border-top": "2px solid white", "width": "100%", "max-width": CONFIG['max-width']}),

        # Data Science Intern - Schneider National
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    html.Img(
                        src="/assets/schneider-logo.png",
                        className="img-fluid", 
                        style={"max-width": "140px", "height": "auto", "margin-bottom": "20px"}
                    )
                ], sm=12, md=2, className="align-self-center", style={"text-align": "center"}),

                dbc.Col([
                    dbc.Row([
                        dbc.Col(
                            html.H4(
                                "Data Science Intern · Schneider National",
                                className="text-light text-md-start text-center"
                            ), sm=12, md=6
                        ),
                        dbc.Col(
                            html.H4(
                                "May 2023 – Aug 2023",
                                className="text-light text-md-end text-center date-text"
                            ), sm=12, md=6
                        ),
                    ], className="text-light"),
                    html.Ul([
                        html.Li("Implemented image filtering pipeline to count semi-truck trailers "
                                "in satellite images. Achieved 72% accuracy on test set."),
                        html.Li("Developed an XGBoost model to predict the probability of direct "
                                "bookings on the Schneider freight app, bypassing brokers."),
                        html.Li("Created PowerBI and Tableau dashboards for 170+ associates, enhancing "
                                "driver training, customer resolutions, and staffing."),
                        html.Li("Automated data processes with Python and SQL."),
                    ], className="text-light"),
                ], sm=12, md=10),
            ],
            style={"max-width": CONFIG['max-width']}, 
            className="w-100 justify-content-center align-items-center"),
        ], xs=12, sm=12, md=12, lg=12, xl=12,
        className="d-flex align-items-center justify-content-center"),

        # Divider Line
        html.Div(style={"height": "10px"}),
        html.Hr(style={"border-top": "2px solid white", "width": "100%", "max-width": CONFIG['max-width']}),
    
        # Teaching Assistant - UW Madison
        dbc.Col([
            dbc.Row([
            dbc.Col([
                html.Img(
                src="/assets/uw-madison-logo.png", 
                className="img-fluid", 
                style={"max-width": "140px", "height": "auto", "margin-bottom": "20px"}
                )
            ], sm=12, md=2, className="align-self-center", style={"text-align": "center"}),

            dbc.Col([
                dbc.Row([
                dbc.Col(
                    html.H4(
                    "Teaching Assistant · UW-Madison", 
                    className="text-light text-md-start text-center"
                    ), sm=12, md=6
                ),
                dbc.Col(
                    html.H4(
                    "Aug 2021 – Dec 2021", 
                    className="text-light text-md-end text-center date-text"
                    ), sm=12, md=6
                ),
                ], className="text-light"),
                html.Ul([
                html.Li("Provided hands-on support to over 80 students, ensuring "
                    "comprehension of circuit analysis concepts, and honing skills "
                    "in communication, critical thinking, and instructional guidance."),
                ], className="text-light"),
            ], sm=12, md=10),
            ],
            style={"max-width": CONFIG['max-width']}, 
            className="w-100 justify-content-center align-items-center"),
        ], xs=12, sm=12, md=12, lg=12, xl=12,
        className="d-flex align-items-center justify-content-center"),

        # Divider Line
        html.Div(style={"height": "10px"}),
        html.Hr(style={"border-top": "2px solid white", "width": "100%", "max-width": CONFIG['max-width']}),
        html.Div(style={"height": "5px"}),
    ],
    style={
        "padding-left": CONFIG['padding-left'],
        "padding-right": CONFIG['padding-right'],
        "padding-top": "40px",
        "padding-bottom": "20px",
        "background-color": "#333333",
        "color": "white",
        "justify-content": "center",
        "align-items": "center",
        "margin": "0 auto",
    })
)