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
        ], xs=12, sm=5, className="custom-mt-sm d-flex align-items-center justify-content-center"),  # Center vertically and horizontally on xs screens
        # Text Column
        dbc.Col([
            html.Div([
                html.P(
                    "Hi 👋, my name is", 
                    style={"font-size": "18px", "margin-bottom": "5px", "color": CONFIG['text-dark']}
                ),
                html.H1(
                    "Luke Neuendorf", 
                    style={"font-size": "36px", "margin-bottom": "10px", "color": CONFIG['text-dark']}
                ),
                html.P([
                    "I am a Green Bay-based Data Engineer with a background in Computer Engineering "
                    "and Machine Learning. I enjoy spending my free time on sports "
                    "analytics-related side projects 📊, but you can also find me playing disc golf 平, ultimate "
                    "frisbee 🥏, biking 🚴🏼, or watching Wisconsin sports 🏈."
                ], style={"text-align": "justify", "color": CONFIG['text-dark']}),
            ], className="text-left"),
        ], xs=12, sm=7, className="d-flex align-items-center", style={"margin-top": "20px"}),  # Center vertically on xs screens
    ],
    className="d-flex flex-column flex-md-row align-items-center justify-content-center",  # Center items vertically and horizontally
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