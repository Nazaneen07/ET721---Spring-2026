"""
Nazaneen Baguaei, 
Feb 5, 2025
lab 5, functions
"""
import math
from lab5_function_Baguaei import * 
    
print('\n ----- Example 1: user-defined function ')
w = 8
length = 3
a = area_rectangle(w,length)
print_area_result(w,length,a)

print('\n ----- Example 2: calculate ')
x1 = collectnum('x1')
x2 = collectnum('x2')
y1 = collectnum('y1')
y2 = collectnum('y2')

#testing
print(f"({x1},{y1}) ({x2},{y2})")

# testing
print(f" distance = {calculate_distance(x1,x2,y1,y2)}")

# testing

distance = calculate_distance(x1,x2,y1,y2)
print_distance(x1,x2,y1,y2,distance)

print('\nEXERCISE')