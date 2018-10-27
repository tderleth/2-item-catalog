#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""List model."""

from sqlalchemy import Column, Integer, String, ForeignKey
from app.server.database import Base
from sqlalchemy.orm import relationship


class List(Base):
    __tablename__ = 'lists'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="lists")
    items = relationship("Item", back_populates="list")

    def __init__(self, name):

        self.name = name

    def __repr__(self):
        return '<List %r>' % (self.name)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
