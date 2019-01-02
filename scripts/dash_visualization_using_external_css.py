import dash
import dash_core_components as dcc
import dash_html_components as html

ext_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=ext_stylesheets)

app.layout = html.Div(children=[
    html.H1(children="Dash Visualization using External StyleSheets"),
    html.Div(children="A web Application framework for Python"),
    dcc.Graph(
        id="Example-Graph",
        figure={
            'data': [
                {
                    'x': [1,2,3,4,5], 'y': [6,7,8,8,9], 'type': "bar", 'name': "SF"
                },
                {
                    'x': [1,2,3,4,5], 'y': [10,3,1,6,8], 'type': "bar", 'name': "Montreal"
                }
            ],
            'layout': {
                'title': "Python Data Visualization"
            }

        }
    )
]

)

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
