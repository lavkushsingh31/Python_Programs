# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 22:21:45 2026
@author: Luvkush
Title: Define a higher-order function that takes two functions, a filter function and a map function, along with a list of integers. The higher-order function should first filter the integers using the filter function and then apply the map function to the filtered integers. Test with different filter and map functions.
Credits: Krish Naik's "Complete Data Science,Machine Learning,DL,NLP Bootcamp" udemy course
"""

def hof(filter_func, map_func, int_list):
    filtered = [x for x in int_list if filter_func(x)]
    print(f"Filtered: {filtered}")
    mapped = [map_func(x) for x in filtered]
    # Compact way: mapped = [map_func(x) for x in int_list if filter_func(x)]
    return mapped

result = hof(lambda x: x%2==0, lambda x: x**2, [1,2,3,4,5,6])
print(f"Result: {result}")