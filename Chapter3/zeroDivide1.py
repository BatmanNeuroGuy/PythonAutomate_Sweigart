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

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
