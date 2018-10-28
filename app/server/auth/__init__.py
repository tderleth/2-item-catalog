#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Initialize package."""

from flask import redirect, url_for
from flask import session as login_session
from functools import wraps


def login_required(f):
    """Check if user is authenticated."""
    @wraps(f)
    def wrap(*args, **kwargs):
        if login_session.get('logged_in'):
            if login_session['logged_in'] is True:
                return f(*args, **kwargs)
        return redirect(url_for('auth.showLogin'))

    return wrap
