from dash import html
import dash_bootstrap_components as dbc

# Define the navbar height manually, since Dash doesn't provide an easy way to calculate it dynamically.
navbar_height = 56  # The navbar's height is approximately 56px (assuming py-1 adds around 8px of padding vertically).

about = html.Div([
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
    })
])