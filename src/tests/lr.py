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
    re = many1(digit)(st)
    return int("".join(re))

def mulN(x):
    @Parsec
    def func(st):
        y = eq("*").then(N)(st)
        return x*y
    return func

def addF(x):
    @Parsec
    def func(st):
        y = eq("+").then(F)(st)
        return x+y
    return func

@Parsec
def N(st):
    return choice(attempt(integer), between(eq('('), eq(')'), T))(st)

@Parsec
def F(st):
    # x = choice(attempt(N), F)(st)
    # eq('*')(st)
    # y = N(st)
    # return x * y
    return choice(attempt(N), F).bind(mulN)(st)

@Parsec
def T(st):
    # x = choices(attempt(F), T)(st)
    # eq('+')(st)
    # y = F(st)
    # return x + y
    return choice(attempt(F), T).bind(addF)(st)

if __name__ == '__main__':
    st = BasicState(input)
    re = T(st)
    print(re)
