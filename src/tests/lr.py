#!/usr/bin/env python3
# coding:utf-8

# N = [0..9] | (T); F = N | F * N; T = F | T + F; P = T$;
# 输入文本是"1 * 2 + 3 * (4 + 5)
# 因为parsec不支持左递归，这个脚本一定会死循环，所以不要直接执行

from parsec import *
import string

input = "1*2+3*(4+5)"

digit = oneOf(string.digits)

@Parsec
def integer(st):
    re = many1(st)
    return int(re)

def mulN(x):
    y = one("*").then(N)(st)
    return x*y

def addT(x):
    y = one("+").then(T)(st)
    return x+y

@Parsec
def N(st):
    return choice(integer, T)(st)

@Parsec
def F(st):
    return choice(N, F.bind(mulN))(st)

@Parsec
def T(st):
    return choice(F, T.bind(addT))(st)

if __name__ == '__main__':
    st = BasicState(input)
    re = T(st)
    print(re)
