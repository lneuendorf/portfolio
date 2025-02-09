from dash import html
import dash_bootstrap_components as dbc
from config.config import CONFIG

# Timeline component
timeline = html.Div(
    style={
        "position": "relative",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
        "padding": "40px 0",
    },
    children=[
        # Vertical line
        html.Div(
            style={
                "position": "absolute",
                "left": "50%",
                "width": "2px",
                "height": "100%",
                "background": CONFIG['text-dark'],
                "transform": "translateX(-50%)",
            }
        ),
        # Timeline items
        html.Div(
            [
                # Data Engineer at Schneider
                html.Div(
                    style={
                        "position": "relative",
                        "margin-bottom": "40px",
                        "display": "flex",
                        "align-items": "center",
                    },
                    children=[
                        # Circle with logo
                        html.Div(
                            style={
                                "position": "absolute",
                                "left": "50%",
                                "transform": "translateX(-50%)",
                                "width": "70px",
                                "height": "70px",
                                "border-radius": "50%",
                                "background": "#ff6d39",
                                "display": "flex",
                                "align-items": "center",
                                "justify-content": "center",
                                "z-index": 1,
                                "border": f"2px solid {CONFIG['text-dark']}",
                            },
                            children=[
                                html.Img(
                                    src="/assets/schneider-logo.png",
                                    style={
                                        "width": "80%",
                                        "height": "auto",
                                    },
                                ),
                            ],
                        ),
                        # Job description box
                        html.Div(
                            style={
                                "width": "45%",
                                "margin-left": "55%",
                                "padding": "20px",
                                "background": "white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer
                                html.Div(
                                    style={
                                        "position": "absolute",
                                        "left": "-10px",
                                        "top": "50%",
                                        "transform": "translateY(-50%)",
                                        "width": "0",
                                        "height": "0",
                                        "border-top": "10px solid transparent",
                                        "border-bottom": "10px solid transparent",
                                        "border-right": "10px solid white",
                                    }
                                ),
                                # Job title and date
                                dbc.Row([
                                    html.H3(
                                        "Data Engineer",
                                        className="text-md-start text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "3px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.H6(
                                        "Jan 2024 – Present",
                                        className="text-md-start text-center date-text",
                                        style={"color": CONFIG['text-dark']}
                                    ),
                                ], style={"padding-top": "5px"}),
                                # Job description
                                html.Ul([
                                    html.Li("Developed a process-based model to classify late orders by cause, "
                                            "deployed it to Azure Kubernetes Service, and automated reason tagging"
                                            " of daily late orders."),
                                    html.Li("Upgraded a legacy Java data pipeline for appointment scheduling "
                                            "model to Python using VSCode, GitHub Copilot, and SQL."),
                                    html.Li("Created APIs using Flask."),
                                ], style={"color": CONFIG['text-dark'], "text-align": "justify"}),
                            ],
                        ),
                    ],
                ),
                # Data Science Intern at Schneider
                html.Div(
                    style={
                        "position": "relative",
                        "margin-bottom": "40px",
                        "display": "flex",
                        "align-items": "center",
                    },
                    children=[
                        # Circle with logo
                        html.Div(
                            style={
                                "position": "absolute",
                                "left": "50%",
                                "transform": "translateX(-50%)",
                                "width": "70px",
                                "height": "70px",
                                "border-radius": "50%",
                                "background": "#ff6d39",
                                "display": "flex",
                                "align-items": "center",
                                "justify-content": "center",
                                "z-index": 1,
                                "border": f"2px solid {CONFIG['text-dark']}",
                            },
                            children=[
                                html.Img(
                                    src="/assets/schneider-logo.png",
                                    style={
                                        "width": "80%",
                                        "height": "auto",
                                    },
                                ),
                            ],
                        ),
                        # Job description box
                        html.Div(
                            style={
                                "width": "45%",
                                "margin-right": "55%",
                                "padding": "20px",
                                "background": "white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer
                                html.Div(
                                    style={
                                        "position": "absolute",
                                        "right": "-10px",
                                        "top": "50%",
                                        "transform": "translateY(-50%)",
                                        "width": "0",
                                        "height": "0",
                                        "border-top": "10px solid transparent",
                                        "border-bottom": "10px solid transparent",
                                        "border-left": "10px solid white",
                                    }
                                ),
                                # Job title and date
                                dbc.Row([
                                    html.H3(
                                        "Data Science Intern",
                                        className="text-md-end text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "3px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.H6(
                                        "May 2023 – Aug 2023",
                                        className="text-md-end text-center date-text",
                                        style={"color": CONFIG['text-dark']}
                                    ),
                                ], style={"padding-top": "5px"}),
                                # Job description
                                html.Ul([
                                    html.Li("Implemented image filtering pipeline to count semi-truck trailers "
                                            "in satellite images. Achieved 72% accuracy on test set."),
                                    html.Li("Developed an XGBoost model to predict the probability of direct "
                                            "bookings on the Schneider freight app, bypassing brokers."),
                                    html.Li("Created PowerBI and Tableau dashboards for 170+ associates, enhancing "
                                            "driver training, customer resolutions, and staffing."),
                                    html.Li("Automated data processes with Python and SQL."),
                                ], style={"color": CONFIG['text-dark'], "text-align": "justify"}),
                            ],
                        ),
                    ],
                ),
                # Teaching Assistant
                html.Div(
                    style={
                        "position": "relative",
                        "margin-bottom": "40px",
                        "display": "flex",
                        "align-items": "center",
                    },
                    children=[
                        # Circle with logo
                        html.Div(
                            style={
                                "position": "absolute",
                                "left": "50%",
                                "transform": "translateX(-50%)",
                                "width": "70px",
                                "height": "70px",
                                "border-radius": "50%",
                                "background": "#C5050C",
                                "display": "flex",
                                "align-items": "center",
                                "justify-content": "center",
                                "z-index": 1,
                                "border": f"2px solid {CONFIG['text-dark']}",
                            },
                            children=[
                                html.Img(
                                    src="/assets/ece.png",
                                    style={
                                        "width": "80%",
                                        "height": "auto",
                                    },
                                ),
                            ],
                        ),
                        # Job description box
                        html.Div(
                            style={
                                "width": "45%",
                                "margin-left": "55%",
                                "padding": "20px",
                                "background": "white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer
                                html.Div(
                                    style={
                                        "position": "absolute",
                                        "left": "-10px",
                                        "top": "50%",
                                        "transform": "translateY(-50%)",
                                        "width": "0",
                                        "height": "0",
                                        "border-top": "10px solid transparent",
                                        "border-bottom": "10px solid transparent",
                                        "border-right": "10px solid white",
                                    }
                                ),
                                # Job title and date
                                dbc.Row([
                                    html.H3(
                                        "Teaching Assistant",
                                        className="text-md-start text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "3px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.H6(
                                        "Aug 2021 – Dec 2021",
                                        className="text-md-start text-center date-text",
                                        style={"color": CONFIG['text-dark']}
                                    ),
                                ], style={"padding-top": "5px"}),
                                # Job description
                                html.P([
                                   "Provided hands-on support to over 80 students, ensuring "
                                    "comprehension of circuit analysis concepts, and honing skills "
                                    "in communication, critical thinking, and instructional guidance."
                                ], style={"color": CONFIG['text-dark'], "text-align": "justify"}),
                            ],
                        ),
                    ],
                ),
                # Mechanical Engineering Intern
                html.Div(
                    style={
                        "position": "relative",
                        "margin-bottom": "40px",
                        "display": "flex",
                        "align-items": "center",
                    },
                    children=[
                        # Circle with logo
                        html.Div(
                            style={
                                "position": "absolute",
                                "left": "50%",
                                "transform": "translateX(-50%)",
                                "width": "70px",
                                "height": "70px",
                                "border-radius": "50%",
                                "background": "#1a409f",
                                "display": "flex",
                                "align-items": "center",
                                "justify-content": "center",
                                "z-index": 1,
                                "border": f"2px solid {CONFIG['text-dark']}",
                            },
                            children=[
                                html.Img(
                                    src="/assets/marathon-petroleum.png",
                                    style={
                                        "width": "80%",
                                        "height": "auto",
                                    },
                                ),
                            ],
                        ),
                        # Job description box
                        html.Div(
                            style={
                                "width": "45%",
                                "margin-right": "55%",
                                "padding": "20px",
                                "background": "white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer
                                html.Div(
                                    style={
                                        "position": "absolute",
                                        "right": "-10px",
                                        "top": "50%",
                                        "transform": "translateY(-50%)",
                                        "width": "0",
                                        "height": "0",
                                        "border-top": "10px solid transparent",
                                        "border-bottom": "10px solid transparent",
                                        "border-left": "10px solid white",
                                    }
                                ),
                                # Job title and date
                                dbc.Row([
                                    html.H3(
                                        "Mechanical Engineering Intern",
                                        className="text-md-end text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "3px"}
                                    ),
                                ]),
                                # ], style={"padding-top": "10px"}),
                                dbc.Row([
                                    html.H6(
                                        "Aug 2020 – Dec 2020",
                                        className="text-md-end text-center date-text",
                                        style={"color": CONFIG['text-dark']}
                                    ),
                                ], style={"padding-top": "5px"}),
                                # Job description
                                html.P([
                                    "Facilitated successful integration of drainage canals in a refinery unit, "
                                    "fostering smooth cross-departmental collaboration among a 10-member team "
                                    "encompassing construction, finance, and engineering departments."
                                    # justify the text
                                ], style={"color": CONFIG['text-dark'], "text-align": "justify"}),
                            ],
                        ),
                    ],
                ),
            ]
        ),
    ]
)

# Experience section
experience = dbc.Row(
    [
        html.H2(
            "Relevant Experience",
            style={
                "margin-bottom": "30px",
                "font-size": "36px",
                "font-weight": "bold",
                "max-width": CONFIG['max-width'],
                "margin": "0 auto",
                "padding-bottom": "20px",
                "color": CONFIG['text-dark'],
            },
            className="text-center",
        ),
        html.Hr(style={"border-top": f"2px solid {CONFIG['text-dark']}", "width": "100%", "max-width": CONFIG['max-width']}),
        timeline,
    ],
    justify="center",
    className="d-flex flex-wrap",
    style={
        "padding-left": CONFIG["padding-left"],
        "padding-right": CONFIG["padding-left"],
        "padding-top": "40px",
        "background": "white",
        "margin": "0 auto",
    },
    id="experience",
)