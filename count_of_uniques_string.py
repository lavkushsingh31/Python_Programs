# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 15:45:47 2025
@author: Luvkush
Title: Find the count of unique in String
"""

sn = input("Enter the string: ")
print(f"You entered: {sn}")
sn = set(sn.split())
print(f"Uniques: {sn}")
print(f"Length of uniques present: {len(sn)}")


