"""
Nazaneen Baguaei, 
Feb 5, 2025
lab 5, functions
"""
import math
import random

#example 1
def area_rectangle(width, length):
    return width*length

#void function doesnt return value
def print_area_result(width, length, area): 
    print(f"The area of rectangle of {width} and {length} is {area}")

# example 2: calculate teh distance of two points
# disctance = square_root of ( (x2-x1)^2 + (y2-y1)^2 )
# function 1) collect a number between 1 and 10 
def collectnum(point):
    num = int(input("Enter a number for " + point + ": "))
    # use a loop to recollect the number if teh number isnt between 1 and 10
    while(num < 1 or num > 10):
        num = int(input("Invalid! Enter a number between 1 and 10: "))
    
    return num

# function that calculates and returns the distance 
# distance = square_root of ( (x2-x1)^2 + (y2-y1)^2 )
def calculate_distance(x1, x2, y1, y2):
    return math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))

# function to print result 
def print_distance(x1, x2, y1, y2, distance):
    print(f"distance of points ({x1},{y1}) and ({x2},{y2}) is {round(distance,2)}")

# ---------------- EXERCISE ----------------
# function that generates and returns a random number
def generate_random(min_num, max_num):
    return random.randint(min_num, max_num)

# function that compares guess number with random number
def compare_number(guess, random_num):
    if random_num < guess:
        print("The number is smaller than the guess number")
    if random_num > guess:
        print("The number is bigger than the guess number")
    if random_num == guess:
        print("You got it!")
