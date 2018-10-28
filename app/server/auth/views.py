#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Auth and User views."""

from app.server.database import db_session
from app.server.database.user import User, getUserByMail
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask import session as login_session
from google.auth.transport import requests
from google.oauth2 import id_token


auth = Blueprint("auth", __name__, template_folder="templates")


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
        user = User(username=idinfo['given_name']
                    + " " + idinfo['family_name'],
                    email=idinfo['email'],
                    picture=idinfo['picture'],
                    gplus_id=idinfo['sub'])
        db_session.add(user)
        db_session.commit()

    login_session['auth'] = True
    login_session['gplus_id'] = user.gplus_id
    login_session['picture'] = user.picture
    login_session['user_id'] = user.id
    login_session['username'] = user.username

    flash("Now logged in as %s" % user.username)
    return redirect(url_for('main.index'))


@auth.route('/logout')
def logout():
    """Todo."""
    login_session.clear()
    return redirect(url_for('main.index'))
