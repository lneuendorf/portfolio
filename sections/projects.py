from dash import html
import dash_bootstrap_components as dbc

from config.config import CONFIG

projects = dbc.Row([
    html.H2("Projects", className="text-center text-dark my-4"),

    dbc.Row(
        children=[
            dbc.Col(
                html.Div(
                    children=[
                        html.Div(
                            children=[
                                html.A(
                                    children=[
                                        html.H3("Project 1: NFL Big Data Bowl", className="text-dark"),
                                    ],
                                    href="https://github.com/username/project1",
                                    style={
                                        "text-decoration": "none",
                                        "color": "black",
                                        "font-size": "24px",
                                        "transition": "transform 0.3s ease-in-out",
                                    },
                                    className="project-title",
                                ),
                                html.P(
                                    "Developed a predictive model using Bayesian linear regression to forecast NFL player performance. "
                                    "Created an interactive dashboard with Dash Plotly.",
                                    className="text-dark",
                                ),
                            ],
                            style={"position": "relative", "z-index": 1},
                        ),
                        html.Img(
                            src="/assets/motion.gif",
                            style={
                                "position": "absolute",
                                "top": 0,
                                "left": 0,
                                "width": "100%",
                                "height": "100%",
                                "object-fit": "cover",
                                "z-index": -1,
                                "opacity": 0.5,
                            }
                        ),
                    ],
                    style={"position": "relative", "height": "400px"},
                ),
                width={"size": 6, "offset": 0},
            ),
            dbc.Col(
                html.Div(
                    children=[
                        html.H3("Project 2: NFL Fantasy Football Models", className="text-dark"),
                        html.P(
                            "Developed models using quantile regression and gradient boosting to optimize NFL fantasy football picks. "
                            "Created a comprehensive dashboard for analysis and visualization.",
                            className="text-dark",
                        ),
                        dbc.Button("View Project", href="https://github.com/username/project2", color="primary"),
                    ]
                ),
                width={"size": 6, "offset": 0},
            ),
            dbc.Col(
                html.Div(
                    children=[
                        html.H3("Project 3: Low-Resource Machine Translation", className="text-dark"),
                        html.P(
                            "Worked on a machine translation model for low-resource languages using joint dropout and data diversification techniques.",
                            className="text-dark",
                        ),
                        dbc.Button("View Project", href="https://github.com/username/project3", color="primary"),
                    ]
                ),
                width={"size": 6, "offset": 0},
            ),
            dbc.Col(
                html.Div(
                    children=[
                        html.H3("Project 4: Image Classification Model", className="text-dark"),
                        html.P(
                            "Built a convolutional neural network (CNN) for image classification using TensorFlow and Keras. "
                            "Achieved 85% accuracy on a custom dataset.",
                            className="text-dark",
                        ),
                        dbc.Button("View Project", href="https://github.com/username/project4", color="primary"),
                    ]
                ),
                width={"size": 6, "offset": 0},
            ),
        ],
        style={"max-width": CONFIG['max-width']},
        className="mb-4",
    ),
], 
justify="center", 
className="d-flex flex-wrap", 
style={
    "padding-left": "20px",
    "padding-right": "20px",
    "padding-top": "40px",
    "background-color": "#9ae7eb",
    "color": "black",
    "border-radius": "10px",
})