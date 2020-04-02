#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 13:48:25 2020

@author: justinhayes
"""

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inv, lst):
    print('Inventory')
    addToInventory(inv, lst)
    count = 0
    for k,v in inv.items():
        print(str(v) + ' ' + str(k))
        count = count + int(v)
    print('Total Number of Items ' + str(count))
    

def addToInventory(inv, lst):
    for l in lst:   
        for k in inv.keys():
            if k == l:
                inv[k] = inv[k] + 1
    return inv
    
displayInventory(inventory, dragonLoot)

        
    