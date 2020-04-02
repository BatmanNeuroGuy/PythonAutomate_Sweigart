#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:01:00 2020

@author: justinhayes
"""
# loops through grid printing grid[0][0]...grid[1][0]...grid[8][0]
# grid[0][1]...grid[8][1]...grid[0][5]...grid[8][5]
# NOTE: the end = '' keyword argument in the nested print statement which 
# tells the program to print each value adjacent to previous value
# Last print statement tells is outside the nested for loop, tells the program
# to move to the next line

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

len_lst = len(grid)
len_sub = len(grid[0])

for i in range(len_sub):  # length of each nested list = 6
    for x in range(len_lst): # number of nested lists (items in list) = 9
        print(str(grid[x][i]), end = '') 
    print()
    
    

            

        
    
            
