# -*- coding: utf-8
from __future__ import unicode_literals
from __future__ import print_function
from pygments.token import Token


def create_toolbar_handler(is_color, is_fuzzy):

    assert callable(is_color)
    assert callable(is_fuzzy)

    def get_toolbar_items(_):
        """
        Return bottom menu items
        :param _: cli instance
        :return: list of Token.Toolbar
        """
        if is_color():
            color_token = Token.Toolbar.On
            color = 'ON'
        else:
            color_token = Token.Toolbar.Off
            color = 'OFF'
        if is_fuzzy():
            fuzzy_token = Token.Toolbar.On
            fuzzy = 'ON'
        else:
            fuzzy_token = Token.Toolbar.Off
            fuzzy = 'OFF'
        return [
            (Token.Toolbar, ' [F2] Docs '),
            (color_token, ' [F3] Color: {0} '.format(color)),
            (fuzzy_token, ' [F4] Fuzzy: {0} '.format(fuzzy)),
            (Token.Toolbar, ' [F5] Refresh Resources '),
            (Token.Toolbar, ' [F10] Exit ')
        ]
    return get_toolbar_items
