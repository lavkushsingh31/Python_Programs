# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:04:06 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

year = int(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year!")
        else:
            print("This is not leap year!")
    else:
        print("This is a leap year!")
else:
    print("This is not leap year!")
    