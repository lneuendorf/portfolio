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
                    },
                    loop=True,
                    autoPlay=True,
                    muted=True,
                    controls=False,
                )
            ]),
            html.Script("""
                document.querySelector('video').setAttribute('playsinline', '');
            """)
        ], sm=12, md=5),
        dbc.Col([
            html.P(
                "Hi, my name is", 
                style={"font-size": "18px", "margin-bottom": "5px"}
            ), html.H1(
                "Luke", 
                style={"font-size": "36px", "margin-bottom": "10px"}
            ), html.P([
                "I'm a data engineer with a background in computer engineering. ",
                "I specialize in machine learning, data science, and cloud-based solutions, ",
                "and have extensive experience in building APIs, automating processes, and developing predictive models. ",
                "I earned my MS in Computer Engineering with a focus on machine learning from the University of Wisconsin-Madison. ",
                "Currently, I'm working as a Data Engineer at Schneider National, where I build scalable data pipelines ",
                "and deploy machine learning models to Azure Kubernetes."
            ], style={}),
        ], sm=12, md=7),
    ],
    style={
        "padding-left": CONFIG['padding-left'],
        "padding-right": CONFIG['padding-right'],
    })
)