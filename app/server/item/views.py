#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Item views."""

from app.server.auth import login_required
from app.server.database import db_session
from app.server.database.item import Item
from app.server.database.list import List
from flask import session as login_session


from flask import Blueprint, render_template, redirect
from flask import jsonify, request, flash, url_for

item = Blueprint("item", __name__, template_folder="templates")


@item.route('/json')
def index(list_id):
    """Get all lists."""
    data = db_session.query(Item).filter(Item.list_id == list_id).all()
    items = []
    for item in data:
        items.append(item.as_dict())
    return jsonify(items)


@item.route('/<int:item_id>/json')
@item.route('/<int:item_id>')
def show(list_id, item_id):
    """Get single item via id."""
    list = db_session.query(List).filter(List.id == list_id).first()
    data = db_session.query(Item).filter(Item.id == item_id).first()
    if '/json' in request.path:
        return jsonify(data.as_dict())
    else:
        return render_template('item/show.html', item=data, list=list)


@item.route('/create', methods=['POST'])
@login_required
def create(list_id):
    """Store new item."""
    list = db_session.query(List).filter(List.id == list_id).first()
    if(list.user_id != login_session['user_id']):
        flash("This list does not belong to your account")
        return redirect(url_for('list.show', list_id=list_id))
    name = request.form.get("name")
    if not name:
        flash("Please provide a name")
        return redirect(url_for('list.show', list_id=list_id))
    description = request.form.get("description")
    if not description:
        flash("Please provide a description")
        return redirect(url_for('list.show', list_id=list_id))
    item = Item(name=name, description=description, list_id=list_id)
    db_session.add(item)
    db_session.commit()
    flash("New item %s created" % name)
    return redirect(url_for('list.show', list_id=list_id))


@item.route('/<int:item_id>/destroy', methods=['GET'])
@login_required
def destory(list_id, item_id):
    """Delete item."""
    list = db_session.query(List).filter(List.id == list_id).first()
    if(list.user_id != login_session['user_id']):
        flash("This list does not belong to your account")
        return redirect(url_for('list.show', list_id=list_id))
    item = db_session.query(Item).filter(Item.id == item_id).first()
    db_session.delete(item)
    db_session.commit()
    flash("Item %s destroyed" % item.name)
    return redirect(url_for('list.show', list_id=list_id))


@item.route('/<int:item_id>/update', methods=['POST'])
@login_required
def update(list_id, item_id):
    """Update item."""
    list = db_session.query(List).filter(List.id == list_id).first()
    if(list.user_id != login_session['user_id']):
        flash("This list does not belong to your account")
        return redirect(url_for('list.show', list_id=list_id))
    item = db_session.query(Item).filter(Item.id == item_id).first()
    name = request.form.get("name")
    if not name:
        flash("Please provide a name")
        return redirect(url_for('item.show', list_id=list_id, item_id=item.id))
    description = request.form.get("description")
    if not description:
        flash("Please provide a description")
        return redirect(url_for('item.show', list_id=list_id, item_id=item.id))
    item.name = name
    item.description = description
    item.list_id = list_id
    db_session.add(item)
    db_session.commit()
    flash("Item %s was updated" % item.name)
    return redirect(url_for('item.show', list_id=list_id, item_id=item.id))
