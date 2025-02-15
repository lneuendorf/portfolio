import dash
import dash_bootstrap_components as dbc
from dash import html

from components.navbar import navbar
from components.callbacks import register_callbacks
from sections.about import about
from sections.experience import experience
from sections.education import education
from sections.projects import projects
from sections.skills import skills
from components.footer import footer

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.QUARTZ, "/assets/styles.css"],
)

app.title = 'Luke Neuendorf'

app.layout = html.Div([
    navbar,
    html.Section([
        about,
    ], id="about-section"),
    html.Section([
        experience,
    ], id="experience-section"),
    html.Section([
        education,
    ], id="education-section"),
    html.Section([
        projects,
    ], id="projects-section"),
    html.Section([
        skills,
    ], id="skills-section"),
    html.Section([
        footer,
    ], id="footer-section"),
])

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=80)