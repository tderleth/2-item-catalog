#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""List model."""

from app.server.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class List(Base):
    """List Class."""

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'lists'
    id = Column(Integer, primary_key=True)
    items = relationship("Item", cascade="all,delete", back_populates="list")
    name = Column(String(80), nullable=False)
    user = relationship("User", back_populates="lists")
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        """Define custom __repr__ method."""
        return '<List %r>' % (self.name)

    def as_dict(self):
        """Convert row object to python dict."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
