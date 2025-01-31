from dash import html
import dash_bootstrap_components as dbc

education = dbc.Row([
    html.H2("Education", className="text-center text-white my-4"),

    dbc.Row(
        children=[
            dbc.Col(
                html.Div(
                    children=[
                        dbc.Row([
                            dbc.Col(
                                html.Img(
                                    src="/assets/uw-madison-logo.png",
                                    className="img-fluid",
                                    style={
                                        "max-width": "100%",
                                        "height": "auto",
                                    }
                                ),
                                width=2,
                            ),
                            dbc.Col(
                                html.Div([
                                    html.H4("MS in Computer Engineering - University of Wisconsin-Madison", className="text-white"),
                                    html.P(
                                        "Focus on Machine Learning, Signal Processing. Coursework: Machine Learning, Big Data Systems, "
                                        "Advanced NLP, Optimization, Digital Image Processing, Probability & Information Theory in ML.",
                                        className="text-white",
                                    ),
                                ], style={"position": "relative", "z-index": 1}),
                                width=10,
                            ),
                        ]),
                    ],
                    style={"position": "relative", "z-index": 1},
                ),
                width={"size": 12, "offset": 0},
            ),
            dbc.Col(
                html.Div(
                    children=[
                        dbc.Row([
                            dbc.Col(
                                html.Img(
                                    src="/assets/uw-madison-logo.png",
                                    className="img-fluid",
                                    style={
                                        "max-width": "100%",
                                        "height": "auto",
                                    }
                                ),
                                width=2,
                            ),
                            dbc.Col(
                                html.Div([
                                    html.H4("BS in Computer Engineering - University of Wisconsin-Madison", className="text-white"),
                                    html.P(
                                        "Graduated with a focus on Data Science, Autonomous Systems. Activities: Data Science Club, Wisconsin Autonomous, "
                                        "Wisconsin Space Race, Running Club.",
                                        className="text-white",
                                    ),
                                ], style={"position": "relative", "z-index": 1}),
                                width=10,
                            ),
                        ]),
                    ],
                    style={"position": "relative", "z-index": 1},
                ),
                width={"size": 12, "offset": 0},
            ),
        ],
        className="mb-4",
    ),
], justify="center", className="d-flex flex-wrap", style={
    "padding-left": "20px",
    "padding-right": "20px",
    "padding-top": "40px",
    "background-color": "#28a745",
    "color": "white",
    "border-radius": "10px",
})