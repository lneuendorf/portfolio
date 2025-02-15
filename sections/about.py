from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

about = (
    dbc.Row([
        # Image Column
        dbc.Col([
            html.Div([
                html.Img(
                    src="/assets/headshot.png", 
                    style={"width": "100%", "height": "auto"}
                )
            ], className="d-flex justify-content-center")
        ], xs=12, sm=5, className="custom-mt-sm"),  # Apply Bootstrap class and custom class
        # Text Column
        dbc.Col([
            html.Div([
                html.P(
                    "Hi 👋, my name is", 
                    style={"font-size": "18px", "margin-bottom": "5px", "color": CONFIG['text-dark']}
                ),
                html.H1(
                    "Luke", 
                    style={"font-size": "36px", "margin-bottom": "10px", "color": CONFIG['text-dark']}
                ),
                html.P([
                    "I am a Green Bay-based Data Engineer with a background in Computer Engineering "
                    "and Machine Learning. I enjoy spending my free time on sports "
                    "analytics-related side projects, but you can also find me playing disc golf, ultimate "
                    "frisbee, or watching the Packers."
                ], style={"text-align": "justify", "color": CONFIG['text-dark']}),
            ], className="text-left"),
        ], xs=12, sm=7, style={"margin-top": "20px"}),
    ],
    className="d-flex flex-column flex-md-row align-items-center",
    style={
        "min-height": "calc(100vh)",
        "padding-left": CONFIG['padding-left'],
        "padding-right": CONFIG['padding-right'],
        "padding-top": "20px",
        "padding-bottom": "20px",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
    },
    id="about",)
)