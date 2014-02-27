from .model import Document
from .main import app
from .collection import DocumentCollection


@app.json(model=Document)
def document_default(self, request):
    return {'id': self.id,
            'title': self.title,
            'content': self.content}


@app.html(model=DocumentCollection)
def document_collection_default(self, request):
    return '''\
<html>
<body>
<form action="/documents/add" method="POST">
title: <input type="text" name="title"><br>
content: <input type="text" name="content"><br>
<input type="submit" value="Add!"><br>
</form>
</body>
</html>
'''


@app.html(model=DocumentCollection, name='add', request_method='POST')
def document_collection_add(self, request):
    title = request.form.get('title')
    content = request.form.get('content')
    document = self.add(title=title, content=content)
    return "<p>Awesome %s</p>" % document.id
