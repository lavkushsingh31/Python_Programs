# -*- coding: utf-8 -*-
"""
Created on Sat May 10 19:20:41 2025
@author: Luvkush
Title: Program to find the largest even number from the input list
"""

num_list = eval(input("Enter the list of numbers: "))
print(f"Num List: {num_list}")
print(f"Type of num list: {type(num_list)}")
largest_even = None
i = 0

while i<len(num_list):
    num = num_list[i]
    print(f"Number in loop: {num}")
    print(f"Value of i in loop: {i}")
    i+=1
    print(f"Incremented value of i in loop: {i}")
    if num%2 == 0:
        print(f"Even number checked and found true: {num}")
        if largest_even is None or largest_even < num:
            print(f"Largest even num prev value: {largest_even}")
            largest_even = num
            print(f"Updated largest even num value: {largest_even}")

print(f"Largest Even number: {largest_even}")