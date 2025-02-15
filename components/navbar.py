import dash_bootstrap_components as dbc
from dash import html

from config.config import CONFIG

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand(
                html.Img(src="/assets/logo.png", height="40px"),
                className="ms-2 fw-bold text-light custom-font",
            ),

            dbc.NavbarToggler(
                id="navbar-toggler",
                n_clicks=0,
                className="custom-toggler"
            ),

            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("About", href="#about-section", id="nav-about-section", external_link=True, className="text-light")),
                        dbc.NavItem(dbc.NavLink("Experience", href="#experience-section", id="nav-experience-sectoin", external_link=True, className="text-light")),
                        dbc.NavItem(dbc.NavLink("Education", href="#education-section", id="nav-education-section", external_link=True, className="text-light")),
                        dbc.NavItem(dbc.NavLink("Projects", href="#projects-section", id="nav-projects", external_link=True, className="text-light")),
                        dbc.NavItem(dbc.NavLink("Skills", href="#skills-section", id="nav-skills-section", external_link=True, className="text-light")),
                    ],
                    className="ms-auto", navbar=True
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
                className="justify-content-end text-end"
            ),
        ], 
        fluid=True, 
        style={"max-width": f"calc({CONFIG['max-width']} + 100px)"},
        className="d-flex align-items-center justify-content-between"
    ),
    fixed="top",
    className="py-1",
)