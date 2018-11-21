#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Entrypoint for application."""

import sys
sys.path.insert(0, '/var/www/html')

from app.server import create_app


def run(app=None):
    """Run application, pass values for host, port and debug."""
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])

if __name__ == '__main__':
    app = create_app('development')
    run(app)
