#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Auth and User views."""

from app.server.database import db_session
from app.server.database.user import User
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask import session as login_session
from google.auth.transport import requests
from google.oauth2 import id_token


auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/<username>")
def show(username):
    """Show user by username."""
    u = User.query.filter_by(username=username).first_or_404()
    return "Hello, {}!".format(u.username)


@auth.route('/login')
def showLogin():
    """Show login page."""
    return render_template('auth/login.html')


@auth.route('/google-tokensignin', methods=['POST'])
def google_tokensignin():
    """Post request to save user to database if not existent."""
    try:
        client_id = current_app.config['CLIENT_ID']
        idinfo = id_token.verify_oauth2_token(
            request.get_json(), requests.Request(), client_id)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

    except ValueError:
        # Invalid token
        print "error Token"

    user = getUserByMail(idinfo['email'])

    if (user is None):
        user = User(username=idinfo['given_name'],
                    email=idinfo['email'],
                    picture=idinfo['picture'],
                    gplus_id=idinfo['sub'])
        db_session.add(user)
        db_session.commit()

    login_session['gplus_id'] = user.gplus_id
    login_session['username'] = user.username
    login_session['picture'] = user.picture

    flash("Now logged in as %s" % user.username)
    return redirect(url_for('main.index'))


@auth.route('/logout')
def logout():
    """Todo."""
    login_session.clear()
    return redirect(url_for('main.index'))


def getUserByMail(email):
    try:
        user = db_session.query(User).filter_by(email=email).one()
        return user
    except:
        return None