from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Root(object):
    pass


class Document(Base):
    __tablename__ = 'document'

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    content = Column(Text)
