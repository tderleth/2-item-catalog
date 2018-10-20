#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""

from flask import Blueprint, render_template
catalog = Blueprint('catalog', __name__, template_folder='templates')


@catalog.route('/')
def index():
    """Call  test method."""
    return render_template('index.html', name='world')
