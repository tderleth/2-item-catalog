#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""


from flask import Blueprint

auth = Blueprint("auth", __name__, template_folder="templates")

from app.server.auth import views
