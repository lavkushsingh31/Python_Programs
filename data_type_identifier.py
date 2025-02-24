# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:52:40 2025
@author: Luvkush
Title: This program identifies the data type of the user input
"""

name = eval(input("Enter Name: "))
age = eval(input("Enter Age: "))
salary = eval(input("Enter Salary: "))
experience = eval(input("Enter Experience: "))
hobbies = eval(input("Enter Hobbies: "))
skills = eval(input("Enter Skills: "))
address = eval(input("Enter Address: "))

inputs = [name, age, salary, experience, hobbies, skills, address]

for value in inputs:
    print(type(value))