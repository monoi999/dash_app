# [4-1]

dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
df = px.data.gapminder()

yearList = df['year'].sort_values().unique()
continentList = df['continent'].unique()
marks = { str(year):str(year) for year in yearList }

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP, dbc_css])


app.layout = html.Div([
    dcc.Dropdown(options=continentList, id='continent'),
    dcc.Slider(yearList[0], yearList[-1], step=None, marks=marks, id='year'),
    html.Hr(),
    html.Div(id='result')
], className='dbc w-25 d-grid gap-2 m-2 w-25 h5')

@callback(Output('result','children'),
          Input('continent','value'), Input('year','value'))
def func(continent, year):
    print(continent, year)
    if continent and year :
        popSum = df.query('continent==@continent and year==@year')['pop'].sum()
        return f'Total {continent} Population in {year} => {popSum}'

if __name__ == '__main__':
    app.run_server(debug=True)
