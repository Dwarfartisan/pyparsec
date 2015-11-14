#!/usr/bin/python3
# coding:utf-8
from parsec.error import ParsecEof

class BasicState(object):
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.tran = -1

    def next(self):
        if 0 <= self.index < len(self.data):
            re = self.data[self.index]
            self.index += 1
            return re
        else:
            raise ParsecEof(self)

    def begin(self):
        if self.tran == -1 :
            self.tran = self.index

        return self.index

    def commit (self, tran):
        if self.begin == tran:
            self.begin = -1

    def rollback (self, tran):
        if 0 <= self.index < len(self.data):
            self.index = tran
        if self.begin  ==tran:
            self.begin = -1
