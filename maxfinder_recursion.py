# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 15:19:41 2023
@author: Luvkush

"""

# Write your code here

#a = int(input())
#b = int(input())
#c = int(input())

lst = [1,0,-3,200,34]

def max_finder(lst):

    if len(lst)==0:
        #print("List has no elements here")
        return -99999999
    else:
        max_num = lst[0]
        
        if max_num > max_finder(lst[1:]):
            #print(f"Current Max: {max_num}")
            return max_num
        else:
            #print("Else Executed")
            return max_finder(lst[1:])
    
        
print(max_finder(lst))
