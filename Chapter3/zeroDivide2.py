#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:44:05 2020

@author: justinhayes
"""

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid Argument.')

# The reason print(spam(1)) is never executed is because once the execution 
# jumps to the code in the except clause, it does not return to the try 
# clause. Instead, it just continues moving down as normal.