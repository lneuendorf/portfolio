import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand(
            html.Img(src="/assets/navbar/signature.png", height="35px"),
            className="ms-2 fw-bold text-light"
        ),
        
        dbc.NavbarToggler(
            id="navbar-toggler",
            n_clicks=0,
            className="custom-toggler"
        ),
        
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("About", href="#about", id="nav-about", external_link=True, className="text-light")),
                    dbc.NavItem(dbc.NavLink("Experience", href="#experience", id="nav-experience", external_link=True, className="text-light")),
                    dbc.NavItem(dbc.NavLink("Education", href="#education", id="nav-education", external_link=True, className="text-light")),
                    dbc.NavItem(dbc.NavLink("Projects", href="#projects", id="nav-projects", external_link=True, className="text-light")),
                    dbc.NavItem(dbc.NavLink("Skills", href="#skills", id="nav-skills", external_link=True, className="text-light")),
                ],
                className="ms-auto", navbar=True
            ),
            id="navbar-collapse",
            is_open=False,
            navbar=True,
            className="justify-content-end text-end"
        ),
    ], fluid=True),
    fixed="top",
    # style={"backgroundColor": "#454748"},
    className="py-1",
)
