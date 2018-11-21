#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Configuration for application."""

import json
import os


class Config(object):
    """Basic Config class cotaining settings that are valid for all configs."""

    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = True
    PORT = 5000
    HOST = "0.0.0.0"
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False


class Development(Config):
    """Dev Config class."""

    CLIENT_ID = json.loads(
        open('app/server/secret.json', 'r').read())['web']['client_id']
    ENV = 'Development'
    RELOAD = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(Config):
    """Prod Config class."""

    CLIENT_ID = json.loads(
        open('app/server/secret.json', 'r').read())['web']['client_id']
    ENV = 'Production'
    RELOAD = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
    'default': Development,
    'development': Development,
    'production': Production
}
