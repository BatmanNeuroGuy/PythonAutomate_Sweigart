#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:01:00 2020

@author: justinhayes
"""

myPets = ['Zophie', 'Pooka', 'Fat-tail']

print('Enter a pet name:')
name = input()

if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')