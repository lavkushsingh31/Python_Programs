# -*- coding: utf-8 -*-
"""
Created on Sun Jan 11 19:00:03 2026
@author: Luvkush
Title: Define a function that takes another function as a callback and a list of integers. The function should apply the callback to each integer in the list and return a new list with the results. Test with different callback functions.
Credits: Krish Naik's "Complete Data Science,Machine Learning,DL,NLP Bootcamp" udemy course
"""

def callback_func(func, int_list):
    result = [func(element) for element in int_list]
    return result

def squares(value):
    return value**2

input_list = [1,2,3,4,5]
result = callback_func(squares, input_list)
print(result)
        