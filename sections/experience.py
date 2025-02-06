from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

experience = (
    dbc.Row([
        html.H2(
            "Relevant Experience",
            style={
                "margin-bottom": "30px",
                "font-size": "36px",  # Default font size for xs screens
                "font-weight": "bold",
                "max-width": CONFIG['max-width'],
                "margin": "0 auto",
                "padding-bottom": "20px",
                "color": CONFIG['text-dark'],
            },
            className="text-center d-none d-sm-block"  # Hide on xs screens
        ),
        html.H2(
            "Relevant Experience",
            style={
                "margin-bottom": "30px",
                "font-size": "32px",  # Font size for sm screens and larger
                "font-weight": "bold",
                "max-width": CONFIG['max-width'],
                "margin": "0 auto",
                "padding-bottom": "20px",
                "color": CONFIG['text-dark'],
            },
            className="text-center d-block d-sm-none"  # Show only on xs screens
        ),

         # Divider Line
        html.Hr(style={"border-top": f"2px solid {CONFIG['text-dark']}", "width": "100%", "max-width": CONFIG['max-width']}),

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
                                className="text-md-start text-center",
                                style={"color": CONFIG['text-dark']}
                            ), sm=12, md=6
                        ),
                        dbc.Col(
                            html.H4(
                                "Jan 2024 – Present", 
                                className="text-md-end text-center date-text",
                                style={"color": CONFIG['text-dark']}
                            ), sm=12, md=6
                        ),
                    ]),
                    html.Ul([
                        html.Li("Developed a process-based model to classify late orders by cause, "
                                "deployed it to Azure Kubernetes Service, and automated reason tagging"
                                 " of daily late orders."),
                        html.Li("Upgraded a legacy Java data pipeline for appointment scheduling "
                                "model to Python using VSCode, GitHub Copilot, and SQL."),
                        html.Li("Created API’s using Flask."),
                    ], style={"color": CONFIG['text-dark']}),
                ], sm=12, md=10),
            ],
            style={"max-width": CONFIG['max-width']}, 
            className="w-100 justify-content-center align-items-center"),
        ], xs=12, sm=12, md=12, lg=12, xl=12,
        className="d-flex align-items-center justify-content-center"),

        # Divider Line
        html.Div(style={"height": "10px"}),
        html.Hr(style={"border-top": f"2px solid {CONFIG['text-dark']}", "width": "100%", "max-width": CONFIG['max-width']}),

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
                                className="text-md-start text-center",
                                style={"color": CONFIG['text-dark']}
                            ), sm=12, md=6
                        ),
                        dbc.Col(
                            html.H4(
                                "May 2023 – Aug 2023",
                                className="text-md-end text-center date-text",
                                style={"color": CONFIG['text-dark']}
                            ), sm=12, md=6
                        ),
                    ]),
                    html.Ul([
                        html.Li("Implemented image filtering pipeline to count semi-truck trailers "
                                "in satellite images. Achieved 72% accuracy on test set."),
                        html.Li("Developed an XGBoost model to predict the probability of direct "
                                "bookings on the Schneider freight app, bypassing brokers."),
                        html.Li("Created PowerBI and Tableau dashboards for 170+ associates, enhancing "
                                "driver training, customer resolutions, and staffing."),
                        html.Li("Automated data processes with Python and SQL."),
                    ], style={"color": CONFIG['text-dark']}),
                ], sm=12, md=10),
            ],
            style={"max-width": CONFIG['max-width']}, 
            className="w-100 justify-content-center align-items-center"),
        ], xs=12, sm=12, md=12, lg=12, xl=12,
        className="d-flex align-items-center justify-content-center"),

        # Divider Line
        html.Div(style={"height": "10px"}),
        html.Hr(style={"border-top": f"2px solid {CONFIG['text-dark']}", "width": "100%", "max-width": CONFIG['max-width']}),

        # Teaching Assistant - UW Madison
        dbc.Col([
            dbc.Row([
            dbc.Col([
                html.Img(
                src="/assets/uw-madison-logo.png", 
                className="img-fluid", 
                style={"max-width": "160px", "height": "auto", "margin-bottom": "20px"}
                )
            ], sm=12, md=2, className="align-self-center", style={"text-align": "center"}),

            dbc.Col([
                dbc.Row([
                dbc.Col(
                    html.H4(
                    "Teaching Assistant · UW-Madison", 
                    className="text-md-start text-center",
                    style={"color": CONFIG['text-dark']}
                    ), sm=12, md=6
                ),
                dbc.Col(
                    html.H4(
                    "Aug 2021 – Dec 2021", 
                    className="text-md-end text-center date-text",
                    style={"color": CONFIG['text-dark']}
                    ), sm=12, md=6
                ),
                ]),
                html.Ul([
                html.Li("Provided hands-on support to over 80 students, ensuring "
                    "comprehension of circuit analysis concepts, and honing skills "
                    "in communication, critical thinking, and instructional guidance."),
                ], style={"color": CONFIG['text-dark']}),
            ], sm=12, md=10),
            ],
            style={"max-width": CONFIG['max-width']}, 
            className="w-100 justify-content-center align-items-center"),
        ], xs=12, sm=12, md=12, lg=12, xl=12,
        className="d-flex align-items-top justify-content-center"),

        # Divider Line
        html.Div(style={"height": "10px"}),
        html.Hr(style={"border-top": f"2px solid {CONFIG['text-dark']}", "width": "100%", "max-width": CONFIG['max-width']}),
        html.Div(style={"height": "5px"}),
    ],
    style={
        "padding-left": CONFIG['padding-left'],
        "padding-right": CONFIG['padding-right'],
        "padding-top": "40px",
        "padding-bottom": "20px",
        "background-color": "white",
        "color": CONFIG['text-dark'],
        "justify-content": "center",
        "align-items": "center",
        "margin": "0 auto",
    },
    id="experience")
)