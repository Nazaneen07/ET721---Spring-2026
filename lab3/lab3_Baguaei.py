"""
Nazaneen Baguaei, 
Feb 3, 2026
lab 3, condition statement and loop is python 
"""
print("\n ----- Example 1: Set-up of conditional statement -------")
# coniditonal statement states the flow the program 
age = 11
if(age >=21):
    print("You are an adult!")
elif(age<21 and age>=13):
    print("you are a teen")
elif(age<13 and age>0):
    print("You are a kid")
else: 
    print("unable to read age")

print("\n ----- Example 2: for loop -------")
# for loop as a counter to print from 9 to 1, step 1
for n in range(9,0,-1):
    print(n)

# for loop in a list 
print('\n-------- Example 3: for loop in a list -------')
numbers = [3,2,6,1,-8,9,-5]
count_negative = 0
for m in numbers: 
    if m<0:
        count_negative += 1 
else: 
    print(f"there is/are {count_negative} negative numbers")
# for-else, the else statement will run only after the completion of all iteration in the for loop 

print('\nEND OF PROGRAM!')

print('\n-------- Example 4: while loop as a counter -------')
# while loop to print from -3 to 5, unclusive, step of 2, output --> -3  -1  1  3  5
x = -3
while x <= 5:
    print(x)
    x += 2 

print('\n-------- Example 5: while loop to validate an input -------')
# program collects a number from the user and print if the number is even or odd 
# after it, the program will ask the user if another number will be tested 
# if the user type 'y' or 'Y' then the program will run 
# if the user types any other charecter that is not 'y' or 'Y', the program will stop 

decision_user = 'y' 
user_number = 0 

while True: 
    user_number = int(input("Enter a number: "))
    if user_number%2 == 0 and user_number !=0 : 
        print(f"{user_number} is EVEN")
    elif user_number ==0:
        print("The number is zero")
    else: 
        print(f"{user_number} is ODD")

    decision_user = input("Do you want another run? y or Y for yes: ")
    if decision_user !='y' and decision_user != 'Y': 
        break

print('\n-------- EXCERCISE 1: validate a number between 1 and 9 -------')
# use while loop to validate that the user_number is between 1 and 9
user_number = 0
while user_number < 1 or user_number > 9:
    user_number = int(input("Enter a number between 1 and 9: "))
    if user_number < 1 or user_number > 9:
        print("Invalid number! Try again.")
    else:
        print(f"Valid number: {user_number}")

print('\n-------- EXCERCISE 2: Guess a number with 3 attempts -------')
# use loop to allow the user to guess the number three times
# if the user guesses the number before the third attempt, the program should end (break)
number = 9 
attempt = 0

while attempt < 3:
    user_guess = int(input("Guess the number (1-10): "))
    attempt += 1
    
    if user_guess == number:
        print(f"Congratulations! You guessed the number in {attempt} attempt(s)!")
        break
    else:
        print(f"Wrong guess! Attempts remaining: {3 - attempt}")
else:
    print(f"Sorry, you ran out of attempts. The number was {number}")

print('\nEND OF PROGRAM!')