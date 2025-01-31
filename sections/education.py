from dash import html
import dash_bootstrap_components as dbc

education = html.Div([
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
    })
])