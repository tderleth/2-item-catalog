#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""User model."""

from app.server.database import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.server.database import db_session


class User(Base):
    """User Class."""

    __table_args__ = {'extend_existing': True}
    __tablename__ = 'users'
    email = Column(String(120), unique=True, nullable=False)
    gplus_id = Column(Integer, unique=True, nullable=False)
    id = Column(Integer, primary_key=True, nullable=False)
    lists = relationship("List", back_populates="user")
    picture = Column(Text)
    username = Column(String(80), nullable=False)

    def __init__(self, email, gplus_id, picture, username):
        """Create new model."""
        self.email = email
        self.gplus_id = gplus_id
        self.picture = picture
        self.username = username

    def is_authenticated(self):
        """Check if user is authenticated."""
        return True

    def __repr__(self):
        """Define custom __repr__ method."""
        return '<User %r>' % (self.username)

    def as_dict(self):
        """Convert row object to python dict."""
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


def getUserByMail(email):
    """Get User by mailt."""
    try:
        user = db_session.query(User).filter_by(email=email).one()
        return user
    except Exception:
        return None
