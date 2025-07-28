# -*- coding: utf-8 -*-
"""
Created on Wed May 17 15:16:22 2023
@author: Luvkush
"""


array1 = [0,1,0,3,12]
array2 = [1,7,0,0,8,0,10,12,0,4]


def zeros_first(arr):
    zero_counts = arr.count(0)
    non_zeros = [element for element in arr if element != 0]
    zeros = [0]*zero_counts 
    return zeros + non_zeros

print(zeros_first(array1))
print(zeros_first(array2))