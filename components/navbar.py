import dash_bootstrap_components as dbc

# Navbar component with links to sections
navbar = dbc.Navbar(
    dbc.Container([
        # Bold name for the brand
        dbc.NavbarBrand(
            "Luke Neuendorf", 
            className="ms-2 fw-bold text-dark", 
            style={"fontSize": "24px"}
        ),
        
        # Toggler for mobile view (hamburger icon)
        dbc.NavbarToggler(
            id="navbar-toggler",
            n_clicks=0,
            className="custom-toggler"  # Add a custom class to target the icon in CSS
        ),
        
        # Collapsable Nav links (shown when toggler is clicked on smaller screens)
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
            className="justify-content-end text-end"  # Right-align links, padding on the right
        ),
    ], fluid=True),  # Full-width container
    color="white",
    dark=False,
    sticky="top",
    className="py-1",  # Reduce vertical padding to make the navbar less tall
    style={"borderBottom": "2px solid #404747"}  # Add grey line at the bottom
)
