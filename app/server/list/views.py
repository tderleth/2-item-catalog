#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""List views."""

from app.server.auth import login_required
from app.server.database import db_session
from app.server.database.list import List
from flask import session as login_session


from flask import Blueprint, render_template, redirect
from flask import jsonify, request, flash, url_for

list = Blueprint("list", __name__, template_folder="templates")


@list.route('/json')
@list.route('/')
def index():
    """Get all lists."""
    data = List.query.all()
    if '/json' in request.path:
        lists = []
        for list in data:
            lists.append(list.as_dict())
        return jsonify(lists)
    else:
        return render_template('list/index.html', lists=data)


@list.route('/<int:list_id>/json')
@list.route('/<int:list_id>')
def show(list_id):
    """Get single list via id."""
    data = db_session.query(List).filter(List.id == list_id).first()
    if '/json' in request.path:
        return jsonify(data.as_dict())
    else:
        return render_template('list/show.html', list=data)


@list.route('/create', methods=['POST'])
@login_required
def create():
    """Store new list."""
    name = request.form.get("name")
    if not name:
        flash("Please provide a name")
        return redirect(url_for('list.index'))
    list = List(name=name, user_id=login_session['user_id'])
    db_session.add(list)
    db_session.commit()
    flash("New list %s created" % name)
    return redirect(url_for('list.index'))


@list.route('/<int:list_id>/destroy', methods=['GET'])
@login_required
def destory(list_id):
    """Delete list."""
    list = db_session.query(List).filter(List.id == list_id).first()
    if(list.user_id != login_session['user_id']):
        flash("This list does not belong to your account")
        return redirect(url_for('list.index'))
    db_session.delete(list)
    db_session.commit()
    flash("List %s destroyed" % list.name)
    return redirect(url_for('list.index'))


@list.route('/<int:list_id>/update', methods=['POST'])
@login_required
def update(list_id):
    """Update list."""
    list = db_session.query(List).filter(List.id == list_id).first()
    if(list.user_id != login_session['user_id']):
        flash("This list does not belong to your account")
        return redirect(url_for('list.show', list_id=list_id))
    name = request.form.get("name")
    if not name:
        flash("Please provide a name")
        return redirect(url_for('list.show', list_id=list_id))
    list.name = name
    db_session.add(list)
    db_session.commit()
    flash("List %s was updated" % list.name)
    return redirect(url_for('list.show', list_id=list_id))
