# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 16:46:26 2025
@author: Luvkush
Title: Sum of digits of a positive integer until it is a single digit
"""

def sum_nums(num):
    sum_num = 0
    while num!=0:
        rem = num%10
        sum_num+=rem
        num = num//10
    return sum_num
        
#print(sum_nums(12345))
input_num = input("Enter number: ")

try:
    input_num = int(input_num)
except:
    print("Cannot convert entered number to Integer!")
else:
    step = 1
    while input_num//10 != 0:
        sum_of_nums = sum_nums(input_num)
        print(f"Step-{step} Sum: {sum_of_nums}")
        input_num = sum_of_nums
        step+=1
