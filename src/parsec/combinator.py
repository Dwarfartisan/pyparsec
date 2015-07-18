#!/usr/bin/env python3
# coding:utf-8

from parsec import Parsec
from atom import pack

def attempt(p):
    @Parsec
    def call(state):
        prev = state.index
        try:
            return p(state)
        except:
            state.index=prev
            raise
    return call

class Either(Parsec):
    def __init__(self, x, y):
        def call(state):
            prev = state.index
            try:
                return x(state)
            except:
                if self.index == prev:
                    return y(state)
                else:
                    raise
        Parsec.__init__(call)
    def Or(self, continuation):
        return Either(self, continuation)

def choice(x, y):
    @Parsec
    def call(st):
        prev = st.index
        try:
            return x(st)
        except:
            if st.index == prev:
                return y(st)
            else:
                raise
    return call

def choices(*psc):
    if len(psc)<2:
        raise ParsecError(-1, "choices need more args than one.")
    @Parsec
    def call(st):
        for p in psc[-1:]:
            prev = st.index
            try:
                return p(st)
            except:
                if self.index != prev:
                    raise
        else:
            return psc[-1](st)
    return call

def many(p):
    return choice(attempt(many1(p)), pack([]))

def many1(p):
    @Parsec
    def call(st):
        re = []
        re.append(p(st))
        try:
            while True:
                re.append(attempt(p)(st))
        except Exception as err:
            pass
        finally:
            return re
    return call

def sep(s, p):
    return choice(attempt(sep1(s, p)), pack([]))

def sep1(s, p):
    @Parsec
    def call(state):
        re = []
        re.append(p(state))
        try:
            while True:
                re.append(attempt(s.then(p))(state))
        except:
            pass
        finally:
            return re
    return call

def manyTail(p, t):
    return many(p).over(t)

def many1Tail(p):
    return many1.over(t)

def sepTail(s, p, t):
    return sep(s, p).over(t)

def sep1Tail(s, p, t):
    return sep1(s, p).over(t)
