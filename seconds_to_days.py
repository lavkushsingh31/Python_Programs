# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:29:10 2023
@author: Luvkush
"""

secs = int(input("Enter seconds: "))

days = secs//(1*24*60*60) # no of secods in 1 day

rem_secs = secs%(1*24*60*60)
hrs = rem_secs//(1*60*60)

rem_secs = rem_secs%(1*60*60)
mins = rem_secs//(1*60)

rem_secs = rem_secs%(1*60)

print(f"Days: {days} Hours: {hrs} Mins: {mins} Secs: {rem_secs}")

