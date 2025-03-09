# -*- coding: utf-8 -*-
"""
Created on Sun Mar  9 15:53:53 2025
@author: Luvkush
Title: Updating elements in Tuple
"""


tup = input()
item = input()

tup= tup.split(',')
tup.remove(item)
tup = tuple(tup)
print(tup)
