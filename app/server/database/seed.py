#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Udacity Fullstack Developer nanodegree (Item catalg)."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.auth.models import User

engine = create_engine('sqlite:///database.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()

user = User(name="John Doe", email="john@doe.com",
            picture='https://via.placeholder.com/350x150')

session.add(user)
session.commit()

category = Category(name="Hockey")

session.add(category)
session.commit()

item = Item(name="Stick", category=category)

session.add(item)
session.commit()

print "db seeded."
