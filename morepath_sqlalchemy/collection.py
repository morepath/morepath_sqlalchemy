from .model import Document
from .main import Session

MAX_LIMIT = 20

class DocumentCollection(object):
    def __init__(self, offset, limit):
        self.offset = offset
        self.limit = min(limit, MAX_LIMIT)

    def query(self):
        return Session.query(Document).offset(self.offset).limit(self.limit)

    def add(self, title, content):
        session = Session()
        document = Document(title=title, content=content)
        session.add(document)
        session.flush()
        return document

    def previous(self):
        if self.offset == 0:
            return None
        new_offset = max(self.offset - self.limit, 0)
        return DocumentCollection(new_offset, self.limit)

    def next(self):
        count = Session.query(Document.id).count()
        new_offset = self.offset + self.limit
        if new_offset >= count:
            return None
        return DocumentCollection(new_offset, self.limit)

