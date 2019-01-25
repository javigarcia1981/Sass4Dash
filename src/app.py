# -*- coding: utf-8 -*-
import os
import json

import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
from dotenv import load_dotenv

from routes import register_routes
from callbacks import register_callbacks

load_dotenv()

# Server config
app = dash.Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

# Main layout
app.title = 'Example Dashboards'
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', className='container')
])

# Routing
register_routes(app)

# Callbacks
register_callbacks(app)

# External styles
with open('src/styles/external/urls.json') as external_urls:
    urls = json.load(external_urls)
for external_url in urls['external_urls']:
    app.css.append_css({'external_url': external_url})


# Launch with python
if __name__ == '__main__':
    debug = os.environ.get('DEBUG') if (
        os.environ.get('DEBUG') is not None) else False
    app.run_server(debug=debug,
                   port=os.environ.get('APP_PORT') or 8050,
                   host=os.environ.get('APP_HOST') or '0.0.0.0')
