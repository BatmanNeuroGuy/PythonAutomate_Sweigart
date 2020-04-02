#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:01:00 2020

@author: justinhayes
"""
def eggs(someParameter):
    someParameter.append('Hello')
    
spam = [1, 2, 3]
eggs(spam)
print(spam)
