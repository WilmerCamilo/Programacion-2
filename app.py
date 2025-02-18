import dash
from dash import html
import dash_bootstrap_components as dbc
import math
from dash.dependencies import Input, Output

#import fronted
from fronted.navegador.navegador import navegador
from fronted.derecha.derecha import derecha

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(navegador, md=12, style={'background-color':'gray'}),
                dbc.Col(derecha, md=4, style={'background-color':'gray'}),

            ]
        )
    ]
)



if __name__ == '__main__':
    app.run_server(debug=True)