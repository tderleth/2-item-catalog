#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Entrypoint for application."""

import sys
sys.path.insert(0, '/var/www/html')

from app.server import create_app
application = create_app('production')
