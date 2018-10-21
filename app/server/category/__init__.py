#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""


from flask import Blueprint

category = Blueprint("category", __name__, template_folder="templates")

from app.server.category import views
