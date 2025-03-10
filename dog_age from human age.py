# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 14:46:11 2023
@author: Luvkush
Title: Calculate the dog's age in dog years
"""

# Write your code here

h_age = int(input())

if h_age <=2:
    dog_age = h_age*10.5
elif h_age > 2:
    dog_age = 2*10.5 + ((h_age-2)*4)
else:
    dog_age = 0

dcimal = int(str(dog_age).split('.')[-1])
if dcimal==0:
    print(f"Decimal: {dcimal}")
    dog_age = int(dog_age)
print(f"Dog's age: {dog_age}")





