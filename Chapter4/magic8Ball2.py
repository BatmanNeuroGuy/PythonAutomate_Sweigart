#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:01:00 2020

@author: justinhayes
"""

import random

messages = ['It is certain', 'It is decidedly so', 'Yes definitely',
'Reply hazy try again','Ask again later','Concentrate and ask again',
'My reply is no', 'Outlook not so good','Very doubtful']

def magic8(lst):
    input('Ask a question: \n')
    print(lst[random.randint(0, len(lst) - 1)])
    
magic8(messages)
