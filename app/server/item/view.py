#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""


from flask import render_template, jsonify, request
from app.server.category import blueprint
from app.server.database import Category


@blueprint.route('/')
@blueprint.route('/items')
@blueprint.route('/api/items')
def index():
    """Get all items."""
    items = Category.query().all()
    if 'api/' in request.path:
        return jsonify(items=[i.serialize for i in items])
    else:
        return render_template('index.html', items=items)


@blueprint.route('/items/<int:category_id>')
@blueprint.route('/api/items/<int:category_id>')
def show(category_id):
    """Get single category via id."""
    category = Category.query.filter_by(id=category_id).one()
    if 'api/' in request.path:
        return jsonify(category=category.serialize)
    else:
        return render_template('index.html', category=category)
