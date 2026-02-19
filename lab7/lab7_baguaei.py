"""
Nazaneen baguaei
Feb 19, 2026
"""

print("\n --- Example 1: read file")
with open("phrases.txt", "r") as file1:
    filecontent = file1.read()
    print(filecontent)

# ccheck if the file is closed 
print(f"Is the file closed? {file1.closed}")