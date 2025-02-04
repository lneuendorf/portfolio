from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

# Dictionary mapping skills to image paths
skill_images = {
    "NumPy": "/assets/skills/numpy.png",
    "Pandas": "/assets/skills/pandas.png",
    "PagerDuty": "/assets/skills/pagerduty.png",
    "Dynatrace": "/assets/skills/dynatrace.png",
    "Kibana": "/assets/skills/kibana.png",
    "Docker": "/assets/skills/docker.png",
    "Kubernetes": "/assets/skills/kubernetes.png",
    "OpenShift": "/assets/skills/openshift.png",
    "MLflow": "/assets/skills/mlflow.png",
    "Snowflake": "/assets/skills/snowflake.png",
    "SQL Developer": "/assets/skills/sqldeveloper.png",
    "Redis": "/assets/skills/redis.png",
    "SQLite": "/assets/skills/sqlite.png",
    "Dash Plotly": "/assets/skills/dashplotly.png", 
    "PowerBI": "/assets/skills/powerbi.png",
    "Tableau": "/assets/skills/tableau.png",
    "Matplotlib": "/assets/skills/matplotlib.png",
    "Seaborn": "/assets/skills/seaborn.png",
    "Dask": "/assets/skills/dask.png",
    "Kafka": "/assets/skills/kafka.png",
    "Apache Spark": "/assets/skills/spark.png",
    "Scikit-learn": "/assets/skills/scikitlearn.png",
    "XGBoost": "/assets/skills/xgboost.png",
    "PYMC": "/assets/skills/pymc.png",
    "PyTorch": "/assets/skills/pytorch.png",
    "TensorFlow": "/assets/skills/tensorflow.png",
    "Python": "/assets/skills/python.png",
    "SQL": "/assets/skills/sql.png",
    "Java": "/assets/skills/java.png",
    "C": "/assets/skills/c.png",
    "C++": "/assets/skills/c++.png",
    "R": "/assets/skills/r.png",
    "Matlab": "/assets/skills/matlab.png",
}

def create_skill_badges(skills):
    return html.Div([
        html.Span(
            html.Img(src=skill_images[skill], style={"height": "24px", "width": "auto", "margin-right": "5px", "display": "block", "margin": "0 auto"})
            if skill in skill_images else skill,
            style={
                "backgroundColor": "white",
                "color": "#black",
                "margin": "3px",
                "borderRadius": "4px",
                "fontSize": "14px",
                "display": "inline-flex",  # Ensure proper alignment with images
                "alignItems": "center",
                "padding": "4px 8px",
            },
            className="badge"
        ) for skill in skills
    ],
    className="d-flex flex-wrap justify-content-center")

languages = dbc.Card([
    dbc.CardBody([
        html.H5("Programming Languages", className="text-dark text-center"),
        create_skill_badges(["Python", "SQL", "Java", "C", "C++", "R", "Matlab"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")


machine_learning = dbc.Card([
    dbc.CardBody([
        html.H5("Machine Learning", className="text-dark text-center"),
        create_skill_badges(["Scikit-learn", "XGBoost", "PYMC", "PyTorch", "TensorFlow"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

big_data = dbc.Card([
    dbc.CardBody([
        html.H5("Big Data", className="text-dark text-center"),
        create_skill_badges(["Dask","Kafka","Apache Spark"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

data_viz = dbc.Card([
    dbc.CardBody([
        html.H5("Data Visualization", className="text-dark text-center"),
        create_skill_badges(["Dash Plotly", "PowerBI", "Tableau", "Matplotlib", "Seaborn"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

database = dbc.Card([
    dbc.CardBody([
        html.H5("Database", className="text-dark text-center"),
        create_skill_badges(["Snowflake", "SQL Developer", "Redis", "SQLite"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

devops_mlops = dbc.Card([
    dbc.CardBody([
        html.H5("DevOps & MLOps", className="text-dark text-center"),
        create_skill_badges(["Docker", "Kubernetes", "OpenShift", "MLflow"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

monitoring = dbc.Card([
    dbc.CardBody([
        html.H5("Monitoring & Incident Response", className="text-dark text-center"),
        create_skill_badges(["PagerDuty", "Dynatrace", "Kibana"])
    ], style={"padding": "10px 10px 20px 10px"})
], className="shadow-sm rounded-3 mb-3")

# Skill Category Cards
data_processing = dbc.Card([
    dbc.CardBody([
        html.H5("Data Processing & Scientific Computing", className="text-dark text-center"),
        create_skill_badges(["NumPy", "Pandas"])
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
                devops_mlops,
                monitoring,
                data_processing,
            ], lg=4, xs=6, className="col-xxs-12"),
            dbc.Col([
                languages,
                machine_learning,
                big_data,
            ], lg=4, xs=6, className="col-xxs-12"),
            dbc.Col([
                database,
                data_viz,
            ], lg=4, xs=6, className="col-xxs-12"),
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

