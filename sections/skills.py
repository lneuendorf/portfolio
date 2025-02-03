from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

def create_skill_badges(skills):
    return html.Div([
        html.Span(
            skill, 
            style={
                "backgroundColor": "#404747", 
                "color": "#FFFFFF", 
                # "padding": "4px 8px",
                "margin": "3px",  
                "borderRadius": "4px",  # Round the corners
                "fontSize": "14px",
                "display": "inline-block"
            },
            className="badge"
        ) for skill in skills
    ], 
    className="d-flex flex-wrap justify-content-center")

languages = dbc.Card([
    dbc.CardBody([
        html.H4("Programming Languages", className="text-dark text-center"),
        create_skill_badges(["Python", "SQL", "Java", "C", "C++", "R", "Matlab"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")


machine_learning = dbc.Card([
    dbc.CardBody([
        html.H4("Machine Learning & Deep Learning", className="text-dark text-center"),
        create_skill_badges(["scikit-learn", "XGBoost", "PYMC", "Pytorch", "TensorFlow", "Numpy", "Pandas", "SciPy"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

probabilistic_modeling = dbc.Card([
    dbc.CardBody([
        html.H4("Probabilistic Modeling", className="text-dark text-center"),
        create_skill_badges(["PYMC", "Bayesian Modeling"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

big_data = dbc.Card([
    dbc.CardBody([
        html.H4("Big Data & Distributed Computing", className="text-dark text-center"),
        create_skill_badges(["Apache Spark", "Dask", "multiprocessing"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

data_viz = dbc.Card([
    dbc.CardBody([
        html.H4("Data Visualization", className="text-dark text-center"),
        create_skill_badges(["PowerBI", "Tableau", "Dash Plotly", "Matplotlib", "Seaborn"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

stats = dbc.Card([
    dbc.CardBody([
        html.H4("Statistical Analysis & Experimentation", className="text-dark text-center"),
        create_skill_badges(["A/B Testing", "Hypothesis Testing"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

cloud = dbc.Card([
    dbc.CardBody([
        html.H4("Cloud & DevOps", className="text-dark text-center"),
        create_skill_badges(["Docker", "GCP (Google Cloud Platform)", "Azure Cloud", "Kubernetes"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

data_eng = dbc.Card([
    dbc.CardBody([
        html.H4("Data Engineering & ETL", className="text-dark text-center"),
        create_skill_badges(["ETL (Extract, Transform, Load)"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

web_dev = dbc.Card([
    dbc.CardBody([
        html.H4("Web Development & API Development", className="text-dark text-center"),
        create_skill_badges(["Flask"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

# Skills Section Layout
skills = dbc.Row([
    dbc.Col([
        html.H2("Skills", className="text-center text-dark"),
        html.Hr(style={"border-top": "2px solid black", "width": "100%", "max-width": CONFIG['max-width']}),

        # Responsive Skill Cards (3 per row on large screens, 2 per row on medium screens)
        dbc.Row([
            dbc.Col([
                languages,
                machine_learning,
                probabilistic_modeling,
            ], lg=4, xs=6, className="col-xxs-12"),
            dbc.Col([
                big_data,
                data_viz,
                stats,
            ], lg=4, xs=6, className="col-xxs-12"),
            dbc.Col([
                cloud,
                data_eng,
                web_dev,
            ], lg=4, xs=6, className="col-xxs-12")
        ])
    ])
], 
style={
    "padding-left": CONFIG['padding-left'],
    "padding-right": CONFIG['padding-right'],
    "padding-top": "40px",
    "padding-bottom": "20px",
    "display": "flex",
    "align-items": "center",
    "justify-content": "center",
    "flex-wrap": "wrap",
    "max-width": CONFIG['max-width'],
    "margin": "0 auto",
})
