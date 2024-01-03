from app import data
import pandas as pd
from dash import dcc, html
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

sns.set(style="whitegrid")

plt.figure(figsize=(10, 6))
sns.lineplot(x='Diagnosis', y='Age', data=data, marker='o', ci=None)
plt.title('Trend Plot of Age for Different Diagnoses')
plt.xlabel('Diagnosis')
plt.ylabel('Average Age')
buffer_trend = BytesIO()
plt.savefig(buffer_trend, format='png')
buffer_trend.seek(0)
image_uri_trend = base64.b64encode(buffer_trend.read()).decode('utf-8')

fig_count_plot = px.histogram(
    data,
    x='Gender',
    color='Diagnosis',
    barmode='group',
    title='Count Plot of Diagnosis Frequency by Gender',
    labels={'Gender': 'Gender', 'value': 'Frequency'},
)

layout = html.Div([
    html.H1("Bivariate Analysis", style={'text-align': 'center', 'color': '#00203FFF', 'font-family': 'Arial, sans-serif'}),
    html.Br(),  
    html.Img(src=f'data:image/png;base64,{image_uri_trend}', style={'width': '100%'}),
    html.Br(),    
    dcc.Graph(id='count_plot', figure=fig_count_plot)
])

