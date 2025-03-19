# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 18:41:54 2025
@author: Luvkush
Title: count the number of odd and even numbers in the list. 
"""

numbers = [ 
            [2, 5, 11, 20, 8],
            [9, 4, 15, 28, 17],
            [1, 6, 21, 18, 3],
            [10, 13, 25, 33, 30],
            [14, 7, 16, 19, 22] 
         ]

odds = 0
evens = 0

for lst in numbers:
    for item in lst:
        if item%2 == 0:
            evens+=1
        else:
            odds+=1
            

print(f"Odds count: {odds}\nEvens count: {evens}")