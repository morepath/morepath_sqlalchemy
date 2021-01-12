.. image:: https://github.com/morepath/morepath_sqlalchemy/workflows/CI/badge.svg?branch=master
   :target: https://github.com/morepath/morepath_sqlalchemy/actions?workflow=CI
   :alt: CI Status

.. image:: https://coveralls.io/repos/github/morepath/morepath_sqlalchemy/badge.svg?branch=master
    :target: https://coveralls.io/github/morepath/morepath_sqlalchemy?branch=master

.. image:: https://img.shields.io/pypi/v/morepath_sqlalchemy.svg
  :target: https://pypi.org/project/morepath_sqlalchemy/

.. image:: https://img.shields.io/pypi/pyversions/morepath_sqlalchemy.svg
  :target: https://pypi.org/project/morepath_sqlalchemy/


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
