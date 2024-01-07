# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 06:10:24 2023
@author: Luvkush
"""

string = input()

result = {}

for char in string:
    if char in result.keys():
        result[char] += 1
    else:
        result[char] = 1

print(result)