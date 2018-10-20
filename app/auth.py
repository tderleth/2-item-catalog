#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""

from flask import Blueprint, render_template
from flask import session as login_session
import random
import string


auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route('/login')
def login():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('auth/login.html')
