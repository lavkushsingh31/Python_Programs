# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 12:58:55 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

print("Welcome to the Roller Coaster")
height = float(input("Enter your height (in cms): "))

if height >= 120:
    print("Ride Roller Coaster")
    age = int(input("What is your age: "))
    if age <12:
        print("Please pay $5")
    elif age >=12 & age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")    
else:
    print("Do not Ride Roller Coaster!")
    
    
    



