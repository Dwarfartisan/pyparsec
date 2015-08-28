#!/usr/bin/env python3
#coding:utf-8
from parsec.error import ParsecError
from parsec import Parsec

def string(s):
    @Parsec
    def call(st):
        for chr in s:
            c = st.next()
            if chr != c:
                raise ParsecError(st, "Expect '{0}' but got {1}".format(s, c))
        else:
            return s
    return call

@Parsec
def space(state):
    c = state.next()
    if c.isspace():
        return c
    raise ParsecError(st, "Expect a space but got {0}".format(c))
