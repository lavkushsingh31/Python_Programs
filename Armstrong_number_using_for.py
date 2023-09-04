# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:34:24 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

number = int(input("Enter the number: "))

n = number

cubesum = 0

for i in range(len(str(n))):
    
    rem = n%10
    quo = n//10
    
    cubesum = cubesum + rem**3
    
    n = quo

if cubesum == number:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")

    
    

  