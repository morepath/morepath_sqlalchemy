from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import register

Session = scoped_session(sessionmaker())
register(Session)
