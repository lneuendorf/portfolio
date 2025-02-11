education_wide = html.Div(
    style={
        "position": "relative",
        "max-width": CONFIG['max-width'],
        "margin": "0 auto",
        "padding": "0px 0px",
    },
    children=[
        html.Div(
            id="education-line",
            style={
                "position": "absolute",
                "left": "calc(50% - 1px)", 
                "width": "2px",
                "height": "calc(100% - 15px)",  # Adjusted height to fit between boxes
                "background": CONFIG['text-dark'],
                "top": "10px",  # Start below the top circle
            }
        ),
        # Education items
        html.Div(
            [
                # M.S. Computer Engineering
                html.Div(
                    style={
                        "position": "relative",
                        "margin-bottom": "40px",
                        "display": "flex",
                        "align-items": "center",
                    },
                    children=[
                        # Circle with logo
                        html.Div(
                            style={
                                "position": "absolute",
                                "left": "50%",
                                "transform": "translateX(-50%)",
                                "width": "70px",
                                "height": "70px",
                                "border-radius": "50%",
                                "background": "#C5050C",
                                "display": "flex",
                                "align-items": "center",
                                "justify-content": "center",
                                "z-index": 1,
                                "border": f"2px solid {CONFIG['text-dark']}",
                            },
                            children=[
                                html.Img(
                                    src="/assets/ece.png",
                                    style={
                                        "width": "80%",
                                        "height": "auto",
                                    },
                                ),
                            ],
                        ),
                        # Job description box
                        html.Div(
                            style={
                                "width": "45%",
                                "margin-left": "calc(50% + 50px)",
                                "padding": "20px",
                                "background": "white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer
                                html.Div(
                                    style={
                                        "position": "absolute",
                                        "left": "-10px",
                                        "top": "50%",
                                        "transform": "translateY(-50%)",
                                        "width": "0",
                                        "height": "0",
                                        "border-top": "10px solid transparent",
                                        "border-bottom": "10px solid transparent",
                                        "border-right": "10px solid white",
                                    }
                                ),
                                dbc.Row([
                                    html.H3(
                                        "M.S. Computer Engineering",
                                        className="text-md-start text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.H5(
                                        "Sept 2022 - Dec 2023",
                                        className="text-md-start text-center date-text",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.H6(
                                        "GPA: 3.75/4.0",
                                        className="text-md-start text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "10px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.Ul([
                                        html.B("Focus: ", style={"color": CONFIG['text-dark']}),  # Bold with custom color
                                        html.Span(
                                            "Machine Learning & Signal Processing", 
                                            style={"color": CONFIG['text-dark']}),
                                        html.Br(),
                                        html.B("Coursework: ", style={"color": CONFIG['text-dark']}), 
                                        html.Span(
                                            "Machine Learning, Big Data Systems, Advanced NLP, Optimization, "
                                            "Digital Image Processing, Probability & Information Theory in ML, "
                                            "Theoretical Foundations of Data Science",
                                            style={
                                                "color": CONFIG['text-dark'],
                                            }
                                        ),
                                    ], className="text-start text-dark"),
                                ]),
                            ],
                        ),
                    ],
                ),
                # Data Science Intern at Schneider
                html.Div(
                    style={
                        "position": "relative",
                        "margin-bottom": "40px",
                        "display": "flex",
                        "align-items": "center",
                    },
                    children=[
                        # Circle with logo
                        html.Div(
                            style={
                                "position": "absolute",
                                "left": "50%",
                                "transform": "translateX(-50%)",
                                "width": "70px",
                                "height": "70px",
                                "border-radius": "50%",
                                "background": "#C5050C",
                                "display": "flex",
                                "align-items": "center",
                                "justify-content": "center",
                                "z-index": 1,
                                "border": f"2px solid {CONFIG['text-dark']}",
                            },
                            children=[
                                html.Img(
                                    src="/assets/ece.png",
                                    style={
                                        "width": "80%",
                                        "height": "auto",
                                    },
                                ),
                            ],
                        ),
                        # Job description box
                        html.Div(
                            style={
                                "width": "45%",
                                "margin-right": "calc(50% + 50px)",
                                "padding": "20px",
                                "background": "white",
                                "border-radius": "10px",
                                "box-shadow": "0px 0px 15px 5px rgba(0, 0, 0, 0.1)",
                                "position": "relative",
                            },
                            children=[
                                # Triangle pointer
                                html.Div(
                                    style={
                                        "position": "absolute",
                                        "right": "-10px",
                                        "top": "50%",
                                        "transform": "translateY(-50%)",
                                        "width": "0",
                                        "height": "0",
                                        "border-top": "10px solid transparent",
                                        "border-bottom": "10px solid transparent",
                                        "border-left": "10px solid white",
                                    }
                                ),
                                dbc.Row([
                                    html.H3(
                                        "B.S. Computer Engineering",
                                        className="text-md-end text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.H5(
                                        "Sept 2017 - Aug 2022",
                                        className="text-md-end text-center date-text",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "5px"}
                                    ),
                                ]),
                                dbc.Row([
                                    html.H6(
                                        "GPA: 3.44/4.0",
                                        className="text-md-end text-center",
                                        style={"color": CONFIG['text-dark'], "margin-bottom": "10px"}
                                    ),
                                ]),
                                # Job description
                                dbc.Row([
                                    html.Ul([
                                        html.B("Activities: ", style={"color": CONFIG['text-dark']}), 
                                        html.Span(
                                            "Data Science Club, Wisconsin Autonomous, Wisconsin Space Race, Running Club",
                                            style={"color": CONFIG['text-dark']}
                                        ),
                                    ], className="text-start text-dark")
                                ]),
                            ],
                        ),
                    ],
                ),
            ]
        ),
    ]
)