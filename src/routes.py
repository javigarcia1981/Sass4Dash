# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output

from views.index import view_index

urls = {
    '/': view_index,
    '/index': view_index
}


def register_routes(app):
    """ Add callback to register app routes """
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname in urls:
            return urls[pathname].layout
        return '404'
