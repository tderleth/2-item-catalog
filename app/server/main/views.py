#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Main views."""


from flask import render_template, Blueprint


main = Blueprint('main', __name__,)


@main.route('/')
def index():
    """Render landing page."""
    return render_template('index.html')
