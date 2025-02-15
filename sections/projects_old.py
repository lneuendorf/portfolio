from dash import html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from config.config import CONFIG

nfl_bdb_2025 = (
    dbc.Col([
        html.Div(
            children=[
                html.Img(
                    src="/assets/motion.gif",
                    style={
                        "width": "100%",
                        "height": "auto",
                    },
                ),
                html.Div(
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.P(),
                                    width=2,
                                ),
                                dbc.Col(
                                    html.H3("Motion for More", style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}),
                                    width=8,
                                ),
                                dbc.Col(
                                    dbc.Button(
                                        "+",
                                        id="collapse-button-nfl-25",
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
                        # Brief synopsis (visible when collapse is closed)
                        html.Div(
                            id="brief-synopsis-nfl-25",
                            children=[
                                html.P(
                                    "2025 NFL Big Data Bowl Submission (Honorable Mention)",
                                    style={
                                        "color": CONFIG['text-dark'],
                                        "text-align": "center",
                                        "margin": "10px 0 0 0",
                                        "font-style": "italic",
                                    },
                                ),
                            ],
                        ),
                        # Collapsible component (visible when collapse is open)
                        dbc.Collapse(
                            dbc.Row([
                                html.P([
                                    "Used Bayesian regression to analyze the impact of pre-snap motion on ",
                                    "rushing success in the NFL, identifying the motion types and run concepts ",
                                    "that maximize yards per carry (YPC). Notably, pre-snap Jet motion ",
                                    "increased YPC by an average of 0.55 ",
                                    "compared to the same play without ",
                                    "it, provided the ball carrier was not the motion player. This project ",
                                    "earned an ",
                                    html.B("honorable mention"),
                                    " in the ",
                                    html.A(
                                        "2025 NFL Big Data Bowl",
                                        href="https://operations.nfl.com/gameday/analytics/big-data-bowl/2025-big-data-bowl-finalists/",
                                        target="_blank",
                                        style={"color": CONFIG['text-dark'], "text-decoration": "underline"}
                                    ),
                                    "."
                                ],
                                style={
                                    "color": CONFIG['text-dark'],
                                    "text-align": "justify",
                                    "margin": "10px 0 0 0",
                                }),
                            ]),
                            id="collapse-nfl-25",
                            is_open=False,
                        ),
                        html.Div(
                            children=[
                                dbc.Button(
                                    html.Img(
                                        src="/assets/kaggle.png",
                                        style={"height": "20px", "width": "auto"},
                                    ), 
                                    href="https://www.kaggle.com/code/lukeneuendorf/motion-for-more", 
                                    target="_blank", 
                                    color="dark", 
                                    className="m-1 px-1 py-1"
                                ),
                                dbc.Button(
                                    html.Img(
                                        src="/assets/github-logo-full.png",
                                        style={"height": "20px", "width": "auto"},
                                    ),
                                    href="https://github.com/lneuendorf/nfl-big-data-bowl-2025",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                                dbc.Button(
                                    "Dashboard", 
                                    href="https://motion-for-more-19060a459b59.herokuapp.com/distributions", 
                                    target="_blank", 
                                    color="dark", 
                                    className="m-1 px-1 py-1"
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
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
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                "border": "2px solid white",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ], className='mb-3')
)

nfl_bdb_2024 = (
    dbc.Col([
        html.Div(
            children=[
                html.Img(
                    src="/assets/2024-bdb-play.gif",
                    style={
                        "width": "100%",
                        "height": "auto",
                        # "border-bottom": "2px solid white",
                    },
                ),
                html.Div(
                    children=[
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.P(),
                                    width=2,
                                ),
                                dbc.Col(
                                    html.H3("TDOE (Tackle Depth Over Expectation)", style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}),
                                    width=8,
                                ),
                                dbc.Col(
                                    dbc.Button(
                                        "+",
                                        id="collapse-button-nfl-24",
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
                        # Brief synopsis (visible when collapse is closed)
                        html.Div(
                            id="brief-synopsis-nfl-24",
                            children=[
                                html.P(
                                    "2024 NFL Big Data Bowl Submission",
                                    style={
                                        "color": CONFIG['text-dark'],
                                        "text-align": "center",
                                        "margin": "10px 0 0 0",
                                        "font-style": "italic",
                                    },
                                ),
                            ],
                        ),
                        # Collapsible component (visible when collapse is open)
                        dbc.Collapse(
                            dbc.Row([
                                html.P([
                                    "Developed a deep learning model using LSTMs to predict the location "
                                    " of a tackle, achieving an R-Squared of 0.74. Created the metric Tackle Depth Over "
                                    "Expectation (TDOE) to evaluate tackling effectiveness, "
                                    "enabling teams to assess defenders' ability to minimize yards gained, "
                                    "and providing a more contextualized measure of tackling performance beyond traditional "
                                    "counting stats."
                                ],
                                style={
                                    "color": CONFIG['text-dark'],
                                    "text-align": "justify",
                                    "margin": "10px 0 0 0",
                                }),
                            ]),
                            id="collapse-nfl-24",
                            is_open=False,
                        ),
                        html.Div(
                            children=[
                                dbc.Button(
                                    html.Img(
                                        src="/assets/kaggle.png",
                                        style={"height": "20px", "width": "auto", "align": "center"},
                                    ), 
                                    href="https://www.kaggle.com/code/lukeneuendorf/tdoe-tackle-depth-over-expectation", 
                                    target="_blank", 
                                    color="dark", 
                                    className="m-1 px-1 py-1"
                                ),
                                dbc.Button(
                                    html.Img(
                                        src="/assets/github-logo-full.png",
                                        style={"height": "20px", "width": "auto", "align": "center"},
                                    ),
                                    href="https://github.com/lneuendorf/NFL-Big-Data-Bowl-2024",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
                    ],
                    style={
                        "background": "#f1f1ee",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid white",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ], className='mb-3')
)

low_resource_machine_translation = (
    dbc.Col([
        html.Div(
            children=[
                html.Img(
                    src="/assets/low-resource-mt.png",
                    style={
                        "width": "100%",
                        "height": "auto",
                        # "border-bottom": "2px solid white",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("Low-Resource Machine Translation Research", style={"color": CONFIG['text-dark']}),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "Explored various NLP data pre-processing techniques to enhance translation quality in low-resource settings, specifically for Nepali-to-English translation. ",
                            "BART, a transformer-based model, significantly improved performance, achieving a ",
                            "2.11 BLEU",
                            " score compared to the baseline of ",
                            "1.07 BLEU",
                            ", demonstrating its effectiveness in this limited-data scenario. "
                            "Joint Dropout led to a modest improvement, reaching ",
                            "1.11 BLEU.",
                        ],
                        style={
                            "color": CONFIG['text-dark'],
                            "text-align": "justify",
                            "margin": "10px 0 0 0",
                        }),
                        html.Div(
                            children=[
                                dcc.Link(
                                    dbc.Button("Paper", color="dark", className="m-1 px-2 py-1"),
                                    href="/assets/low-resource-mt.pdf",
                                    target="_blank"
                                ),
                                dbc.Button(
                                    html.Img(
                                        src="/assets/github-logo-full.png",
                                        style={"height": "20px", "width": "auto", "align": "center"},
                                    ),
                                    href="https://github.com/gselzer/cs769-final-project",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
                    ],
                    style={
                        "background": "#f1f1ee",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid white",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ], className='mb-3')
)

saguage = (
    dbc.Col([
        html.Div(
            children=[
                html.Img(
                    src="/assets/sanguage.gif",
                    style={
                        "width": "100%",
                        "height": "auto",
                        # "border-bottom": "2px solid white",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("Sanguage", style={"color": CONFIG['text-dark']}),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "Developed ",
                            "Sanguage",
                            ", an Android mobile app that recognizes and translates ",
                            "American Sign Language (ASL) alphabet letters",
                            " into text in real time using the TensorFlow Lite model ",
                            "EfficientNet-Lite0",
                            ", achieving ",
                            "99.43% test set classification accuracy",
                            ". While this prototype focuses on Alphabetical letters, it demonstrates the potential ",
                            "for a larger-scale system that could enable real-time ASL translations."
                        ],
                        style={
                            "color": CONFIG['text-dark'],
                            "text-align": "justify",
                            "margin": "10px 0 0 0",
                        }),
                        html.Div(
                            children=[
                                dbc.Button(
                                    html.Img(
                                        src="/assets/github-logo-full.png",
                                        style={"height": "20px", "width": "auto", "align": "center"},
                                    ),
                                    href="https://github.com/lneuendorf/ECE454FinalProject",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
                    ],
                    style={
                        "background": "#f1f1ee",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid white",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ], className='mb-3')
)

ffcrystalball = (
    dbc.Col([
        html.Div(
            children=[
                html.Img(
                    src="/assets/ffcrystalball.gif",
                    style={
                        "width": "100%",
                        "height": "auto",
                        # "border-bottom": "2px solid white",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("Fantasy Football Crystal Ball", style={"color": CONFIG['text-dark']}),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                       html.P([
                            "Developed ",
                            "FFCrystal Ball",
                            ", a fantasy football analytics tool leveraging ",
                            "quantile regression",
                            " with ",
                            "gradient boosting",
                            " to predict a player's range of fantasy point outcomes. This approach ",
                            "improved mean absolute error by ",
                            "15%",
                            " compared to a baseline linear regression model, demonstrating the value of ",
                            "a more complex model."
                        ],
                        style={
                            "color": CONFIG['text-dark'],
                            "text-align": "justify",
                            "margin": "10px 0 0 0",
                        }),
                        html.Div(
                            children=[
                                dbc.Button(
                                    html.Img(
                                        src="/assets/github-logo-full.png",
                                        style={"height": "20px", "width": "auto", "align": "center"},
                                    ),
                                    href="https://github.com/lneuendorf/ffcrystalball",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
                    ],
                    style={
                        "background": "#f1f1ee",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid white",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ], className='mb-3')
)

octoberodds = (
    dbc.Col([
        html.Div(
            children=[
                html.Img(
                    src="/assets/octoberodds.png",
                    style={
                        "width": "100%",
                        "height": "auto",
                        # "border-bottom": "2px solid white",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("October Odds", style={"color": CONFIG['text-dark']}),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "This project is currently in progress and aims to provide a dynamic visualization of each ",
                            "MLB team's probability of making the playoffs",
                            " at any point in the season. The app will utilize a ",
                            "win probability model",
                            " to estimate the likelihood of winning each remaining game and employ ",
                            "Monte Carlo simulation",
                            " to generate probability distributions for playoff qualification. Additionally, it will display ",
                            "World Series winner odds",
                            " based on simulated season outcomes."
                        ],
                        style={
                            "color": CONFIG['text-dark'],
                            "text-align": "justify",
                            "margin": "10px 0 0 0",
                        }),
                        html.Div(
                            children=[
                                dbc.Button(
                                    html.Img(
                                        src="/assets/github-logo-full.png",
                                        style={"height": "20px", "width": "auto", "align": "center"},
                                    ),
                                    href="https://github.com/lneuendorf/mlb-playoff-models",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
                    ],
                    style={
                        "background": "#f1f1ee",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid white",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ])
)

projects = dbc.Row([    
    html.H2(
        "Projects",
        style={
            "font-size": "36px",  # Default font size for xs screens
            "font-weight": "bold",
            "max-width": CONFIG['max-width'],
            "margin": "0 auto",
            "padding-bottom": "25px",
            "color": CONFIG['text-dark'],
        },
        className="text-center d-none d-sm-block"  # Hide on xs screens
    ),
    html.H2(
        "Projects",
        style={
            "font-size": "32px",  # Font size for sm screens and larger
            "font-weight": "bold",
            "max-width": CONFIG['max-width'],
            "margin": "0 auto",
            "padding-bottom": "25px",
            "color": CONFIG['text-dark'],
        },
        className="text-center d-block d-sm-none"  # Show only on xs screens
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
    dbc.Row([
        dbc.Col([
                nfl_bdb_2025,
                low_resource_machine_translation,
                ffcrystalball
            ],
            sm=12, md=6, xl=6,
            className="px-2",
        ),
        dbc.Col([
                nfl_bdb_2024,
                saguage,
                octoberodds
            ],
            sm=12, md=6, xl=6,
            className="px-2",
        ),
    ], style={
        "max-width": CONFIG['max-width'],
        "padding": "0px 0px 30px 0px",
        "display": "flex",  # Ensures flexbox behavior for `order`
        "flex-wrap": "wrap",  # Allows wrapping of tiles on small screens
    })

], 
justify="center", 
className="d-flex flex-wrap", 
style={
    "padding-left": CONFIG["padding-left"],
    "padding-right": CONFIG["padding-left"],
    "padding-top": "40px",
    "padding-bottom": "20px",
    "background-color": "white",
    "margin": "0 auto",
},
id="projects"
)