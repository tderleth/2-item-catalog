#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""Database package."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgresql+psycopg2://catalog:secret@localhost/catalog', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    """Initialize database."""
    
    from app.server.database import user
    from app.server.database import list
    from app.server.database import item

    Base.metadata.create_all(bind=engine)
