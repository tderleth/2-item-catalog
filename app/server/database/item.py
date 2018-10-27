#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Item model."""

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.server.database import Base


class Item(Base):
    __tablename__ = 'items'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    description = Column(Text, nullable=False)
    list_id = Column(Integer, ForeignKey('lists.id'))
    list = relationship("User", back_populates="list")

    def __init__(self, name, description, list_id):

        self.name = name
        self.description = description
        self.list_id = list_id

    def __repr__(self):
        return '<Item %r>' % (self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
