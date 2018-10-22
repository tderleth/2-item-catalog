#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Category model."""

from sqlalchemy import Column, Integer, String
from app.server.database import Base


class Category(Base):
    __tablename__ = 'category'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)

    def __init__(self, name):

        self.name = name

    def __repr__(self):
        return '<Category %r>' % (self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}