#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""

from flask import current_app
from app.server.auth import auth
from flask import Blueprint, Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import make_response
from flask import session as login_session
from google.auth.transport import requests
from google.oauth2 import id_token
import httplib2
import json
import random
import string
from app.server.database import db_session
from app.server.database.user import User


@auth.route("/<username>")
def show(username):
    u = User.query.filter_by(username=username).first_or_404()
    return "Hello, {}!".format(u.username)


@auth.route('/login')
def showLogin():
    return render_template('auth/login.html')


@auth.route('/google-tokensignin', methods=['POST'])
def google_tokensignin():

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

    print user

    if (user is None):
        user = User(username=idinfo['given_name'],
                    email=idinfo['email'], picture=idinfo['picture'], gplus_id=idinfo['sub'])
        db_session.add(user)
        db_session.commit()

    login_session['gplus_id'] = user.gplus_id
    login_session['username'] = user.username
    login_session['picture'] = user.picture

    flash("Now logged in as %s" % user.username)
    return redirect(url_for('main.index'))


@auth.route('/logout')
def logout():
    login_session.clear()
    return redirect(url_for('main.index'))


def getUserByMail(email):
    try:
        user = db_session.query(User).filter_by(email=email).one()
        return user
    except:
        return None
