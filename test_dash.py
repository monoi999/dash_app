# [4-1]

from dash import Dash, html

app = Dash(__name__)

app.layout = html.Div(children=[
    html.Div(children='Exam Div'),
    html.Br(),
    html.Div(children=[
        html.H1(children='Exam H1'),
        html.P(children='Exam P')
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True) 