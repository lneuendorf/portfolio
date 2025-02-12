from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

about = (
    dbc.Row([
        # Video Column
        dbc.Col([
            html.Div([
                html.Video(
                    src="/assets/memoji.mov", 
                    className="img-fluid",
                    style={
                        "width": "100%",
                        "max-width": "400px",
                        "object-fit": "cover",
                        "transform": "scale(1.5)",
                        "padding-top": "70px",  # Reduced from 70px to 40px
                    },
                    loop=True,
                    autoPlay=True,
                    muted=True,
                    controls=False,
                )
            ], className="d-flex justify-content-center"),
        ], sm=12, md=5, className="d-flex align-items-end align-items-md-center justify-content-center mb-3 mb-md-0"),  # Added spacing for small screens

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
        ], sm=12, md=7, className="d-flex align-items-start align-items-md-center justify-content-center"),  
        # align-items-start on small screens, align-items-center on medium+
    ],
    style={
        "min-height": "calc(100vh)",
        "padding-left": CONFIG['padding-left'],
        "padding-right": CONFIG['padding-right'],
        "padding-top": "20px",
        "padding-bottom": "20px",
        "display": "flex",
        "align-items": "center",
        "justify-content": "center",
        "flex-wrap": "wrap",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
    },
    id="about",)
)
