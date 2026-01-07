# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 23:36:20 2023
@author: Luvkush
"""

n = int(input("Enter the number"))

sum = 0

for num in range(1,n+1):
    sum = sum + (1/num)

print(sum)
