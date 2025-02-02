import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand(
            "Luke Neuendorf", 
            className="ms-2 fw-bold text-dark", 
            style={"fontSize": "24px"}
        ),
        
        dbc.NavbarToggler(
            id="navbar-toggler",
            n_clicks=0,
            className="custom-toggler"
        ),
        
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavItem(dbc.NavLink("About", href="#about", external_link=True, className="text-dark")),
                    dbc.NavItem(dbc.NavLink("Experience", href="#experience", external_link=True, className="text-dark")),
                    dbc.NavItem(dbc.NavLink("Education", href="#education", external_link=True, className="text-dark")),
                    dbc.NavItem(dbc.NavLink("Skills", href="#skills", external_link=True, className="text-dark")),
                    dbc.NavItem(dbc.NavLink("Projects", href="#projects", external_link=True, className="text-dark")),
                ],
                className="ms-auto", navbar=True
            ),
            id="navbar-collapse",
            is_open=False,
            navbar=True,
            className="justify-content-end text-end"
        ),
    ], fluid=True),
    color="white",
    dark=False,
    fixed="top",
    className="py-1",
    style={"borderBottom": "2px solid gray"}
)
