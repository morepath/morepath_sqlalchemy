from .model import Document
from .main import app

@app.json(model=Document)
def document_default(self, request):
    return {'id': self.id,
            'title': self.title,
            'content': self.content}
