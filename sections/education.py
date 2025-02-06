from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

masters = (
    dbc.Col([
        html.Div(
            children=[
                html.Div(
                    html.A(
                        html.Img(
                            src="/assets/uw-madison.png",
                            style={
                                "height": "100%",
                                "width": "auto",
                                "max-height": "150px",
                                "max-width": "100%",
                                "display": "block",
                                "margin": "0 auto",
                            },
                        ),
                        style={
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "height": "100%",
                        },
                    ),
                    style={
                        "width": "100%",
                        "height": "150px",
                        "background": "linear-gradient(to bottom, #C5050C, #c4676a)",
                        "border-bottom": "2px solid black",
                    },
                ),
                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3(
                                    "M.S. Computer Engineering", 
                                    style={"color": CONFIG['text-dark'], "margin-bottom": "10px"}
                                ),
                                html.H5(
                                    "Sept 2022 - Dec 2023",
                                    style={"color": CONFIG['text-dark'], "margin-bottom": "10px"}
                                ),
                                html.H6(
                                    "GPA: 3.75/4.0",
                                    style={"color": CONFIG['text-dark'], "margin-bottom": "10-px"}
                                ),
                            ],
                            style={
                                "text-align": "center",
                            },
                        ),
                        html.Div([
                            html.Ul([
                                html.Li([
                                    html.B("Focus: ", style={"color": CONFIG['text-dark']}),  # Bold with custom color
                                    html.Span(
                                        "Machine Learning & Data Science", 
                                        style={"color": CONFIG['text-dark']}),
                                ]),
                                html.Li([
                                    html.B("Coursework: ", style={"color": CONFIG['text-dark']}), 
                                    html.Span(
                                        "Machine Learning, Big Data Systems, Advanced NLP, Optimization,"
                                        "Digital Image Processing, Probability & Information Theory in ML, "
                                        "Theoretical Foundations of Data Science",
                                        style={
                                            "color": CONFIG['text-dark'],
                                            "text-align": "justify",
                                        }
                                    ),
                                ]),
                            ], className="text-start text-dark"),
                        ]),
                    ],
                    style={
                        "background": "#f1f1ee",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",  # Forces all content sections to be the same height
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.2)",  # Glow effect
                "width": "100%",
                "border": "2px solid black",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ], className='mb-3')
)

bachelors = (
    dbc.Col([
        html.Div(
            children=[
                html.Div(
                    html.A(
                        html.Img(
                            src="/assets/uw-madison.png",
                            style={
                                "height": "100%",
                                "width": "auto",
                                "max-height": "150px",
                                "max-width": "100%",
                                "display": "block",
                                "margin": "0 auto",
                            },
                        ),
                        style={
                            "display": "flex",
                            "justify-content": "center",
                            "align-items": "center",
                            "height": "100%",
                        },
                    ),
                    style={
                        "width": "100%",
                        "height": "150px",
                        "background": "linear-gradient(to bottom, #C5050C, #c4676a)",
                        "border-bottom": "2px solid black",
                    },
                ),
                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3(
                                    "B.S. Computer Engineering", 
                                    style={"color": CONFIG['text-dark'], "margin-bottom": "10px"}
                                ),
                                html.H5(
                                    "Sept 2017 - Aug 2022",
                                    style={"color": CONFIG['text-dark'], "margin-bottom": "10px"}
                                ),
                                html.H6(
                                    "GPA: 3.44/4.0",
                                    style={"color": CONFIG['text-dark'], "margin-bottom": "10-px"}
                                ),
                            ],
                            style={
                                "text-align": "center",
                            },
                        ),
                        html.Div([
                            html.Ul([
                                html.Li([
                                    html.B("Activities: ", style={"color": CONFIG['text-dark']}), 
                                    html.Span(
                                        "Data Science Club, Wisconsin Autonomous, Wisconsin Space Race, Running Club",
                                        style={"color": CONFIG['text-dark']}
                                    ),
                                ]),
                            ], className="text-start text-dark"),
                        ]),
                    ],
                    style={
                        "background": "#f1f1ee",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",  # Forces all content sections to be the same height
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.2)",
                "width": "100%",
                "border": "2px solid black",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ], className='mb-3')
)

education = dbc.Row([    
    html.H2(
        "Education",
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
        "Education",
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
            masters,
        ], sm=12, md=6, xl=6, className="px-2"),
        dbc.Col([
            bachelors,
        ], sm=12, md=6, xl=6, className="px-2") 
    ], style={
        "max-width": CONFIG['max-width'],
        # padding below
        "padding": "10px 10px 30px 10px"
    })
], 
justify="center", 
className="d-flex flex-wrap", 
style={
    "padding-left": CONFIG["padding-left"],
    "padding-right": CONFIG["padding-left"],
    "padding-top": "40px",
    "background": "white",
    # "margin": "0 auto",
},
id="projects"
)