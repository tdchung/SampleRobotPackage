#!/usr/bin/env python

from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError as error:
    from distutils.core import setup

VERSION = "1.0.0"

DESCRIPTION = """
Just a sample python package.
"""[1:-1]


CLASSIFIERS = """
Development Status :: N/A
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(name         = 'sample-python-package',
      version      = VERSION,
      description  = 'sample python package',
      long_description = DESCRIPTION,
      author       = 'Tran Duc Chung',
      author_email = 'tdchung.9@gmail.com',
      maintainer   = 'N/A',
      maintainer_email = 'N/A',
      url          = 'http://github.com/',
      license      = 'MIT',
      keywords     = '',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'' : 'src'},
      packages     = [''],
      install_requires=[
            'robotframework',
      ],
      extras_require={
            # TODO: 'test': ['flask']
            None
      },
)
