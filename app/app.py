#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""


from flask import Flask
from catalog import catalog
from auth import auth

app = Flask(__name__)

app.register_blueprint(catalog)
app.register_blueprint(auth)

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
