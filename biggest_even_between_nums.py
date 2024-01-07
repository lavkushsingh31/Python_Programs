# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 21:46:48 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

if m<n:
    if n%2 == 0:
        print(f"Biggest even number between {m} and {n}")
        print(n)
    else:
        print(f"Biggest even number between {m} and {n}")
        print(n-1)
else:
    if m%2 == 0:
        print(f"Biggest even number between {n} and {m}")
        print(m)
    else:
        print(f"Biggest even number between {n} and {m}")
        print(m-1)
    