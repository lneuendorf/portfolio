from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Row([
    dbc.Col([
        # Brief Summary Section
        dbc.Card([
            dbc.CardBody([
                html.H2("Luke Neuendorf", className="card-title text-dark"),
                html.P([
                    "(608) 616-4787 ❖ lneuendorf@proton.me ❖ github.com/lneuendorf ❖ linkedin.com/in/luke-neuendorf"
                ], className="card-text text-dark"),
                html.P("Computer Engineer focused on Machine Learning and Data Science, with a proven track record in solving real-world problems.", className="text-dark")
            ])
        ], className="mb-4"),
        # Work Experience Section
        dbc.Card([
            dbc.CardBody([
                html.H3("Relevant Work Experience", id="experience", className="card-title text-dark"),
                html.H4("Schneider National, Data Engineer", className="card-subtitle text-dark"),
                html.P("Jan 2024 – Present", className="text-dark"),
                html.Ul([
                    html.Li("Developed a process-based model to classify late orders by cause."),
                    html.Li("Upgraded a legacy Java pipeline to Python, deployed in Azure Kubernetes."),
                    html.Li("Created APIs using Flask for various projects.")
                ])
            ])
        ], className="mb-4"),
        # Education Section
        dbc.Card([
            dbc.CardBody([
                html.H3("Education", id="education", className="card-title text-dark"),
                html.H4("University of Wisconsin-Madison", className="card-subtitle text-dark"),
                html.P("Masters of Science, Computer Engineering - Machine Learning and Signal Processing", className="text-dark"),
                html.P("December 2023", className="text-dark"),
                html.P("GPA: 3.75/4.0", className="text-dark"),
                html.H4("Bachelors of Science, Computer Engineering", className="text-dark"),
                html.P("August 2022", className="text-dark"),
                html.P("GPA: 3.44/4.0", className="text-dark")
            ])
        ], className="mb-4"),
        # Skills Section
        dbc.Card([
            dbc.CardBody([
                html.H3("Skills & Interests", id="skills", className="card-title text-dark"),
                html.Ul([
                    html.Li("Programming Languages: Python, SQL, C, C++, Java, R, Matlab"),
                    html.Li("Machine Learning & Data Science: scikit-learn, XGBoost, PYMC, Pytorch, Numpy, Pandas"),
                    html.Li("Data Visualization: PowerBI, Tableau, Dash Plotly, Matplotlib, Seaborn"),
                    html.Li("Cloud & Big Data Tools: Microsoft Azure, Snowflake, Redis, Kafka"),
                    html.Li("DevOps Tools: Dynatrace, Kibana, Redhat"),
                    html.Li("API & Testing Tools: Insomnia, Flask")
                ])
            ])
        ], className="mb-4"),
        # Projects Section with links
        dbc.Card([
            dbc.CardBody([
                html.H3("Projects", id="projects", className="card-title"),
                html.Div([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card([
                                dbc.CardImg(src="/assets/nfl1.png", top=True),
                                dbc.CardBody([
                                    html.H4("2025 NFL Big Data Bowl - Motion for More"),
                                    dbc.Button("View Write-Up", href="/nfl2025_writeup", color="primary", className="me-2"),
                                    dbc.Button("View Dashboard", href="/nfl2025_dashboard", color="primary", className="me-2"),
                                    dbc.Button("View Code", href="/nfl2025_code", color="primary")
                                ])
                            ])
                        ], md=6, className="mb-4"),
                        dbc.Col([
                            dbc.Card([
                                dbc.CardImg(src="/assets/nfl2.png", top=True),
                                dbc.CardBody([
                                    html.H4("2024 NFL Big Data Bowl - Tackle Depth Over Expected"),
                                    dbc.Button("View Write-Up", href="/nfl2024_writeup", color="primary", className="me-2"),
                                    dbc.Button("View Code", href="/nfl2024_code", color="primary")
                                ])
                            ])
                        ], md=6, className="mb-4")
                    ])
                ])
            ])
        ])
    ], lg=8)
], justify="center")