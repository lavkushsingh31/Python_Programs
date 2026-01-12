# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 23:39:40 2026
@author: Luvkush
Title: Take a list of strings and sort them by the number of vowels in each string and if there is a tie, use alphabetical order
"""

input_list = ['This', 'test', 'is', 'tset', 'aeiou','string']

def count_vowels(string):
    return sum(1 for char in string.lower() if char in 'aeiou')

# The key returns a TUPLE: (vowel_count, word_itself)
sorted_list = sorted(input_list, key=lambda x: (count_vowels(x), x.lower()))

print(sorted_list)