#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:44:05 2020

@author: justinhayes
"""


def spam():
    global eggs
    eggs = 'spam' # this is the global
    
def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global
    
eggs = 42 # this is the global
spam()
print(eggs)
    print(eggs) # this is the global
    
    eggs = 42 # this is the global
    spam()
     print(eggs)