# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 17:30:55 2023
@author: Luvkush
Credits: https://www.udemy.com/course/100-days-of-code
"""

print("\n ***** Splitted Bill Calculator ***** \n")

bill = float(input("Enter the bill amount: $"))
tip_percent = float(input("Enter the percent(%) of tip you would want to pay: "))
total_members = int(input("How many people to split the bill with: "))
total_bill = bill + (tip_percent*bill/100)
per_head_bill = total_bill/total_members
#per_head_bill = round(per_head_bill,2)
per_head_bill = "{:.2f}".format(per_head_bill)
print(f"\nEach person should pay: ${per_head_bill}")




