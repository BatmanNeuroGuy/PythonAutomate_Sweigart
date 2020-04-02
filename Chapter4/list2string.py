#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:01:00 2020

@author: justinhayes
"""

spam = ['apples', 'bananas', 'tofu', 'cats']
var = ''

def conv2str(lst, new_var):
    for i in range(len(lst)):
        if i < len(lst) - 1:
            new_var = new_var + str(lst[i]) + ', '
        else:
            new_var = new_var + 'and ' + str(lst[i])
    print(new_var)

conv2str(spam, var)
