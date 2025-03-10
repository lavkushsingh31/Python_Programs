# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 22:05:20 2025
@author: Luvkush
Title: Check if a word starts with vowel or consonant
"""

input_str = input("Enter a string: ").lower()

vowels = ['a','e','i','o','u']

if input_str[0] in vowels:
    print(f"This '{input_str}' word starts with vowel.")
else:
    print(f"This '{input_str}' word starts with consonant.")