from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

about = (
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Img(
                    src="/assets/head.png",  # Update to the image file
                    className="img-fluid",
                    style={
                        "width": "80%",
                        "max-width": "350px",
                    },
                )
            ], className="d-flex justify-content-center"),
        ], sm=12, md=5, className="d-flex align-items-center justify-content-center justify-content-md-end"),
        
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
                    "analytics-related side projects, but you can also find me playing disc golf and ultimate "
                    "frisbee or watching Wisconsin sports teams."
                ], style={"text-align": "justify", "color": CONFIG['text-dark']}),
            ], className="text-left"),
        ], sm=12, md=7, className="d-flex align-items-start align-items-md-center justify-content-start"),
        # align-items-start on small screens, align-items-center on medium+
    ],
    style={
        "height": "100vh",
        "padding-left": CONFIG['padding-left'],
        "padding-right": CONFIG['padding-right'],
        "padding-top": "20px",
        "padding-bottom": "20px",
        # "display": "flex",
        # "align-items": "center",
        # "justify-content": "center",
        "flex-wrap": "wrap",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
    },
    id="about")
)
