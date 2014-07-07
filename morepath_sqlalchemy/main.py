import morepath
import sqlalchemy
from more.transaction import transaction_app
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import register
from .model import Base

Session = scoped_session(sessionmaker())
register(Session)

class app(transaction_app):
    pass

def main():
    engine = sqlalchemy.create_engine('sqlite:///morepath_sqlalchemy.db')
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine

    morepath.autosetup()
    morepath.run(app())
