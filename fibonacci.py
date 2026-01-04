# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:44:03 2023
@author: Luvkush
"""

def generate_fibonacci(terms):
    
    print(f"\nHere are the first {terms} terms of Fibonacci Series: \n")
    
    first = 1
    second = 1
    print(first)
    print(second)
    
    while terms>=3:
        next_element = first + second
        first = second
        second = next_element
        print(next_element)
        terms-=1
    

n = int(input("Please enter the number of terms you want: "))

generate_fibonacci(n)




    
