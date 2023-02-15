# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 23:00:08 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""


def calculate_bmi(height, weight):
    bmi = int(weight / (height ** 2))
    return bmi
    

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

try:
    height = float(height)
    weight = float(weight)
    bmi = calculate_bmi(height, weight)
    print(f"You BMI: {bmi}")
except:
    print("Input is not numbers! Please input numbers only!")
    

