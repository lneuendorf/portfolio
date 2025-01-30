from dash import html
import dash_bootstrap_components as dbc

# Social media icons, replace with actual links
footer = html.Div(
    children=[
        dbc.Row(
            children=[
                dbc.Col(
                    dbc.Nav(
                        children=[
                            dbc.NavItem(
                                dbc.NavLink(
                                    "BlueSky", href="https://bsky.app/profile/lukeneuendorf.bsky.social", target="_blank", className="text-light"
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    html.Img(src="/assets/github.png", height="30px"),
                                    href="https://github.com/lneuendorf", target="_blank",
                                    className="text-light"
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    html.Img(src="/assets/linkedin.png", height="30px"),
                                    href="https://www.linkedin.com/in/luke-neuendorf/", target="_blank",
                                    className="text-light"
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    "lneuendorf@proton.me", className="text-light"
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    "+1 (608)-616-4787", className="text-light"
                                )
                            ),
                        ],
                        className="d-flex justify-content-center",
                    ),
                    width=12,
                ),
            ],
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    html.P(
                        "Made with Dash Plotly",
                        className="text-center text-light",
                    ),
                    width=12,
                ),
            ],
        ),
        dbc.Row(
            children=[
                dbc.Col(
                    html.P(
                        "© 2025 Luke Neuendorf. All Rights Reserved.",
                        className="text-center text-light",
                    ),
                    width=12,
                ),
            ],
        ),
    ],
    className="bg-dark text-light py-1",
    id="footer",  # Add an id to target the footer
)