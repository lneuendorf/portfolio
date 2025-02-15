from dash import html
import dash_bootstrap_components as dbc
from config.config import CONFIG

timeline_wide = html.Div(
    style={
        "position": "relative",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
        "padding": "0px 0px",
    },
    children=[
        html.Div(
            id="timeline-line",
            style={
                "position": "absolute",
                "left": "calc(50% - 1px)", 
                "width": "2px",
                "height": "calc(100% - 15px)",  # Adjusted height to fit between boxes
                "background": CONFIG['text-dark'],
                "top": "10px",  # Start below the top circle
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
                                "margin-left": "calc(50% + 50px)",
                                "padding": "20px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Data Engineer",
                                                    className="text-start",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Jan 2024 – Present",
                                                    className="text-start date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-data-eng-lg",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.Ul([
                                            html.Li("Built a process-based model to classify late orders, intersecting "
                                                    "weather polygons with location data. Deployed process on Anaconda Enterprise."),
                                            html.Li("Refactored a 118-file Java data pipeline for appointment scheduling "
                                                    "into a streamlined 33-file Python solution using VSCode, GitHub "
                                                    "Copilot, Unit Testing, and SQL."),
                                            html.Li("Completed several smaller projects, working with Snowflake, "
                                                    "cloud deployments, APIs, Azure ML, and more."),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ], style={"padding-left": "20px"}),
                                    id="collapse-data-eng-lg",
                                    is_open=False,
                                ),
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
                                "margin-right": "calc(50% + 50px)",
                                "padding": "20px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-data-science-lg",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Data Science Intern",
                                                    className="text-end",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "May 2023 – Aug 2023",
                                                    className="text-end date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.Ul([
                                            html.Li("Implemented image filtering pipeline to count semi-truck trailers "
                                                    "in satellite images. Achieved 72% accuracy on test set."),
                                            html.Li("Developed an XGBoost model to predict the probability of direct "
                                                    "bookings on the Schneider freight app."),
                                            html.Li("Created PowerBI and Tableau dashboards for 170+ associates, assisting with "
                                                    "driver training, customer resolutions, and staffing estimates."),
                                            html.Li("Automated ETL process with Python and SQL."),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ], style={"padding-left": "20px"}),
                                    id="collapse-data-science-lg",
                                    is_open=False,
                                ),
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
                                "margin-left": "calc(50% + 50px)",
                                "padding": "20px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Teaching Assistant",
                                                    className="text-start",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Aug 2021 – Dec 2021",
                                                    className="text-start date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-teaching-lg",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.P([
                                            "Provided hands-on support to over 80 students, ensuring "
                                                "comprehension of circuit analysis concepts, and honing skills "
                                                "in communication, critical thinking, and instructional guidance."
                                        ], 
                                        style={"color": CONFIG['text-dark']},
                                        className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-teaching-lg",
                                    is_open=False,
                                ),
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
                                "width": "100%",
                                "margin-right": "calc(50% + 50px)",
                                "padding": "20px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-marathon-lg",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Mechanical Engineering Intern",
                                                    className="text-end",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Aug 2020 – Dec 2020",
                                                    className="text-end date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.P([
                                            "Facilitated successful integration of drainage canals in a refinery unit, "
                                            "fostering smooth cross-departmental collaboration among a 10-member team "
                                            "encompassing construction, finance, and engineering departments."
                                        ], 
                                        style={"color": CONFIG['text-dark']},
                                        className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-marathon-lg",
                                    is_open=False,
                                ),
                            ],
                        ),
                    ],
                ),
            ]
        ),
    ]
)

timeline_narrow = html.Div(
    style={
        "position": "relative",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
        "padding": "0px 0px",
    },
    children=[
        # Vertical line (positioned between the first and last boxes)
        html.Div(
            id="timeline-line",
            style={
                "position": "absolute",
                "left": "38px",  # 50px from the boxes
                "width": "2px",
                "height": "calc(100% - 15px)",  # Adjusted height to fit between boxes
                "background": CONFIG['text-dark'],
                "top": "10px",  # Start below the top circle
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
                                "left": "4px",  # Adjusted to align with the vertical line
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
                        # Job description box (aligned to the right)
                        html.Div(
                            style={
                                "width": "100%",  # Adjusted width
                                "margin-left": "90px",  # Adjusted to align with the vertical line
                                "margin-right": "5px",  
                                "padding": "15px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer (pointing left)
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Data Engineer",
                                                    className="text-start",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Jan 2024 – Present",
                                                    className="text-start date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-data-eng",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.Ul([
                                            html.Li("Built a process-based model to classify late orders, intersecting "
                                                    "weather polygons with location data. Deployed process on Anaconda Enterprise."),
                                            html.Li("Refactored a 118-file Java data pipeline for appointment scheduling "
                                                    "into a streamlined 33-file Python solution using VSCode, GitHub "
                                                    "Copilot, Unit Testing, and SQL."),
                                            html.Li("Completed several smaller projects, working with Snowflake, "
                                                    "cloud deployments, APIs, Azure ML, and more."),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ], style={"padding-left": "20px"}),
                                    id="collapse-data-eng",
                                    is_open=False,
                                ),
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
                                "left": "4px",  # Adjusted to align with the vertical line
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
                        # Job description box (aligned to the right)
                        html.Div(
                            style={
                                "width": "100%",  # Adjusted width
                                "margin-left": "90px",  # Adjusted to align with the vertical line
                                "margin-right": "5px",  
                                "padding": "15px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer (pointing left)
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Data Science Intern",
                                                    className="text-start",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "May 2023 – Aug 2023",
                                                    className="text-start date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-data-science",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.Ul([
                                            html.Li("Implemented image filtering pipeline to count semi-truck trailers "
                                                    "in satellite images. Achieved 72% accuracy on test set."),
                                            html.Li("Developed an XGBoost model to predict the probability of direct "
                                                    "bookings on the Schneider freight app."),
                                            html.Li("Created PowerBI and Tableau dashboards for 170+ associates, assisting with "
                                                    "driver training, customer resolutions, and staffing estimates."),
                                            html.Li("Automated ETL process with Python and SQL."),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ], style={"padding-left": "20px"}),
                                    id="collapse-data-science",
                                    is_open=False,
                                ),
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
                                "left": "4px",  # Adjusted to align with the vertical line
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
                        # Job description box (aligned to the right)
                        html.Div(
                            style={
                                "width": "100%",  # Adjusted width
                                "margin-left": "90px",  # Adjusted to align with the vertical line
                                "margin-right": "5px",  
                                "padding": "15px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer (pointing left)
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Teaching Assistant",
                                                    className="text-start",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Aug 2021 – Dec 2021",
                                                    className="text-start date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-teaching",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.P([
                                            "Provided hands-on support to over 80 students, ensuring "
                                                "comprehension of circuit analysis concepts, and honing skills "
                                                "in communication, critical thinking, and instructional guidance."
                                        ], 
                                        style={"color": CONFIG['text-dark']},
                                        className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-teaching",
                                    is_open=False,
                                ),
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
                                "left": "4px",  # Adjusted to align with the vertical line
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
                        # Job description box (aligned to the right)
                        html.Div(
                            style={
                                "width": "100%",  # Adjusted width
                                "margin-left": "90px",  # Adjusted to align with the vertical line
                                "margin-right": "5px",  
                                "padding": "15px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer (pointing left)
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            [
                                                html.H3(
                                                    "Mechanical Engineering Intern",
                                                    className="text-start",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Aug 2020 – Dec 2020",
                                                    className="text-start date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-marathon",
                                                outline=True,
                                                n_clicks=0,
                                                size="sm",
                                                style={
                                                    "width": "30px",
                                                    "height": "30px",
                                                    "border-radius": "20%",
                                                    "align-items": "center",
                                                    "justify-content": "center",
                                                    "margin": "auto",
                                                    "display": "flex",
                                                    "background": "transparent",
                                                    "font-weight": "bold",
                                                    "border": f"2px solid {CONFIG['text-dark']}",
                                                    "color": CONFIG['text-dark'],
                                                },
                                            ),
                                            width=2,
                                            style={
                                                "align-items": "center",  # Center vertically
                                            },
                                        ),
                                    ],
                                    align="center",  # Align items vertically in the row
                                ),
                                # Collapsible component
                                dbc.Collapse(
                                    dbc.Row([
                                        html.P([
                                            "Facilitated successful integration of drainage canals in a refinery unit, "
                                            "fostering smooth cross-departmental collaboration among a 10-member team "
                                            "encompassing construction, finance, and engineering departments."
                                        ], 
                                        style={"color": CONFIG['text-dark']},
                                        className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-marathon",
                                    is_open=False,
                                ),
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
                "font-size": "36px",
                "font-weight": "bold",
                "max-width": CONFIG['max-width'],
                "margin": "0 auto",
                "padding-bottom": "25px",
                "color": CONFIG['text-dark'],
            },
            className="text-center",
        ),
        html.Hr(
            style={
                "border-top": f"2px solid {CONFIG['text-dark']}", 
                "width": f"calc(100% - 30px)",  # Adjust width to account for 30px padding on both sides
                "max-width": CONFIG['max-width'], 
                "margin-left": "15px",  # Add 30px padding on the left
                "margin-right": "15px",  # Add 30px padding on the right
            }
        ),
        # Wide timeline (shown on larger screens)
        html.Div(
            timeline_wide,
            className="timeline-wide"
        ),
        # Narrow timeline (shown on smaller screens)
        html.Div(
            timeline_narrow,
            className="timeline-narrow"
        ),
    ],
    justify="center",
    className="d-flex flex-wrap",
    style={
        "padding-left": CONFIG["padding-left"],
        "padding-right": CONFIG["padding-left"],
        "padding-top": "40px",
        "padding-bottom": "0px",
        "background": "white",
        "margin": "0 auto",
    },
    id="experience",
)