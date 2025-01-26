from dash import html
import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    dbc.Container([
        html.A(
            dbc.Row([
                dbc.Col(dbc.NavbarBrand("Luke Neuendorf", className="ms-2")),
            ],
            align="center",
            className="g-0",
            ),
            href="/",
            style={"textDecoration": "none"},
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse(
            dbc.Nav([
                    dbc.NavItem(dbc.NavLink("Projects", href="#projects")),
                    dbc.NavItem(dbc.NavLink("Experience", href="#experience")),
                    dbc.NavItem(dbc.NavLink("Education", href="#education")),
                    dbc.NavItem(dbc.NavLink("Skills", href="#skills")),
                ],
                className="ms-auto",
                navbar=True,
            ),
            id="navbar-collapse",
            is_open=False
        ),
    ]),
    color="white",
    dark=False,
    className="mb-5",
)