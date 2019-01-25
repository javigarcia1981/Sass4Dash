# -*- coding: utf-8 -*-
from views.index import view_index


views_with_callbacks = {
    'index': view_index,
}


def register_callbacks(app):
    """ Add views callbacks """
    for path in views_with_callbacks:
        views_with_callbacks[path].register_callbacks(app)
