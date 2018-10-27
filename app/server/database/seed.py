#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""DB seed."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.sever.database import User

engine = create_engine('sqlite:///database.db')

DBSession = sessionmaker(bind=engine)
session = DBSession()

user = User(name="John Doe", email="john@doe.com",
            picture='https://via.placeholder.com/350x150')

session.add(user)
session.commit()

list = List(name="Hockey")

session.add(list)
session.commit()

item = Item(name="Stick", list=list)

session.add(item)
session.commit()

print "db seeded."
