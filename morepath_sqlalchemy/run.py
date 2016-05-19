import morepath
import sqlalchemy
from .session import Session
from .model import Base
from .app import App


def run():   # pragma: no cover
    engine = sqlalchemy.create_engine('sqlite:///morepath_sqlalchemy.db')
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    morepath.autoscan()
    morepath.run(App())
