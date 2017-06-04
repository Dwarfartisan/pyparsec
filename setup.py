#!/usr/bin/env python

from setuptools import setup

setup(name="pyparsec",
      version="0.5.1",
      description="Parsec From Haskell Python 3 Portable",
      long_description="""
PyParsec is a Haskell combinator library, PyParsec is a parsec library for python 3+
""",
      author="marsliu",
      author_email="mars.liu@outlook.com",
      url="https://github.com/Dwarfartisan/pyparsec",
      license="MIT",
      packages=["parsec", "test"],
      package_dir={
          "parsec": "src/parsec",
          "test": "src/tests"
      },
      classifiers=[
         "Topic :: Utilities",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3 :: Only",
         "License :: OSI Approved :: MIT License"
      ]
)
