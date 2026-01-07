# -*- coding: utf-8 -*-
"""
Created on Tue Jan  6 12:52:11 2026
@author: Luvkush
Title: Program to find the index of all occurances of a character in a string
"""

string = input("Enter a string value: ").strip().lower()
char_to_find = input("Enter the character you wish to find: ").strip().lower()

result = []
for i, char in enumerate(string):
    if char == char_to_find:
        result.append(i)

print(f"Index positions: {result}") 