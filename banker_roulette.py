# -*- coding: utf-8 -*-
"""
Created on Mon May  1 06:35:39 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

import random

names = input("Enter the names of people having dinner: ").split(", ")

payer = random.randint(0, len(names)-1)
print(f"{names[payer]} is going to buy the meal today!")