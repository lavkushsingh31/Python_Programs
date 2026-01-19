# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 11:41:21 2026
@author: Luvkush
Title: Program to find the index positions of array elements
"""

import array

user_input = input("Enter integer elements(comma seperated): ").split(',')
element_to_find = input("Enter the element to find: ")

try:
    # converting the user input to list of integers, and element_to_find as interger
    user_input = list(map(int, user_input))
    user_input = array.array('i', user_input)
    element_to_find = int(element_to_find)
    
    # getting indexes of the element to find
    found_at_index = [ i for i, e in enumerate(user_input) if e == element_to_find]
    
    print(f"Element found at index: {found_at_index}")
except ValueError:
    print("Error: Inputs are incorrect")

    
