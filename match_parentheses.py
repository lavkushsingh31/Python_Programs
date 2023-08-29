# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 18:18:06 2023
@author: Luvkush
"""

string = input("Enter the string having parenthesis: ").replace(" ", "")

forward_c = 0
backward_c = 0
temp = ""
print(f"Current input: {string}")
result_list = []

for char in string:
    if char == "(":
        forward_c = forward_c+1
        temp = temp+char
    if char == ")":
        backward_c = backward_c+1
        temp = temp+char
    if forward_c == backward_c:
        result_list.append(temp)
        temp = ""

print(result_list)
            