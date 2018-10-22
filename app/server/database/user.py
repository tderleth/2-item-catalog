#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""User model."""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from app.server.database import Base


class User(Base):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    email = Column(String(120), unique=True, nullable=False)
    gplus_id = Column(Integer, unique=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    picture = Column(Text)
    username = Column(String(80), nullable=False)

    def __init__(self, email, gplus_id, picture, username):
        self.email = email
        self.gplus_id = gplus_id
        self.picture = picture
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User %r>' % (self.username)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
