# -*- coding: utf-8 -*-
"""
Created on Sat Jan 10 22:11:10 2026
@author: Luvkush
Title: Define a function that returns another function. The returned function should take an integer and return its square. Test the returned function with different inputs.
Credits: Krish Naik's "Complete Data Science,Machine Learning,DL,NLP Bootcamp" udemy course
"""

def func(raised_to_power):
    def return_func(int_val):
        return int_val**raised_to_power
    return return_func

square_it = func(2)
four_square = square_it(4)

cube_it = func(3)
six_cube = cube_it(6)

print(f"Square of 4: {four_square} ")
print(f"Cube of 6: {six_cube} ")