#!/usr/bin/env python3
# coding:utf-8

class Parsec(object):
    def __init__(self, parsec):
        self.parsec = parsec
    def __call__(self, st):
        return self.parsec(st)
    def bind(self, continuation):
        def bind(st):
            binder = continuation(self.parsec(st))
            return binder(st)
        return Parsec(bind)
    def then(self, p):
        def then(st):
            self.parsec(st)
            return p(st)
        return Parsec(then)
    def over(self, p):
        def over(st):
            re = self.parsec(st)
            p(st)
            return re
        return Parsec(over)
