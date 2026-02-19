"""
Nazaneen baguaei
Feb 19, 2026
"""

print("\n --- Example 1: read file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read(30)
    print(filecontent)
    filecontent = file1.read(5)
    print(filecontent)


# check if the file is closed 
print(f"Is the file closed? {file1.closed}")

print("\n --- Example 2: readline file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.readline(30)
    print(filecontent)
    filecontent = file1.readline(5)
    print(filecontent)

print("\n --- Example 3: readlines file")
# readline makes a list of all the lines in the text file. each line is an item in the list 
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    print(filecontent)
    filecontent = file1.readlines(5)
    print(filecontent)

print("\n --- Example 4: Loop through each line in a file")
# readlines makes a list of all the lines in the text file. each line is an item in the list 
with open("phrases.txt", "r") as file1:
    filecontent = file1.readlines()
    for eachline in filecontent:
        print(eachline.strip()) # strip() method removes \n in each line

print("\n --- Example 5: create file")
# w mode create a file if the file doesnt exist. on the other hand, if the file exists, w mode will overwrite the data in the file
with open("Baguaei.txt", "w") as file: 
    file.write("Python basics for data science\n")
    file.write("student's full name")

print("\n --- Example 6: append date into an existing file")
# append the date and time into "lastname.txt" file 
from datetime import datetime

with open("Baguaei.txt", "a") as file: 
    file.write(f"\nLast update: {datetime.now()}")

print("\n --- Example 7: copy a file")
# copy file "lastname.txt" into a new file 
with open("Baguaei.txt", "r") as readfile: 
    with open("newfile.txt", "w") as writefile: 
        for eachline in readfile: 
            writefile.write(eachline)

print("\n --- Example 8: pandas a file")
import pandas as pd 

data ={
    'Name' : ['Alice', 'Bob', 'Charlie'],
    'Age'  : [25, 30, 35]
}

df = pd.DataFrame(data)
print(df)

print("\n --- Example 9: Creating df ")
df = pd.read_excel("classdata.xlsx")
print(df)
print(df.head())

print("\n --- EXERCISE ")

def email_read(filename):
    try:
        gmail_count = 0
        yahoo_count = 0
        hotmail_count = 0

        with open(filename, "r") as file:
            filecontent = file.readlines()
            for eachline in filecontent:
                eachline = eachline.strip()
                if "@gmail" in eachline:
                    gmail_count += 1
                elif "@yahoo" in eachline:
                    yahoo_count += 1
                elif "@hotmail" in eachline:
                    hotmail_count += 1

        with open("reportemail.txt", "w") as reportfile:
            reportfile.write(f"gmail = {gmail_count}\n")
            reportfile.write(f"yahoo = {yahoo_count}\n")
            reportfile.write(f"hotmail = {hotmail_count}\n")

        return gmail_count, yahoo_count, hotmail_count

    except FileNotFoundError:
        print("Error: file not found")

email_read("user_email.txt")

with open("reportemail.txt", "r") as file:
    print(file.read())