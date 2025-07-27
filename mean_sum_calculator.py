# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:26:29 2025
@author: Luvkush
Title: Calculate the mean and sum of entered numbers, until 0 is entered
"""

nums = []

while True:
    try:
        i = int(input())
    except:
        print("Exception occured")
        break
    else:
        if i != 0:
            nums.append(i)
        else:
            break

sum_of_nums = sum(nums)
mean = sum_of_nums/len(nums)
print(f"Average and Sum of the above numbers are: {mean} {sum_of_nums}")