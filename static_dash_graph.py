import dash
import dash_core_components as dcc
import dash_html_components as html

# pretty much similar to Flask
app = dash.Dash()

app.layout = html.Div("Intro to Dash")

# the actual content of a tag is contained under a parameter called children
app.layout = html.Div(children="Dash Tutorials")

# The children can also be a list of items


app.layout = html.Div(children=[
    html.H1("Dash Children"),
    dcc.Graph(
        id='Example',
        figure={
            'data':[
                {'x':[1,2,3,4,5], 'y':[14,5,6,6,7], 'type':'line', 'name':'Boats'},
                {'x':[1,2,3,4,5], 'y':[10,4,5,3,2], 'type':'line', 'name':'Cars'}
            ],
            'layout':{
                'title':'Basic Dash Example'
            }
        }
    )
])

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)
