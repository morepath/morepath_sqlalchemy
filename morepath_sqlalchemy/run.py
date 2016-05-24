import sqlalchemy

import morepath

from .app import App, Session
from .model import Base


def run():   # pragma: no cover
    engine = sqlalchemy.create_engine('sqlite:///morepath_sqlalchemy.db')
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)

    morepath.autoscan()
    morepath.run(App())
