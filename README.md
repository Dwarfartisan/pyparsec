# PyParsec

PyParsec is a Haskell combinator library, PyParsec is a parsec library for python 3+

## Installation

```
pip install pyparsec 
```

## Usage

Just like this:

```
>>> import parsec
>>> simple = "It is a simple string."
>>> st = BasicState(simple)
>>> p = many(eq("I"))
>>> p(st)
['I']
```

