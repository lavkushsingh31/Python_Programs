# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 18:19:49 2026
@author: Luvkush
Title: Define a function that takes a variable number of keyword arguments and returns a dictionary containing only those key-value pairs where the value is an integer. Test the function with different inputs.
"""

def func(**kwargs):
    result = {key: value for key, value in kwargs.items() if isinstance(value, int) and type(value) is not bool}
    return result

#input_dict = {'a': 1, 'b': 'b', 'c':3, 'd':4, 'e':5.12,'f':True}
result = func(a=1, b='b', c=3, d=4, e=5.12, f=True)
print(result)