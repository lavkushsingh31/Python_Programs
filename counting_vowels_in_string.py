# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 12:42:05 2025
@author: Luvkush
Title: Write a program that takes a string as input and counts the number of vowels 
(a, e, i, o, u) in the string.
"""

string = input("Enter a string or word: ")

vowel = 0
for char in string:
    if char in 'aeiou':
        vowel+=1

total_length = len(string.replace(' ',''))

print(f"Vowels: {vowel}\nConsonents: {total_length-vowel}")