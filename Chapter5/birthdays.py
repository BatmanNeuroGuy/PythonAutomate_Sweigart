#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:52:27 2020

@author: justinhayes
"""


birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name) # name is idx, returns value
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input() 
        birthdays[name] = bday # updates data base with idx = name, val = bday
        print('Birthday database updated.')