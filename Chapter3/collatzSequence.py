#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:44:05 2020

@author: justinhayes
"""

def collatz(number):
    
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


n = input('Enter a number: \n')
x = 0

try: 
    while n != 1:       # returned value replaces n until n = 1 (recursion)
        n = collatz(int(n))
        x += 1
        
    print('\nIt took ' + str(x) + ' cyles to reach 1!')
    
except:
    print('\nPlease enter an integer.')
    
