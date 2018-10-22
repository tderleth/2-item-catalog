#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Category views."""


from app.server.database.category import Category

from flask import Blueprint, render_template, jsonify, request

category = Blueprint("category", __name__, template_folder="templates")


@category.route('/api')
@category.route('/')
def index():
    """Get all categories."""
    categories = Category.query.all()
    if 'api/' in request.path:
        return jsonify(categories=[i.serialize for i in categories])
    else:
        return render_template('index.html', categories=categories)


@category.route('/<int:category_id>')
@category.route('/api/<int:category_id>')
def show(category_id):
    """Get single category via id."""
    category = Category.query.filter_by(id=category_id).first_or_404()
    if 'api/' in request.path:
        return jsonify(category=category.serialize)
    else:
        return render_template('index.html', category=category)
