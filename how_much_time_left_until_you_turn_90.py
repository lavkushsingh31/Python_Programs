# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:10:55 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

# Program to let you know how much time you have with you
# by the time you turn 90

# Assumption: There are 365 days in a year, 52 weeks in a year and 12 months in a year.

age = input("What is your current age? ")
age = int(age)

years_remaining = 90 - age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")