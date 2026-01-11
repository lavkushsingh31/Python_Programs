# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 12:21:19 2026
@author: Luvkush
Title: Three methods of combining two dicts
"""
from ast import literal_eval

def func(a, b={}):
    
    # Method 1
    m1 = a | b
    m2 = {**a, **b}
    a = a.update(b)
    return m1, m2, a

input_dict1 = literal_eval(input('Enter first dict: '))
input_dict2 = literal_eval(input('Enter second (optional) dict: '))
result = "First input should be dictonary only!"
if isinstance(input_dict1, dict):
    if isinstance(input_dict2, dict):
        result = func(input_dict1, input_dict2)
    result = func(input_dict1)
    print(f"Concatenated Dict (method 1): {result[0]}")
    print(f"Concatenated Dict (method 2): {result[1]}")
    print(f"Concatenated Dict (method 3): {result[2]}")
else:
    print("First input should be dictonary only!")

