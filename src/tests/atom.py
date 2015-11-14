#!/usr/bin/env python3
# coding:utf-8

import unittest
from parsec import *

simple = "It is a simple string."

class TestAtom(unittest.TestCase):
    def test_one(self):
        st = BasicState(simple)
        for i in range(len(simple)):
            idx = st.index
            re = one(st)
            self.assertEqual(re, st.data[idx])
        with self.assertRaises(Exception) as err:
            one(st)
        self.assertTrue(issubclass(type(err.exception), ParsecEof))

    def test_eof(self):
        st = BasicState(simple)
        for i in range(len(simple)):
            re = one(st)
        self.assertIsNone(eof(st))

    def test_eq(self):
        st = BasicState(simple)
        for i in range(len(simple)):
            c = st.data[st.index]
            next_parser = eq(c)
            re = next_parser(st)
            self.assertEqual(re, c)

    def test_ne(self):
        st = BasicState(simple)
        next_parser = ne("")
        for i in range(len(simple)):
            c = st.data[st.index]
            re = next_parser(st)
            self.assertEqual(re, c)
            next_parser = ne(c)

    def test_one_of(self):
        st = BasicState(simple)
        next_parser = oneOf(simple)
        for i in range(len(simple)):
            idx = st.index
            re = next_parser(st)
            self.assertEqual(re, st.data[idx])

    def test_none_of(self):
        st = BasicState(simple)
        n = noneOf("xyzcf")
        for i in range(1, len(simple)):
            idx = st.index
            re = n(st)
            self.assertEqual(re, st.data[idx])

    def test_pack(self):
        st = BasicState(simple)
        p = pack("z")
        for i in range(1, len(simple)):
            idx = st.index
            re = p(st)
            self.assertEqual("z", re)

    def test_fail(self):
        st = BasicState(simple)
        p = fail("z")
        with self.assertRaises(ParsecError):
            p(st)

if __name__ == '__main__':
    unittest.main()
