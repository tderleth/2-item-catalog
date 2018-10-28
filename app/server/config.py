#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Entrypoint for application."""

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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    """Dev Config class."""

    TESTING = True


config = {
    'development': Development,
    'testing': Testing,
    'default': Development
}
