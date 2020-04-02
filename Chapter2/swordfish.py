#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:56:07 2020

@author: justinhayes
"""


while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe.  What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')