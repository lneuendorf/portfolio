from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

data_eng_schneider = dbc.Col([
    html.Div(
        dbc.Row([
            # Left Column for Logo (Moves to top on small screens)
            dbc.Col(
                html.Div(
                    html.A(
                        html.Img(
                            src="/assets/schneider-logo.png",
                            style={
                                "padding": "10px",
                                "width": "100%",
                                "height": "auto",
                                "max-height": "150px",
                                "max-width": "200px",
                                "display": "block",
                                "margin": "0 auto",
                            },
                        ),
                        style={
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "width": "100%",
                            "height": "100%",  # Ensures full height on wide screens
                        },
                    ),
                    style={
                        "background": "#ff6d39",
                        "width": "100%",
                        "height": "100%",  # Ensures full height on wide screens
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "padding": "0",
                        "margin": "0",
                        "min-height": "100px",  # Ensures proper height when on top
                    },
                    className="orange-background"
                ),
                xs=12, sm=12, md=2,  # Moves to top on small screens
                className="d-flex align-items-center justify-content-center p-0"
            ),

            # Right Column for Text Content
            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        html.H3(
                            "Data Engineer", 
                            className="text-md-start text-center",
                            style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                        ), sm=12, md=6
                    ),
                    dbc.Col(
                        html.H5(
                            "Jan 2024 – Present", 
                            className="text-md-end text-center date-text",
                            style={"color": CONFIG['text-dark']}
                        ), sm=12, md=6
                    ),
                ], style={"padding-top": "15px"}),
                html.Ul([
                    html.Li("Developed a process-based model to classify late orders by cause, "
                            "deployed it to Azure Kubernetes Service, and automated reason tagging"
                            " of daily late orders."),
                    html.Li("Upgraded a legacy Java data pipeline for appointment scheduling "
                            "model to Python using VSCode, GitHub Copilot, and SQL."),
                    html.Li("Created APIs using Flask."),
                ], style={"color": CONFIG['text-dark']}),
            ], sm=12, md=10),
        ], 
        className="w-100 align-items-stretch flex-wrap"),  # Ensure proper wrapping
        style={
            "border-radius": "15px",
            "overflow": "hidden",
            "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.2)",
            "width": "100%",
            # "border": "2px solid white",
            "display": "flex",
            "flex-direction": "column",
            "height": "100%",
        },
    ),
], className='mb-3')

data_science_intern = dbc.Col([
    html.Div(
        dbc.Row([
            # Left Column for Logo (Moves to top on small screens)
            dbc.Col(
                html.Div(
                    html.A(
                        html.Img(
                            src="/assets/schneider-logo.png",
                            style={
                                "padding": "10px",
                                "width": "100%",
                                "height": "auto",
                                "max-height": "150px",
                                "max-width": "200px",
                                "display": "block",
                                "margin": "0 auto",
                            },
                        ),
                        style={
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "width": "100%",
                            "height": "100%",  # Ensures full height on wide screens
                        },
                    ),
                    style={
                        "background": "#ff6d39",
                        "width": "100%",
                        "height": "100%",  # Ensures full height on wide screens
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "padding": "10px",
                        "min-height": "100px",  # Ensures proper height when on top
                    },
                    className="orange-background"
                ),
                xs=12, sm=12, md=2,  # Moves to top on small screens
                className="d-flex align-items-center justify-content-center"
            ),

            # Right Column for Text Content
            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        html.H3(
                            "Data Science Intern",
                            className="text-md-start text-center",
                            style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                        ), sm=12, md=6
                    ),
                    dbc.Col(
                        html.H5(
                            "May 2023 – Aug 2023",
                            className="text-md-end text-center date-text",
                            style={"color": CONFIG['text-dark']}
                        ), sm=12, md=6
                    ),
                ], style={"padding-top": "15px"}),
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
        className="w-100 align-items-stretch flex-wrap"),  # Ensure proper wrapping
        style={
            "border-radius": "15px",
            "overflow": "hidden",
            "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.2)",
            "width": "100%",
            # "border": "2px solid white",
            "display": "flex",
            "flex-direction": "column",
            "height": "100%",
        },
    ),
], className='mb-3')

teaching_assistant = dbc.Col([
    html.Div(
        dbc.Row([
            # Left Column for Logo (Moves to top on small screens)
            dbc.Col(
                html.Div(
                    html.A(
                        html.Img(
                            src="/assets/ece.jpg",
                            style={
                                "padding": "10px",
                                "width": "100%",
                                "height": "auto",
                                "max-height": "150px",
                                "max-width": "200px",
                                "display": "block",
                                "margin": "0 auto",
                            },
                        ),
                        style={
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "width": "100%",
                            "height": "100%",  # Ensures full height on wide screens
                        },
                    ),
                    style={
                        "background": "#C5050C",
                        "width": "100%",
                        "height": "100%",  # Ensures full height on wide screens
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "padding": "10px",
                        "min-height": "100px",  # Ensures proper height when on top
                    },
                    className="orange-background"
                ),
                xs=12, sm=12, md=2,  # Moves to top on small screens
                className="d-flex align-items-center justify-content-center"
            ),

            # Right Column for Text Content
            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        html.H3(
                            "Teaching Assistant",
                            className="text-md-start text-center",
                            style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                        ), sm=12, md=6
                    ),
                    dbc.Col(
                        html.H5(
                            "Aug 2021 – Dec 2021",
                            className="text-md-end text-center date-text",
                            style={"color": CONFIG['text-dark']}
                        ), sm=12, md=6
                    ),
                ], style={"padding-top": "15px"}),
                html.Ul([
                    html.Li("Provided hands-on support to over 80 students, ensuring "
                        "comprehension of circuit analysis concepts, and honing skills "
                        "in communication, critical thinking, and instructional guidance."),
                ], style={"color": CONFIG['text-dark']}),
            ], sm=12, md=10),
        ], 
        className="w-100 align-items-stretch flex-wrap"),  # Ensure proper wrapping
        style={
            "border-radius": "15px",
            "overflow": "hidden",
            "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.2)",
            "width": "100%",
            # "border": "2px solid white",
            "display": "flex",
            "flex-direction": "column",
            "height": "100%",
        },
    ),
], className='mb-3')

mechanical_engineering_intern = dbc.Col([
    html.Div(
        dbc.Row([
            # Left Column for Logo (Moves to top on small screens)
            dbc.Col(
                html.Div(
                    html.A(
                        html.Img(
                            src="/assets/marathon-petroleum.png",
                            style={
                                "padding": "10px",
                                "width": "100%",
                                "height": "auto",
                                "max-height": "150px",
                                "max-width": "200px",
                                "display": "block",
                                "margin": "0 auto",
                            },
                        ),
                        style={
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "width": "100%",
                            "height": "100%",  # Ensures full height on wide screens
                        },
                    ),
                    style={
                        "background": "#1a409f",
                        "width": "100%",
                        "height": "100%",  # Ensures full height on wide screens
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "center",
                        "padding": "10px",
                        "min-height": "100px",  # Ensures proper height when on top
                    },
                    className="orange-background"
                ),
                xs=12, sm=12, md=2,  # Moves to top on small screens
                className="d-flex align-items-center justify-content-center"
            ),

            # Right Column for Text Content
            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        html.H3(
                            "Mechanical Engineering Intern",
                            className="text-md-start text-center",
                            style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                        ), sm=12, md=6
                    ),
                    dbc.Col(
                        html.H5(
                            "Aug 2020 – Dec 2020",
                            className="text-md-end text-center date-text",
                            style={"color": CONFIG['text-dark']}
                        ), sm=12, md=6
                    ),
                ], style={"padding-top": "15px"}),
                html.Ul([
                    html.Li("Facilitated successful integration of drainage canals in a refinery unit, "
                            "fostering smooth cross-departmental collaboration among a 10-member team "
                            "encompassing construction, finance, and engineering departments.")
                ], style={"color": CONFIG['text-dark']}),
            ], sm=12, md=10),
        ], 
        className="w-100 align-items-stretch flex-wrap"),  # Ensure proper wrapping
        style={
            "border-radius": "15px",
            "overflow": "hidden",
            "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.2)",
            "width": "100%",
            # "border": "2px solid white",
            "display": "flex",
            "flex-direction": "column",
            "height": "100%",
        },
    ),
], className='mb-3')

experience = dbc.Row([    
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
    html.Hr(style={"border-top": f"2px solid {CONFIG['text-dark']}", "width": "100%", "max-width": CONFIG['max-width']}),

    dbc.Row([
        dbc.Col([
            data_eng_schneider,
            data_science_intern,
            teaching_assistant,
            mechanical_engineering_intern,
        ], xs=12, className="px-2"),
    ], style={
        "max-width": CONFIG['max-width'],
        "padding": "0px 0px 30px 0px",
    })
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
id="projects"
)