# -*- coding: utf-8 -*-
"""
Created on Mon Jan 12 23:33:41 2026
@author: Luvkush
Title: Sort a list having dicts based on age
"""

l = [{'Age': 30, 'Name': 'Bob'},
     {'Age': 20, 'Name': 'Charlie', 'Point': 70},
     {'Age': 50, 'Name': 'Alice', 'Point': 80}]

sorted_result = sorted(l, key = lambda x: x['Age'])
print(sorted_result)

# Inplace list sorting
l.sort(key= lambda x: x['Age'])
print(l)
