
from dash import dcc, html
from dash.dependencies import Input, Output
from app import app
from apps import app1, app2, app3, homepage

app.layout = html.Div(style={'backgroundColor': '#FCF6F5FF'}, children=[
    html.H1("GLAUCOMA DETECTON", style={'text-align': 'center',  'color': '#990011FF', 'font-family': 'Arial, sans-serif'}),
    html.Hr(),
    html.H2("Exploratory Data Analysis", style={'color': '#990011FF', 'font-family': 'Arial, sans-serif'}),
    html.Br(),
    dcc.Location(id='url'),
    dcc.Link("Univariate Analysis", href='/apps/app1', style={'color': '#990011FF', 'font-family': 'Arial, sans-serif'}),
    html.Br(),
    html.Br(),
    dcc.Link("Bivariate Analysis", href='/apps/app2', style={'color': '#990011FF', 'font-family': 'Arial, sans-serif'}),
    html.Br(),
    html.Br(),
    dcc.Link("Trivariate Analysis", href='/apps/app3', style={'color': '#990011FF', 'font-family': 'Arial, sans-serif'}),
    html.Br(),
    html.Br(),
    html.Hr(),
    html.Div(id='page_content'),
    html.Hr(),
])

@app.callback(Output('page_content', 'children'),
              Input('url', 'pathname'))
def display_page_content(path):
    if path == '/apps/app1':
        return app1.layout
    elif path == '/apps/app2':
        return app2.layout
    elif path == '/apps/app3':
        return app3.layout
    else:
        return homepage.layout

if __name__ == '__main__':
    app.run(debug=True)