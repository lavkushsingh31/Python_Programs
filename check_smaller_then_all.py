# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 18:25:15 2023
@author: Luvkush
"""

lst = eval(input("Enter list of numbers as it is: "))
n = int(input("Enter a number: "))

result = list(filter(lambda x: x<n, lst))
result_bool = list(map(lambda x: x<n, lst))

print(result)
print(result_bool)
print(f"List has all elements smaller then {n}: {all(result_bool)}")