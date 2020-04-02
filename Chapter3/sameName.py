#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:44:05 2020

@author: justinhayes
"""


def spam():
    eggs = 'spam local'
    print (eggs)     # prints 'spam local'
    
def bacon():
    eggs = 'bacon local'
    print(eggs)   # prints 'bacon local'
    spam()
    print(eggs)   # prings 'bacon local'
    
eggs = 'global'
bacon()
print(eggs)   # prints 'global'