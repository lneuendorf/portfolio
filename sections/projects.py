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
                        "border-bottom": "2px solid black",
                    },
                ),
                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("Motion for More", className="text-dark"),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "Analyzed the impact of pre-snap motion on rushing success in the NFL "
                            "using Bayesian regression, identifying which motion types and run "
                            "concepts maximize yards per carry. This project received an honorable "
                            "mention in the ",
                            html.A(
                                "2025 NFL Big Data Bowl",
                                href="https://operations.nfl.com/gameday/analytics/big-data-bowl/2025-big-data-bowl-finalists/",
                                target="_blank",
                                style={"color":"#2a2929","text-decoration": "underline"}
                            ),
                            "."
                        ],
                        className="text-dark",
                        style={
                            "text-align": "justify",
                            "margin": "10px 0 0 0",
                            "flex-grow": "1",  # Allows this section to expand to equal height
                        }),
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
                        "background": "white",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",  # Forces all content sections to be the same height
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid black",
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
                        "border-bottom": "2px solid black",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("TDOE (Tackle Depth Over Expectation)", className="text-dark"),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "Developed a deep learning model using LSTMs to predict the location "
                            " of a tackle, achieving an R-Squared of 0.74. Created the metric Tackle Depth Over "
                            "Expectation (TDOE) to evaluate tackling effectiveness, "
                            "enabling teams to assess defenders' ability to minimize yards gained, "
                            "and providing a more contextualized measure of tackling performance beyond traditional "
                            "counting stats."
                        ],
                        className="text-dark",
                        style={
                            "text-align": "justify",
                            "margin": "10px 0 0 0",
                        }),
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
                        "background": "white",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid black",
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
                        "border-bottom": "2px solid black",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("Low-Resource Machine Translation Research", className="text-dark"),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "Implemented and adapted several NLP data pre-processing techniques, including ",
                            html.B("Joint Dropout"),
                            " and ",
                            html.B("Data Diversification"),
                            ", to limited-data settings. These techniques were originally developed ",
                            "for big data settings. ",
                            html.B("Joint Dropout"),
                            " improved translation quality, achieving a ",
                            html.B("20.1 BLEU"),
                            " score (vs. baseline 18.6), while ",
                            html.B("Data Diversification"),
                            " yielded ",
                            html.B("11.4 BLEU"),
                            ", highlighting its limitations in data-constrained environments.",
                        ],
                        className="text-dark",
                        style={
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
                        "background": "white",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid black",
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
                        "border-bottom": "2px solid black",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("Sanguage", className="text-dark"),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "Developed ",
                            html.B("Sanguage"),
                            ", an Android mobile app that recognizes and translates ",
                            html.B("American Sign Language (ASL) alphabet letters"),
                            " into text in real time using the TensorFlow Lite model ",
                            html.B("EfficientNet-Lite0"),
                            ", achieving ",
                            html.B("99.43% test set classification accuracy"),
                            ". While this prototype focuses on Alphabetical letters, it demonstrates the potential ",
                            "for a larger-scale system that could enable real-time ASL translation for seamless communication."
                        ],
                        className="text-dark",
                        style={
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
                                    href="https://github.com/maladinp/ECE454FinalProject",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
                    ],
                    style={
                        "background": "white",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid black",
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
                        "border-bottom": "2px solid black",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("Fantasy Football Crystal Ball", className="text-dark"),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                       html.P([
                            "Developed ",
                            html.B("FFCrystal Ball"),
                            ", a fantasy football analytics tool leveraging ",
                            html.B("quantile regression"),
                            " with ",
                            html.B("gradient boosting"),
                            " to predict a player's range of fantasy point outcomes. This approach ",
                            "improved mean absolute error by ",
                            html.B("15%"),
                            " compared to a baseline linear regression model, providing more accurate player performance projections."
                        ],
                        className="text-dark",
                        style={
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
                                    href="https://github.com/maladinp/ECE454FinalProject",
                                    target="_blank",
                                    color="dark",
                                    className="m-1 px-1 py-1",
                                ),
                            ],
                            className="d-flex justify-content-center flex-wrap mt-2",
                        ),
                    ],
                    style={
                        "background": "white",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid black",
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
                        "border-bottom": "2px solid black",
                    },
                ),

                html.Div(
                    children=[
                        html.A(
                            children=[
                                html.H3("October Odds", className="text-dark"),
                            ],
                            style={
                                "color": "black",
                                "font-size": "24px",
                                "text-align": "center",
                            },
                        ),
                        html.P([
                            "This project is currently in progress and aims to provide a dynamic visualization of each ",
                            html.B("MLB team's probability of making the playoffs"),
                            " at any point in the season. The app will utilize a ",
                            html.B("win probability model"),
                            " to estimate the likelihood of winning each remaining game and employ ",
                            html.B("Monte Carlo simulation"),
                            " to generate probability distributions for playoff qualification. Additionally, it will display ",
                            html.B("World Series winner odds"),
                            " based on simulated season outcomes."
                        ],
                        className="text-dark",
                        style={
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
                        "background": "white",
                        "padding": "15px",
                        "text-align": "center",
                        "flex-grow": "1",
                    },
                ),
            ],
            style={
                "border-radius": "15px",
                "overflow": "hidden",
                "box-shadow": "2px 2px 10px rgba(0, 0, 0, 0.1)",
                "width": "100%",
                # "max-width": "400px",
                "border": "2px solid black",
                "display": "flex",
                "flex-direction": "column",
                "height": "100%",
            },
        ),
    ])
)

projects = dbc.Row([
    html.H2("Projects", className="text-center text-dark"),
    html.Hr(style={"border-top": "2px solid black", "width": "100%", "max-width": CONFIG['max-width']}),

    dbc.Row([
        dbc.Col([
            nfl_bdb_2025,
            nfl_bdb_2024,
            low_resource_machine_translation
        ], sm=12, md=6, xl=6, className=""),
        dbc.Col([
            saguage,
            ffcrystalball,
            octoberodds
        ], sm=12, md=6, xl=6, className="") 
    ], style={
        "max-width": CONFIG['max-width'],
        # padding below
        "padding": "10px 10px 30px 10px"
    })
], 
justify="center", 
className="d-flex flex-wrap", 
style={
    "padding-left": "20px",
    "padding-right": "20px",
    "padding-top": "40px",
    "background-color": "#9ae7eb",
    "color": "black",
    "border-radius": "10px",
})