from .main import app, Session
from .model import Document

@app.path(model=Document, path='documents/{id}',
          converters={'id': int})
def get_document(id):
    session = Session()
    return session.query(Document).filter(Document.id == id).first()
