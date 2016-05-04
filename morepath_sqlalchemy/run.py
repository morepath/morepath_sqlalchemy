import morepath
import sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import register
from .model import Base
from .app import App


Session = scoped_session(sessionmaker())
register(Session)


def run():   # pragma: no cover
    engine = sqlalchemy.create_engine('sqlite:///morepath_sqlalchemy.db')
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    morepath.autoscan()
    morepath.run(App())
