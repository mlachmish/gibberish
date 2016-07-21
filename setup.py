#!/usr/bin/env python

from distutils.core import setup

setup(name='gibbrish',
      version='1.0.0',
      description="Generate '.strings' file with long gibberish strings in order to test if your app is ready for translation.",
      author='Matan Lachmish',
      author_email='matan.lachmish@gmail.com',
      url='https://github.com/mlachmish/gibberish',
      packages=[generator],
     )
