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
    assert collection_response.json == {
        "documents": [],
        "add": "http://localhost/documents/add?limit=10&offset=0",
        "previous": None,
        "next": None
    }


def test_add_submit():
    c = Client(App())

    response = c.post(
        '/documents/add_submit',
        {'title': 'My Title', 'content': 'My Content'}
    )

    assert response.body == '<p>Awesome 1</p>'


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
    new_document_response = {
        "documents": [{
            "id": 1,
            "title": "My Title",
            "content": "My Content",
            "link": "http://localhost/documents/1"
        }],
        "add": "http://localhost/documents/add?limit=1&offset=0",
        "previous": None,
        "next": "http://localhost/documents?limit=1&offset=1"
    }

    assert response.json == new_document_response

    response = c.get('/documents/?limit=1&offset=1')
    new_document_response = {
        "documents": [{
            "id": 2,
            "title": "Two",
            "content": "Secundus",
            "link": "http://localhost/documents/2"
        }],
        "add": "http://localhost/documents/add?limit=1&offset=1",
        "previous": "http://localhost/documents?limit=1&offset=0",
        "next": None
    }

    assert response.json == new_document_response


def test_add():
    c = Client(App())

    response = c.get('/documents/add')

    expected = '''\
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

    assert response.body == expected


def test_root():
    c = Client(App())

    c.get('/', status=302)
