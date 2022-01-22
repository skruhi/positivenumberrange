# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 21:25:09 2022

@author: skruh
"""

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num >= 0:
        print(num, end = " ")
