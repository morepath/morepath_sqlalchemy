SQLAlchemy integration for Morepath
===================================

Demonstrate SQLAlchemy integration with Morepath through more.transaction.

See the `more.transaction documentation`_ to learn more about what is going
on.

.. _`more.transaction documentation`: https://github.com/morepath/more.transaction

Installation
------------

You can use pip in a virtual env::

  $ virtualenv env
  $ source env/bin/activate
  $ env/bin/pip install -e .

Then to run the web server::

  $ env/bin/morepath_sqlalchemy

You can now access the application through http://localhost:5000
