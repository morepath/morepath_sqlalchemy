Morepath SQLAlchemy Demo
========================

Show how to create a server web application with Morepath that integrates
a database based on SQLAlchemy.
It uses the more.transaction plugin.

See also more.transaction on Github:

https://github.com/morepath/more.transaction

Installation
------------

You can use pip in a virtual env::

  $ virtualenv env
  $ source env/bin/activate
  $ env/bin/pip install -e .

Then to run the web server::

  $ env/bin/morepath_sqlalchemy

You can now access the application through http://localhost:5000
