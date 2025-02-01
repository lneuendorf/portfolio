from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

about = (
    dbc.Row([
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
                        "padding-top": "20px",
                    },
                    loop=True,
                    autoPlay=True,
                    muted=True,
                    controls=False,
                )
            ], className="d-flex justify-content-center"),
            html.Script("""
                document.querySelector('video').setAttribute('playsinline', '');
            """)
        ], sm=12, md=5, className="d-flex justify-content-center"),
        dbc.Col([
            html.Div([
                html.P(
                    "Hi, my name is", 
                    style={"font-size": "18px", "margin-bottom": "5px"}
                ),
                html.H1(
                    "Luke", 
                    style={"font-size": "36px", "margin-bottom": "10px"}
                ),
                html.P([
                    "I am a Green Bay based Data Engineer with a bachground in Computer Engineering "
                    "and Machine Learning. I enjoys spending my free time on sports analytics "
                    "related side projects, but you can also find me playing disc golf, ultimate "
                    "frisbee, or watching the Packers."
                ], style={"text-align": "justify"}),
                # NOTE: this site is a work in progress
                html.P([
                    "NOTE: This site is a work in progress. Check back soon for updates!"
                ], style={"text-align": "justify", "font-style": "italic", "margin-top": "20px"}),
            ], className="text-left")
        ], sm=12, md=7, className="d-flex align-items-center justify-content-center"),
    ],
    style={
        "min-height": "calc(100vh - 64px)",  # Adjust for navbar height (including underline)
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
    })
)