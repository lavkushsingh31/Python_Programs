# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 14:33:58 2026
@author: Luvkush
Title: Program to find the index positions of list elements using index method
"""
import array

user_input = input("Enter integer elements(comma seperated): ").split(',')
element_to_find = input("Enter the element to find: ")

try:
    user_input = list(map(int, user_input))
    element_to_find = int(element_to_find)
    
    indexes = []
    start = 0
    found = False
    
    while start <= len(user_input):
        try:
            found = user_input.index(element_to_find,start)
            indexes.append(found)
            start = found+1
        except ValueError:
            break
    print(f"Element found at index: {indexes}")
except Exception as e:
    print(f"Debug Info: The error was {type(e).__name__} - {e}")
    print(f"Error: Incorrect inputs received!")
        
        
