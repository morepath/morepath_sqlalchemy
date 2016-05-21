import sqlalchemy

import morepath

from .app import App
from .model import Base
from .dbsession import Session


def run():   # pragma: no cover
    engine = sqlalchemy.create_engine('sqlite:///morepath_sqlalchemy.db')
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    morepath.autoscan()
    morepath.run(App())
