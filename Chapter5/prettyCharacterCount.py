#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:52:27 2020

@author: justinhayes
"""

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}   

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

