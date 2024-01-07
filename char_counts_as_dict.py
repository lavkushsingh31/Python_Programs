# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 21:05:41 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

strng = input().lower()

count = dict()

for char in strng:
    if char not in count:
        count[char] = strng.count(char)

print(count)