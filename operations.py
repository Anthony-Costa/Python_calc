#!/usr/bin/env/ python3

from math import *
import operator

def add(x, y):
    ops = {"+": operator.add}
    print (ops["+"](x.get(), y.get()))

def substract(x, y):
    ops = {"-": operator.sub}
    print (ops["-"](x.get(), y.get()))

def multiply(x, y):
    ops = {"*": operator.mul}
    print (ops["*"](x.get(), y.get()))

def divide(x, y):
    ops = {"/": operator.truediv}
    print (ops["/"](x.get(), y.get()))

def percent(x):
    ops = {"/": operator.truediv}
    print = (ops["/"](x.get(), 100))

def square(x):
    ops = {"x2": operator.xor}
    print (ops["x2"](x.get()))

