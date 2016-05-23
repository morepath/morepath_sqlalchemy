import sqlalchemy
from sqlalchemy.orm import sessionmaker
from zope.sqlalchemy import register

from more.transaction import TransactionApp
from morepath.reify import reify
from morepath.request import Request

from .model import Base

engine = sqlalchemy.create_engine('sqlite:///morepath_sqlalchemy.db')
Session = sessionmaker()
register(Session)
Session.configure(bind=engine)
Base.metadata.create_all(engine)
Base.metadata.bind = engine


class DBSessionRequest(Request):

    @reify
    def db_session(self):
        return Session()


class App(TransactionApp):
    request_class = DBSessionRequest
