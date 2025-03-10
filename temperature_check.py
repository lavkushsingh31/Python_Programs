# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 22:27:40 2025
@author: Luvkush
Title: Program to validate the city's temperature
"""

temperature = float(input())

if temperature > 0:
    print("The temperature is above freezing (positive)")
elif temperature < 0:
    print("The temperature is below freezing (negative)")
else:
    print("The temperature is exactly at freezing point (zero)")