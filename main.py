
from dash import Dash, html, dcc, callback, Input, Output, State
import plotly.express as px

app = Dash(__name__)

# df = px.data.stocks(indexed=True)
# fig = px.line(df, y='GOOG')
# d = {'GOOG':'구글', 'AAPL':'애플', 'AMZN':'아마존', 'MSFT':'마소', 'FB':'페북', 'NFLX':'넷플릭스'}

app.layout = html.Div(children=[ 
    html.H1(children='Stocks Data'),
    # dcc.Dropdown(
    #     id='company',
    #     options=[{'label':d[x], 'value':x} for x in df.columns],
    #     value=df.columns[0], style={'width':'150px'}
    # ),
    # dcc.Graph(id='graph', figure=fig),  
    # dash_table.DataTable(
    #     id='df_sotcks',
    #     columns = [{'name':'date','id':'date'}] + [{"name": i, "id": i} for i in df.columns],
    #     data=df.reset_index().head(5).to_dict('records'), 
    # )
])
# @app.callback(Output("graph", "figure"), Input("company", "value"))
# def display(company):
#     fig = px.line(df, y=company)
#     return fig

if __name__ == '__main__':
    app.run()
    

    
