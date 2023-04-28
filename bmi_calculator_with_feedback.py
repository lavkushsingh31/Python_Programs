# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 23:28:50 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

def calculate_bmi(height, weight):
    print("calculating")
    bmi = weight / (height ** 2)
    print("calculations done!")
    return round(bmi)
    

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

try:
    print("converting the numbers")
    height = float(height)
    weight = float(weight)
    print("numbers converted")
    bmi = calculate_bmi(height, weight)
    print(f"bmi returned! it is {bmi}")
       
except:
    print("Input is not numbers! Please input numbers only!")
    
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")