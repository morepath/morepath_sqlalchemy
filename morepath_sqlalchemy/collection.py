from .model import Document
from .main import Session

class DocumentCollection(object):
    def add(self, title, content):
        session = Session()
        document = Document(title=title, content=content)
        session.add(document)
        session.flush()
        return document
