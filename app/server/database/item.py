#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Item model."""

from app.server.database import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship


class Item(Base):
    """Item Class."""

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'items'
    description = Column(Text, nullable=False)
    id = Column(Integer, primary_key=True)
    list = relationship("List", back_populates="items")
    list_id = Column(Integer, ForeignKey('lists.id'))
    name = Column(String(80), nullable=False)

    def __init__(self, name, description, list_id):
        """Create new model."""
        self.name = name
        self.description = description
        self.list_id = list_id

    def __repr__(self):
        """Define custom __repr__ method."""
        return '<Item %r>' % (self.name)

    def as_dict(self):
        """Convert row object to python dict."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
