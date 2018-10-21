import os
import json


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = False
    PORT = 5000
    HOST = "0.0.0.0"
    SQLALCHEMY_ECHO = True


class Development(Config):
    DEBUG = True
    ENV = 'Development'
    HOST = "0.0.0.0"
    PORT = 5000
    RELOAD = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CLIENT_ID = json.loads(
        open('app/server/client_secret.json', 'r').read())['web']['client_id']


class Testing(Config):
    TESTING = True


config = {
    'development': Development,
    'testing': Testing,
    'default': Development
}
