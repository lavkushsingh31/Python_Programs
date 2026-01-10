# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 22:49:50 2026
@author: Luvkush
Title: HOF using Generators
Credits: Krish Naik's "Complete Data Science,Machine Learning,DL,NLP Bootcamp" udemy course
"""

def hof_generator(filter_func, map_func, int_list):
    
    filtered = (x for x in int_list if filter_func(x)) # () instead of list []
    
    # We map the filtered items one-by-one
    mapped = (map_func(x) for x in filtered)
    
    return mapped


result_gen = hof_generator(lambda x: x%2==0, lambda x: x**2, [1, 2, 3, 4, 5, 6])

print(f"Generator at: {result_gen}")
print(f"Actual Result: {list(result_gen)}")

