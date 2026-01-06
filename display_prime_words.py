# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 23:49:55 2023
@author: Luvkush

"""

strs = input("Enter sentence: ")

def is_prime(num):
    for i in range(2,num):
        if num%i == 0:
            return False
    return True


for word in strs.split():
    if is_prime(len(word)):
        print(word, end = " ")