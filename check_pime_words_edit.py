# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 17:13:06 2023
@author: Luvkush
"""

strs = input()
m = strs.split(" ")


def prime(a):
    for j in range(2, len(a)):
        if len(a)%j == 0:
            return False
    return True


def app(x):
    n=[]
    for i in x:
        if prime(i):
            n.append(i)
    return n

result = app(m)
print(" ".join(result))