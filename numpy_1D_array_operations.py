# -*- coding: utf-8 -*-
"""
Created on Mon Jan 19 15:24:08 2026
@author: Luvkush
Title: Basic Numpy array (1-D) operations: my_array = np.array([10, 20, 30, 40, 50]).
"""
import numpy as np

my_array = np.array([10, 20, 30, 40, 50])

print(f"The number of elements in the array is: {my_array.size}")
print(f"Third Element: {my_array[2]}")

print(f"Adding '60' element at the end: {np.concatenate((my_array, [60]))}")
print(f"Adding '60' element at the end: {np.append(my_array, [60])}")

my_array[1] = 25
print(f"Update the value of the second element to 25: {my_array}")

mask = my_array != 40
my_array = my_array[mask]
print(f"Remove the element with the value 40 from the array: {my_array}")

print(f"Index of 30 is: {np.where(my_array == 30)[0][0]}")
print(f"Is 30 present in array: {30 in my_array}")

print(f"Sorting the array in descending order: {np.sort(my_array)[::-1]}")