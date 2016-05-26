import sqlalchemy

import morepath
import morepath_sqlalchemy
from morepath_sqlalchemy import App
from webtest import TestApp as Client

from morepath_sqlalchemy.app import Session
from morepath_sqlalchemy.model import Base


def setup_module(module):
    engine = sqlalchemy.create_engine('sqlite:///:memory:')
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)

    morepath.disable_implicit()
    morepath.scan(morepath_sqlalchemy)
    morepath.commit(App)


def test_documents():
    c = Client(App())

    collection_response = c.get('/documents')

    assert collection_response.json["documents"] == []
    assert "http://localhost/documents/add" in collection_response.json["add"]
    assert collection_response.json["previous"] is None
    assert collection_response.json["next"] is None


def test_add_submit():
    c = Client(App())

    response = c.post(
        '/documents/add_submit',
        {'title': 'My Title', 'content': 'My Content'}
    )

    assert response.body == b'<p>Awesome 1</p>'


def test_document():
    c = Client(App())

    response = c.get('/documents/1')
    new_document_response = {
        "id": 1,
        "title": "My Title",
        "content": "My Content",
        "link": "http://localhost/documents/1"
    }

    assert response.json == new_document_response


def test_previous_next():
    c = Client(App())

    c.post('/documents/add_submit', {'title': 'Two', 'content': 'Secundus'})

    response = c.get('/documents/?limit=1&offset=0')
    expected_documents = [{
        "id": 1,
        "title": "My Title",
        "content": "My Content",
        "link": "http://localhost/documents/1"
    }]

    assert response.json["documents"] == expected_documents
    assert "http://localhost/documents/add" in response.json["add"]
    assert response.json["previous"] is None
    assert "http://localhost/documents" in response.json["next"]
    assert "limit=1" in response.json["next"]
    assert "offset=1" in response.json["next"]

    response = c.get('/documents/?limit=1&offset=1')
    expected_documents = [{
        "id": 2,
        "title": "Two",
        "content": "Secundus",
        "link": "http://localhost/documents/2"
    }]

    assert response.json["documents"] == expected_documents
    assert "http://localhost/documents/add" in response.json["add"]
    assert "http://localhost/documents" in response.json["previous"]
    assert "limit=1" in response.json["previous"]
    assert "offset=0" in response.json["previous"]
    assert response.json["next"] is None


def test_add():
    c = Client(App())

    response = c.get('/documents/add')

    expected_response = b'''\
<html>
<body>
<form action="/documents/add_submit" method="POST">
title: <input type="text" name="title"><br>
content: <input type="text" name="content"><br>
<input type="submit" value="Add!"><br>
</form>
</body>
</html>
'''

    assert response.body == expected_response


def test_root():
    c = Client(App())

    c.get('/', status=302)
