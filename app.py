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
from sections.footer import footer

app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.QUARTZ, "/assets/styles.css"],
)

app.title = 'Luke Neuendorf'

app.layout = html.Div([
    navbar,
    html.Section([
        about,
    ], id="about"),
    html.Section([
        experience,
    ], id="experience"),
    html.Section([
        education,
    ], id="education"),
    html.Section([
        projects,
    ], id="projects"),
    html.Section([
        skills,
    ], id="skills"),
    html.Section([
        footer,
    ], id="footer"),
])

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=80)