from dash import html
import dash_bootstrap_components as dbc
from config.config import CONFIG

# Define the layout
education_wide = html.Div(
    style={
        "position": "relative",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
        "padding": "0px 0px",
    },
    children=[
        html.Div(
            id="education-line-wide",
            style={
                "position": "absolute",
                "left": "calc(50% - 1px)", 
                "width": "2px",
                "height": "calc(100% - 15px)",  # Adjusted height to fit between boxes
                "background": CONFIG['text-dark'],
                "top": "10px",  # Start below the top circle
            }
        ),
        # Education items
        html.Div(
            [
                # M.S. Computer Engineering
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
                                                    "M.S. Computer Engineering",
                                                    className="text-start",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Sept 2022 - Dec 2023",
                                                    className="text-start date-text-large mb-0",
                                                    style={"color": CONFIG['text-dark']}
                                                ),
                                            ],
                                            width=10,
                                        ),
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-masters-lg",
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
                                            html.B("GPA: ", style={"color": CONFIG['text-dark']}),
                                            html.Span(
                                                "3.75/4.0", 
                                                style={"color": CONFIG['text-dark']}),
                                            html.Br(),
                                            html.B("Focus: ", style={"color": CONFIG['text-dark']}),
                                            html.Span(
                                                "Machine Learning & Signal Processing", 
                                                style={"color": CONFIG['text-dark']}),
                                            html.Br(),
                                            html.B("Coursework: ", style={"color": CONFIG['text-dark']}), 
                                            html.Span(
                                                "Machine Learning, Probability & Information Theory in ML, "
                                                "Theoretical Foundations of Data Science, Big Data Systems, "
                                                "Advanced NLP, Optimization, "
                                                "Digital Image Processing",
                                                style={
                                                    "color": CONFIG['text-dark'],
                                                }
                                            ),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-masters-lg",
                                    is_open=False,
                                ),
                            ],
                        ),
                    ],
                ),
                # B.S. Computer Engineering
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
                                                id="collapse-button-bachelors-lg",
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
                                                    "B.S. Computer Engineering",
                                                    className="text-end",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Sept 2017 - Aug 2022",
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
                                            html.B("GPA: ", style={"color": CONFIG['text-dark']}),
                                            html.Span(
                                                "3.44/4.0",
                                                style={"color": CONFIG['text-dark']}),
                                            html.Br(),
                                            html.B("Activities: ", style={"color": CONFIG['text-dark']}),
                                            html.Span(
                                                "Data Science Club, Wisconsin Autonomous, Wisconsin Space Race, Running Club",
                                                style={"color": CONFIG['text-dark']}
                                            ),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-bachelors-lg",
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

education_narrow = html.Div(
    style={
        "position": "relative",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
        "padding": "0px 0px",
    },
    children=[
        # Vertical line (positioned on the right)
        html.Div(
            id="education-line-small",
            style={
                "position": "absolute",
                "right": "37px",  # 50px from the boxes
                "width": "2px",
                "height": "calc(100% - 15px)",  # Adjusted height to fit between boxes
                "background": CONFIG['text-dark'],
                "top": "10px",  # Start below the top circle
            }
        ),
        # Education items
        html.Div(
            [
                # M.S. Computer Engineering
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
                                "right": "3px",  # Adjusted to align with the vertical line
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
                        # Job description box (aligned to the left)
                        html.Div(
                            style={
                                "width": "100%",  # Adjusted width
                                "margin-right": "90px",  # Adjusted to align with the vertical line
                                "margin-left": "4px",  
                                "padding": "15px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer (pointing right)
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-masters",
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
                                                    "M.S. Computer Engineering",
                                                    className="text-end",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Sept 2022 - Dec 2023",
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
                                            html.B("GPA: ", style={"color": CONFIG['text-dark']}),
                                            html.Span(
                                                "3.75/4.0", 
                                                style={"color": CONFIG['text-dark']}),
                                            html.Br(),
                                            html.B("Focus: ", style={"color": CONFIG['text-dark']}),
                                            html.Span(
                                                "Machine Learning & Signal Processing", 
                                                style={"color": CONFIG['text-dark']}),
                                            html.Br(),
                                            html.B("Coursework: ", style={"color": CONFIG['text-dark']}), 
                                            html.Span(
                                                "Machine Learning, Probability & Information Theory in ML, "
                                                "Theoretical Foundations of Data Science, Big Data Systems, "
                                                "Advanced NLP, Optimization, "
                                                "Digital Image Processing",
                                                style={
                                                    "color": CONFIG['text-dark'],
                                                }
                                            ),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-masters",
                                    is_open=False,
                                ),
                            ],
                        ),
                    ],
                ),
                # B.S. Computer Engineering
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
                                "right": "3px",  # Adjusted to align with the vertical line
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
                        # Job description box (aligned to the left)
                        html.Div(
                            style={
                                "width": "100%",  # Adjusted width
                                "margin-right": "90px",  # Adjusted to align with the vertical line
                                "margin-left": "4px",  
                                "padding": "15px",
                                "background": "#f1f1ee",
                                "border": "2px solid white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer (pointing right)
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
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id="collapse-button-bachelors",
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
                                                    "B.S. Computer Engineering",
                                                    className="text-end",
                                                    style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                                ),
                                                html.H5(
                                                    "Sept 2017 - Aug 2022",
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
                                            html.B("GPA: ", style={"color": CONFIG['text-dark']}),
                                            html.Span(
                                                "3.44/4.0",
                                                style={"color": CONFIG['text-dark']}),
                                            html.Br(),
                                            html.B("Activities: ", style={"color": CONFIG['text-dark']}), 
                                            html.Span(
                                                "Data Science Club, Wisconsin Autonomous, Wisconsin Space Race, Running Club",
                                                style={"color": CONFIG['text-dark']}
                                            ),
                                        ], className="text-start text-dark mt-1 mb-0"),
                                    ]),
                                    id="collapse-bachelors",
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
education = dbc.Row(
    [
        html.H2(
            "Education",
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
        html.Div(
            education_wide,
            className="timeline-wide"
        ),
        # Narrow education (shown on smaller screens)
        html.Div(
            education_narrow,
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
    id="education",
)