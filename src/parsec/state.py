#!/usr/bin/python3
# coding:utf-8
from parsec.error import ParsecEof

class BasicState(object):
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.begin = -1

    def next(self):
        if 0 <= self.index < len(self.data):
            re = self.data[self.index]
            self.index += 1
            return re
        else:
            raise ParsecEof(self)

    def begin(self):
        if self.begin == -1 :
            self.begin = self.index
        else:
            self.begin = min(self.begin,self.index)
        return self.index

    def commit (self, tran):
        if self.begin == tran:
            self.begin = -1

    def rollback (self, tran):
        if 0 <= self.index < len(self.data):
            self.index = tran
        if self.begin  ==tran:
            self.begin = -1


def min (elemnet1,element2):
    if elemnet1 < element2:
        return elemnet1
    return element2
        
