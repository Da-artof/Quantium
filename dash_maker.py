from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("data/formatted_sales_data.csv")

fig = px.line(df, x='date', y='sales')

app.layout = html.Div(children=[
    html.H1(children='Sales visualiser'),

    dcc.Graph(
        id='Sales graph',
        figure=fig
    )
])

app.run()
