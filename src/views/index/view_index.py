# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html

from views.index.callbacks import register_index_callbacks

layout = html.Div([
    html.H1('Example index page',
            className='page-title text-centered'),
    html.Section([
        dcc.Dropdown(
            id='my-dropdown',
            options=[
                {'label': 'Tesla', 'value': 'TSLA'},
                {'label': 'Apple', 'value': 'AAPL'},
                {'label': 'Coke', 'value': 'COKE'}
            ],
            value='TSLA'
        ),
        dcc.Graph(id='my-graph')
    ]),
])


def register_callbacks(app):
    register_index_callbacks(app)
