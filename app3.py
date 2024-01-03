from app import data
import pandas as pd
import plotly.express as px
from dash import dcc, html

fig_scatter = px.scatter(
    data,
    x='Age',
    y='Intraocular Pressure (IOP)',
    color='Diagnosis',
    title='Scatter Plot between Age and IOP for Different Diagnoses',
    labels={'Age': 'Age', 'Intraocular Pressure (IOP)': 'Intraocular Pressure (IOP)'},
    template='plotly_white'
)

layout = html.Div([
    html.H1("Trivariate Analysis", style={'text-align': 'center', 'color': '#00203FFF', 'font-family': 'Arial, sans-serif'}),
    html.Br(),
    dcc.Graph(id='scatter_plot', figure=fig_scatter)
])
