# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 23:19:34 2026
@author: Luvkush
Title: Take a list of strings and sort them by the number of vowels in each string
"""

input_list = ['This', 'is', 'test', 'aeiou','string']

def count_vowels(string):
    return sum(1 for char in string.lower() if char in 'aeiou')

sorted_list = sorted(input_list, key = count_vowels)
print(sorted_list)


            
        