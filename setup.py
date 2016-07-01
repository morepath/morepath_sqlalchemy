# -*- coding: utf-8 -*-

import io

from setuptools import find_packages, setup

name = "morepath_sqlalchemy"
description = (
    "Morepath SQLAlchemy Demo"
)
long_description = (
    io.open('README.rst', encoding='utf-8').read() + '\n\n' +
    io.open('CHANGES.rst', encoding='utf-8').read())
version = '0.1'

setup(
    name=name,
    version=version,
    description=description,
    long_description=long_description,
    author='Morepath developers',
    author_email='morepath@googlegroups.com',
    license="BSD",
    url="https://github.com/morepath/morepath_sqlalchemy",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'morepath>=0.14',
        'more.transaction',
        'zope.sqlalchemy >= 0.7.4',
        'sqlalchemy >= 0.9',
    ],
    extras_require=dict(
        test=[
            'pytest',
            'pytest-cov',
            'webtest',
        ],
    ),
    entry_points={
        'console_scripts': [
            'morepath_sqlalchemy = morepath_sqlalchemy.run:run',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
