#!/usr/bin/env python3
# coding:utf-8

import unittest
from parsec import *

simple = "It is a simple string."

class TestCombinator(unittest.TestCase):
    def test_many_0(self):
        st = BasicState(simple)
        p = many(one)
        re = p(st)
        data = "".join(re)
        self.assertEqual(data, simple)

    def test_many_1(self):
        st = BasicState(simple)
        p = many(eq("I"))
        re = p(st)
        data = "".join(re)
        self.assertEqual(data, "I")

    def test_many_2(self):
        st = BasicState(simple)
        p = many(eq("z"))
        re = p(st)
        data = "".join(re)
        self.assertEqual(data, "")

    def test_many0_1(self):
        st = BasicState(simple)
        p = many1(one)
        re = p(st)
        data = "".join(re)
        self.assertEqual(data, simple)

    def test_many1_1(self):
        st = BasicState(simple)
        p = many1(eq("I"))
        re = p(st)
        data = "".join(re)
        self.assertEqual(data, "I")

    def test_many1_2(self):
        st = BasicState(simple)
        p = many1(eq("z"))
        with self.assertRaises(ParsecError):
            p(st)

    def test_sep_0(self):
        st = BasicState(simple)
        p = sep(many1(ne(" ")), eq(" "),)
        re = p(st)
        data = ["".join(item) for item in re]
        self.assertEqual(data, simple.split(" "))

    def test_sep1_0(self):
        st = BasicState(simple)
        p = sep1(many1(ne(" ")), eq(" "))
        re = p(st)
        data = ["".join(item) for item in re]
        self.assertEqual(data, simple.split(" "))

if __name__ == '__main__':
    unittest.main()
