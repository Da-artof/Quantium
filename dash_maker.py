from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("data/formatted_sales_data.csv")

fig = px.line(df, x='date', y='sales')

app.layout = html.Div(children=[
    html.H1(children='Sales visualiser'),

    html.Label('Regions'),
    dcc.RadioItems(['north', 'east', 'south', 'west', 'all'],
                   'all', id='region'),

    dcc.Graph(
        id='Sales graph',
        figure=fig
    )
], className='app-header')


@callback(
    Output(component_id='Sales graph', component_property='figure'),
    Input(component_id='region', component_property='value')
)
def update_graph(region):
    if region == 'all':
        return px.line(df, x='date', y='sales')
    return px.line(df[df['region'] == region], x='date', y='sales')


app.run()
