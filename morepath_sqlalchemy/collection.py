from .model import Document

MAX_LIMIT = 20


class DocumentCollection(object):
    def __init__(self, request, offset, limit):
        self.db_session = request.db_session
        self.offset = offset
        self.limit = min(limit, MAX_LIMIT)

    def query(self):
        return self.db_session.query(Document).offset(self.offset) \
            .limit(self.limit)

    def add(self, title, content):
        session = self.db_session
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
        count = self.db_session.query(Document.id).count()
        new_offset = self.offset + self.limit
        if new_offset >= count:
            return None
        return DocumentCollection(new_offset, self.limit)
