import os
from setuptools import setup, find_packages

setup(name='morepath_sqlalchemy',
      version = '0.1dev',
      description="Morepath SQLAlchemy Demo",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'morepath',
        'transaction',
        'zope.sqlalchemy >= 0.7.4',
        'sqlalchemy >= 0.9',
        ],
      entry_points= {
        'console_scripts': [
            'morepath_sqlalchemy = morepath_sqlalchemy.main:main',
            ]
        },
      )
