from dash import html
import dash_bootstrap_components as dbc

footer = html.Div(
    children=[
        dbc.Row(
            children=[
                # Social Links (GitHub, Bluesky, LinkedIn)
                dbc.Col(
                    dbc.Nav(
                        children=[
                            dbc.NavItem(
                                dbc.NavLink(
                                    html.Img(src="/assets/linkedin.png", height="30px"),
                                    href="https://www.linkedin.com/in/luke-neuendorf/", 
                                    target="_blank",
                                    className="text-light"
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    html.Img(src="/assets/github.png", height="30px"),
                                    href="https://github.com/lneuendorf", 
                                    target="_blank",
                                    className="text-light"
                                )
                            ),
                            dbc.NavItem(
                                dbc.NavLink(
                                    html.Img(src="/assets/bluesky.png", height="30px"),
                                    href="https://bsky.app/profile/lukeneuendorf.bsky.social", 
                                    target="_blank",
                                    className="text-light"
                                )
                            ),
                        ],
                        className="d-flex justify-content-center",
                    ),
                    width="auto",
                    className="d-flex justify-content-center align-items-center px-2",
                ),

                # Email
                dbc.Col(
                    dbc.Nav(
                        children=[
                            dbc.NavItem(
                                dbc.NavLink(
                                    "lneuendorf@proton.me", 
                                    className="text-light"
                                )
                            ),
                        ],
                        className="d-flex justify-content-center",
                    ),
                    width="auto",
                    className="d-flex justify-content-center align-items-center px-2",
                ),

                # "Made with Dash Plotly"
                dbc.Col(
                    html.P(
                        [
                            "Made with ",
                            html.A(
                                "Dash Plotly", 
                                href="https://dash.plotly.com/", 
                                className="text-light", 
                                target="_blank"
                            ),
                        ],
                        className="text-center text-light m-0",
                    ),
                    width="auto",
                    className="d-flex justify-content-center align-items-center px-2",
                ),
            ],
            className="d-flex flex-wrap justify-content-center align-items-center",
        ),
    ],
    className="bg-dark text-light py-1",
    id="footer",
)
