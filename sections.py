from dash import html
import dash_bootstrap_components as dbc

# Define the navbar height manually, since Dash doesn't provide an easy way to calculate it dynamically.
navbar_height = 56  # The navbar's height is approximately 56px (assuming py-1 adds around 8px of padding vertically).

tldr = html.Div([
    # tldr Section (Already in your existing layout)
    dbc.Row([
        dbc.Col([
            dbc.Row([
                # First column with headshot
                dbc.Col([
                    html.Div([
                        html.Video(
                            src="/assets/memoji.mov", 
                            className="img-fluid",  # Make the video responsive
                            style={
                                "width": "100%",  # Set width to 100% to make it responsive
                                "max-width": "400px",  # Limit the maximum size
                                "object-fit": "cover",  # Ensure content scales correctly
                                "transform": "scale(1.5)",  # Zoom in by 50%
                            },
                            loop=True,  # Loop the video
                            autoPlay=True,  # Autoplay the video
                            muted=True,  # Mute the video (required for autoplay on most browsers)
                            controls=False,  # Disable controls if you don't need them
                        )
                    ], className="d-flex justify-content-center"),
                    html.Script("""
                        document.querySelector('video').setAttribute('playsinline', '');
                    """)
                ], xs=12, md=5, className="mb-4"),  # Stack on small screens and set size for larger screens
                
                # Second and third columns combined for name and about info
                dbc.Col([
                    html.P("Hi, my name is", style={"font-size": "18px", "margin-bottom": "5px"}),
                    html.H1("Luke", className="text-dark", id="about", style={"font-size": "36px", "margin-bottom": "10px"}),
                    html.P([
                        "I'm a data engineer with a background in computer engineering. ",
                        "I specialize in machine learning, data science, and cloud-based solutions, ",
                        "and have extensive experience in building APIs, automating processes, and developing predictive models. ",
                        "I earned my MS in Computer Engineering with a focus on machine learning from the University of Wisconsin-Madison. ",
                        "Currently, I'm working as a Data Engineer at Schneider National, where I build scalable data pipelines ",
                        "and deploy machine learning models to Azure Kubernetes."
                    ], style={"margin-bottom": "5px"}),
                ], xs=12, md=7),  # Stack on small screens, display side-by-side on larger screens
            ], className="align-items-center mt-4", style={
                "min-height": f"calc(100vh - {navbar_height}px)",  # Subtract navbar height from the total height
                "padding-left": "20px",  # Add padding to the left
                "padding-right": "20px",  # Add padding to the right
                "display": "flex",  # Use flexbox
                "align-items": "center",  # Center the content vertically
            })
        ], lg=8)
    ], justify="center", className="d-flex flex-wrap", style={
        "padding-left": "20px",  # Padding to the left
        "padding-right": "20px",  # Padding to the right
    }),

    # Work Experience Section with dark gray background
    dbc.Row([
        dbc.Col([
            html.H2("Relevant Work Experience", style={"margin-bottom": "20px", "font-size": "28px", "font-weight": "bold"}),
            dbc.Row([
                # First column for the work experience details
                dbc.Col([
                    html.Img(
                        src="/assets/schneider-logo.png", 
                        className="img-fluid", 
                        style={
                            "max-width": "100%", 
                            "height": "auto", 
                        }
                    )
                ], lg=2),
                dbc.Col([
                    html.Div([
                        html.H4("Data Engineer at Schneider National (Jan 2024 – Present)", className="text-light"),
                        html.P([
                            "Developed process-based models, upgraded data pipelines, created APIs, deployed to Azure Kubernetes Service."
                        ], className="text-light"),
                    ], className="mb-4"),
                ], lg=10),
                dbc.Col([
                    html.Img(
                        src="/assets/schneider-logo.png", 
                        className="img-fluid", 
                        style={
                            "max-width": "100%", 
                            "height": "auto", 
                        }
                    )
                ], lg=2),
                dbc.Col([
                    html.Div([
                        html.H4("Data Science Intern at Schneider National (May 2023 – Aug 2023)", className="text-light"),
                        html.P([
                            "Implemented image filtering pipelines, developed prediction models, created dashboards, automated processes."
                        ], className="text-light"),
                    ], className="mb-4"),
                ], lg=10),
                dbc.Col([
                    html.Img(
                        src="/assets/schneider-logo.png", 
                        className="img-fluid", 
                        style={
                            "max-width": "100%", 
                            "height": "auto", 
                        }
                    )
                ], lg=2),
                dbc.Col([
                    html.Div([
                        html.H4("Teaching Assistant at UW-Madison ECE Department (Aug 2021 – Dec 2021)", className="text-light"),
                        html.P([
                            "Taught circuit analysis to over 80 students, focused on communication and critical thinking."
                        ], className="text-light"),
                    ], className="mb-4"),
                ], lg=10),
            ], className="mb-4"),
        ], lg=8)
    ], justify="center", className="d-flex flex-wrap", style={
        "padding-left": "20px",  # Padding to the left
        "padding-right": "20px",  # Padding to the right
        "padding-top": "40px",  # Space between sections
        "background-color": "#333333",  # Dark gray background
        "color": "white",  # Light text for contrast
        "border-radius": "10px",  # Optional: rounded corners for a modern look
    }),

    # Education Section with light green background
    dbc.Row([
        # Section Title
        html.H2("Education", className="text-center text-white my-4"),

        # Education Row - Responsive Layout
        dbc.Row(
            children=[
                # Education 1 Row
                dbc.Col(
                    html.Div(
                        children=[
                            # Left column: Image (e.g., university logo or related image)
                            dbc.Row([
                                dbc.Col(
                                    html.Img(
                                        src="/assets/uw-madison-logo.png",  # Replace with your image path
                                        className="img-fluid",  # Make the image responsive
                                        style={
                                            "max-width": "100%",  # Ensure the image scales correctly
                                            "height": "auto",  # Auto height to preserve aspect ratio
                                        }
                                    ),
                                    width=2,  # 2 columns wide
                                ),
                                # Right column: Text content (degree, focus, coursework)
                                dbc.Col(
                                    html.Div([
                                        html.H4("MS in Computer Engineering - University of Wisconsin-Madison", className="text-white"),
                                        html.P(
                                            "Focus on Machine Learning, Signal Processing. Coursework: Machine Learning, Big Data Systems, "
                                            "Advanced NLP, Optimization, Digital Image Processing, Probability & Information Theory in ML.",
                                            className="text-white",
                                        ),
                                    ], style={"position": "relative", "z-index": 1}),
                                    width=10,  # 10 columns wide
                                ),
                            ]),
                        ],
                        style={"position": "relative", "z-index": 1},  # Ensure text stays above the background
                    ),
                    width={"size": 12, "offset": 0},  # Full width for the row
                ),
                # Education 2 Row
                dbc.Col(
                    html.Div(
                        children=[
                            # Left column: Image (e.g., university logo or related image)
                            dbc.Row([
                                dbc.Col(
                                    html.Img(
                                        src="/assets/uw-madison-logo.png",  # Replace with your image path
                                        className="img-fluid",  # Make the image responsive
                                        style={
                                            "max-width": "100%",  # Ensure the image scales correctly
                                            "height": "auto",  # Auto height to preserve aspect ratio
                                        }
                                    ),
                                    width=2,  # 2 columns wide
                                ),
                                # Right column: Text content (degree, focus, coursework)
                                dbc.Col(
                                    html.Div([
                                        html.H4("BS in Computer Engineering - University of Wisconsin-Madison", className="text-white"),
                                        html.P(
                                            "Graduated with a focus on Data Science, Autonomous Systems. Activities: Data Science Club, Wisconsin Autonomous, "
                                            "Wisconsin Space Race, Running Club.",
                                            className="text-white",
                                        ),
                                    ], style={"position": "relative", "z-index": 1}),
                                    width=10,  # 10 columns wide
                                ),
                            ]),
                        ],
                        style={"position": "relative", "z-index": 1},  # Ensure text stays above the background
                    ),
                    width={"size": 12, "offset": 0},  # Full width for the row
                ),
            ],
            className="mb-4",
        ),
    ], justify="center", className="d-flex flex-wrap", style={
        "padding-left": "20px",  # Padding to the left
        "padding-right": "20px",  # Padding to the right
        "padding-top": "40px",  # Space between sections
        "background-color": "#28a745",  # Light green background
        "color": "white",  # Light text for contrast
        "border-radius": "10px",  # Optional: rounded corners for a clean look
    }),

    dbc.Row([
        # Section Title
        html.H2("Projects", className="text-center text-white my-4"),

        # Projects Row - Responsive Layout
        dbc.Row(
            children=[
                # Project 1 Container with Video Background
                dbc.Col(
                    html.Div(
                        children=[
                            html.Div(
                                children=[
                                    # Make the whole project title clickable
                                    html.A(
                                        children=[
                                            html.H3("Project 1: NFL Big Data Bowl", className="text-white"),
                                        ],
                                        href="https://github.com/username/project1",  # Link to the project
                                        style={
                                            "text-decoration": "none",  # Remove underline
                                            "color": "white",  # Text color for the title
                                            "font-size": "24px",  # Default font size
                                            "transition": "transform 0.3s ease-in-out",  # Smooth transition for hover effect
                                        },
                                        className="project-title",  # Add a custom class for styling
                                    ),
                                    html.P(
                                        "Developed a predictive model using Bayesian linear regression to forecast NFL player performance. "
                                        "Created an interactive dashboard with Dash Plotly.",
                                        className="text-white",
                                    ),
                                ],
                                style={"position": "relative", "z-index": 1},  # Ensure text stays above the background GIF
                            ),
                            # GIF Background (Plays on loop)
                            html.Img(
                                src="/assets/motion.gif",  # Replace with the path to your GIF
                                style={
                                    "position": "absolute",
                                    "top": 0,
                                    "left": 0,
                                    "width": "100%",
                                    "height": "100%",
                                    "object-fit": "cover",  # Ensures the GIF covers the full container
                                    "z-index": -1,  # Send GIF to the back
                                    "opacity": 0.5,  # Make the image more transparent
                                }
                            ),
                        ],
                        style={"position": "relative", "height": "400px"},  # Set container height to match the GIF
                    ),
                    width={"size": 6, "offset": 0},  # 50% width on larger screens, 100% on smaller screens
                ),
                # Project 2 Container
                dbc.Col(
                    html.Div(
                        children=[
                            html.H3("Project 2: NFL Fantasy Football Models", className="text-white"),
                            html.P(
                                "Developed models using quantile regression and gradient boosting to optimize NFL fantasy football picks. "
                                "Created a comprehensive dashboard for analysis and visualization.",
                                className="text-white",
                            ),
                            # Optionally, add a link to the project
                            dbc.Button("View Project", href="https://github.com/username/project2", color="primary"),
                        ]
                    ),
                    width={"size": 6, "offset": 0},  # 50% width on larger screens, 100% on smaller screens
                ),
                # Project 3 Container
                dbc.Col(
                    html.Div(
                        children=[
                            html.H3("Project 3: Low-Resource Machine Translation", className="text-white"),
                            html.P(
                                "Worked on a machine translation model for low-resource languages using joint dropout and data diversification techniques.",
                                className="text-white",
                            ),
                            # Optionally, add a link to the project
                            dbc.Button("View Project", href="https://github.com/username/project3", color="primary"),
                        ]
                    ),
                    width={"size": 6, "offset": 0},  # 50% width on larger screens, 100% on smaller screens
                ),
                # Project 4 Container
                dbc.Col(
                    html.Div(
                        children=[
                            html.H3("Project 4: Image Classification Model", className="text-white"),
                            html.P(
                                "Built a convolutional neural network (CNN) for image classification using TensorFlow and Keras. "
                                "Achieved 85% accuracy on a custom dataset.",
                                className="text-white",
                            ),
                            # Optionally, add a link to the project
                            dbc.Button("View Project", href="https://github.com/username/project4", color="primary"),
                        ]
                    ),
                    width={"size": 6, "offset": 0},  # 50% width on larger screens, 100% on smaller screens
                ),
            ],
            className="mb-4",
        ),
    ], justify="center", className="d-flex flex-wrap", style={
        "padding-left": "20px",  # Padding to the left
        "padding-right": "20px",  # Padding to the right
        "padding-top": "40px",  # Space between sections
        "background-color": "#007bff",  # Light green background
        "color": "black",  # Dark text for readability
        "border-radius": "10px",  # Optional: rounded corners for a clean look
    }),
    dbc.Row([
        dbc.Col([
            html.H2("Skills", style={"margin-bottom": "20px", "font-size": "28px", "font-weight": "bold"}),
            # Row for skills
            dbc.Row([
                # Programming Languages Column
                dbc.Col([
                    html.H4("Programming Languages", className="text-dark"),
                    html.Ul([
                        html.Li("Python"),
                        html.Li("SQL"),
                        html.Li("C++"),
                        html.Li("Java"),
                        html.Li("R"),
                        html.Li("Matlab"),
                    ], className="text-dark"),
                ], lg=4),
                # Machine Learning Column
                dbc.Col([
                    html.H4("Machine Learning", className="text-dark"),
                    html.Ul([
                        html.Li("scikit-learn"),
                        html.Li("XGBoost"),
                        html.Li("PYMC"),
                        html.Li("Pytorch"),
                        html.Li("Numpy"),
                        html.Li("Pandas"),
                    ], className="text-dark"),
                ], lg=4),
                # Data Visualization Column
                dbc.Col([
                    html.H4("Data Visualization", className="text-dark"),
                    html.Ul([
                        html.Li("PowerBI"),
                        html.Li("Tableau"),
                        html.Li("Dash Plotly"),
                        html.Li("Matplotlib"),
                        html.Li("Seaborn"),
                    ], className="text-dark"),
                ], lg=4),
            ], className="mb-4"),
        ], lg=8)
    ], justify="center", className="d-flex flex-wrap", style={
        "padding-left": "20px", 
        "padding-right": "20px", 
        "padding-top": "40px", 
        "background": "#e3e2de",  # Gradient background
        "color": "black",  
        "border-radius": "10px", 
    })
])