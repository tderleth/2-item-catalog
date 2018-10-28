from server.auth import views
from flask import session as login_session
from flask import Flask, redirect, url_for, request
from functools import wraps


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if login_session.get('logged_in'):
            if login_session['logged_in'] is True:
                return f(*args, **kwargs)
        return redirect(url_for('auth.showLogin'))

    return wrap
