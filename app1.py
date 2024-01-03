import pandas as pd
import plotly.express as px
from dash import dcc, html
from app import data

def create_distribution_plot(data, x, nbins=30, marginal='rug', title=''):
    fig = px.histogram(
        data,
        x=x,
        nbins=nbins,
        marginal=marginal,
        title=title,
        labels={'value': x}
    )
    return fig

age_distribution = data['Age']
gender_distribution = data['Gender'].value_counts()

fig_age_distribution = create_distribution_plot(
    age_distribution,
    x='Age',
    title='Distribution Plot of Age'
)

fig_gender_distribution = px.bar(
    x=gender_distribution.index,
    y=gender_distribution.values,
    labels={'x': 'Gender', 'y': 'Count'},
    title='Gender Distribution'
)

layout = html.Div([
    html.H1("Univariate Analysis ", style={'text-align': 'center', 'color': '#00203FFF', 'font-family': 'Arial, sans-serif'}),
    html.Br(),
    dcc.Graph(id='age_distribution_graph', figure=fig_age_distribution),
    dcc.Graph(id='gender_distribution_graph', figure=fig_gender_distribution)
])