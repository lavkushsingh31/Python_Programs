# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:44:55 2025
@author: Luvkush
Description: This program will let user input a string and any integer n. The program will 
output the last n characters of the string
"""


text = input("Enter any string: ")
n = int(input("Enter any integer: "))

sliced = text[-n:]

print(f"\nLast {n} characters: {sliced}")