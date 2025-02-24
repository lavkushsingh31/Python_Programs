# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:44:36 2025
@author: Luvkush
Title: This program calculates the compound interest per the user input
"""


amt = float(input("Enter Principal amount: "))
intr = float(input("Enter rate of interest (in %): "))
years = float(input("Enter the number of years (investing principal amount): "))


def calculate_future_value(amt, intr, years):
    return amt * (1 + (intr/100))**years

fv = calculate_future_value(amt, intr, years)

print(f"Your future amount: {fv}")
