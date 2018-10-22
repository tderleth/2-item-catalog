#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""App entrypoint."""

from config import config
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from app.server.database import init_db

# instantiate extensions
toolbar = DebugToolbarExtension()


def create_app(config_name):
    """Register bleuprints, load extensions."""
    app = Flask(
        __name__,
        template_folder='../client/templates',
        static_folder='../client/static'
    )

    app.config.from_object(config[config_name])

    # set up extensions
    toolbar.init_app(app)
    init_db()

    # register blueprints
    from app.server.main.views import main
    app.register_blueprint(main)

    from app.server.auth.views import auth
    app.register_blueprint(auth, url_prefix="/auth")

    from app.server.category.views import category
    app.register_blueprint(category, url_prefix="/categories")

    return app
