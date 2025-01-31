from dash import html
import dash_bootstrap_components as dbc

projects = html.Div([
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
    })
])