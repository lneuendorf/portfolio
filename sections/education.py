from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

education = dbc.Row([
    html.H2(
        "Education",
        style={
            "margin-bottom": "30px",
            "font-size": "32px",
            "font-weight": "bold",
            "max-width": CONFIG['max-width'],
            "margin": "0 auto",
            "padding-bottom": "25px",
        },
        className="text-dark text-center"
    ),

    # Divider Line
    html.Hr(style={"border-top": "2px solid black", "width": "100%", "max-width": CONFIG['max-width']}),

    # MS in Computer Engineering - UW-Madison
    dbc.Col([
        dbc.Row([
            dbc.Col([
                html.Img(
                    src="/assets/uw-madison-logo.png",
                    className="img-fluid",
                    style={"max-width": "200px", "height": "auto", "margin-bottom": "20px"}
                )
            ], sm=12, md=2, className="align-self-center", style={"text-align": "center"}),

            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        dbc.Row([
                            html.H4("M.S. Computer Engineering", style={"margin-bottom": "5px"}),
                            html.H4("University of Wisconsin-Madison", style={"margin-top": "0px"}),
                        ], className="text-dark text-md-start text-center"
                        ), sm=12, md=8
                    ),
                    dbc.Col(
                        html.H4(
                            "Sept 2022 - Dec 2023",
                            className="text-dark text-md-end text-center date-text"
                        ), sm=12, md=4
                    ),
                ], className="text-light"),
                
                html.Div([
                    html.B("Focus: "),
                    "Machine Learning & Data Science",
                    html.Br(),
                    html.B("Coursework: "),
                    "Machine Learning, Big Data Systems, Advanced NLP, Optimization, ",
                    "Digital Image Processing, Probability & Information Theory in ML, Theoretical Foundations of Data Science",
                ], className="text-dark"),
            ], sm=12, md=10),
        ],
        style={"max-width": CONFIG['max-width']},
        className="w-100 justify-content-center align-items-center"),
    ], xs=12, sm=12, md=12, lg=12, xl=12,
    className="d-flex align-items-center justify-content-center"),

    # Divider Line
    html.Div(style={"height": "10px"}),
    html.Hr(style={"border-top": "2px solid black", "width": "100%", "max-width": CONFIG['max-width']}),

    # BS in Computer Engineering - UW-Madison
    dbc.Col([
        dbc.Row([
            dbc.Col([
                html.Img(
                    src="/assets/uw-madison-logo.png",
                    className="img-fluid",
                    style={"max-width": "200px", "height": "auto", "margin-bottom": "20px"}
                )
            ], sm=12, md=2, className="align-self-center", style={"text-align": "center"}),

            dbc.Col([
                dbc.Row([
                    dbc.Col(
                        dbc.Row([
                            html.H4("B.S. Computer Engineering", style={"margin-bottom": "5px"}),
                            html.H4("University of Wisconsin-Madison", style={"margin-top": "0px"}),
                        ], className="text-dark text-md-start text-center"
                        ), sm=12, md=8
                    ),
                    dbc.Col(
                        html.H4(
                            "Aug 2017 - Aug 2022",
                            className="text-dark text-md-end text-center date-text"
                        ), sm=12, md=4
                    ),
                ], className="text-light"),
                
                html.Div([
                    html.B("Activities: "),
                    "Data Science Club, Wisconsin Autonomous, Wisconsin Space Race"
                ], className="text-dark"),
            ], sm=12, md=10),
        ],
        style={"max-width": CONFIG['max-width']},
        className="w-100 justify-content-center align-items-top"),
    ], xs=12, sm=12, md=12, lg=12, xl=12,
    className="d-flex align-items-center justify-content-center"),

    # Divider Line
    html.Div(style={"height": "10px"}),
    html.Hr(style={"border-top": "2px solid black", "width": "100%", "max-width": CONFIG['max-width']}),
],
style={
    "padding-left": CONFIG['padding-left'],
    "padding-right": CONFIG['padding-right'],
    "padding-top": "40px",
    "padding-bottom": "20px",
    "background": "linear-gradient(to right, #ccd7f9, #ccf9e3)",  # Horizontal color fade
    "color": "black",
    "justify-content": "center",
    "align-items": "center",
    "margin": "0 auto",
    "border-radius": "10px",
},
id="education"
)
