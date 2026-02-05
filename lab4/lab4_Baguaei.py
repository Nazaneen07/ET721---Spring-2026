"""
Nazaneen Baguaei, 
Feb 5, 2026
lab 4, dictionary 
""" 

print("---- Example 1: dictionary ")
# declare and initialize a dictionary
contacts ={
    'Bill': '718-111-2222',
    'Rick': ' 718-000-1111',
    'Mary': '800-222-3333'
    
}
print(f"original dictionary {contacts}")

# update a value of a dictionary 
contacts['Rick'] = '347-000-1111'

print(f"updated dictionary {contacts}")

# add new key-value pair
contacts['Peter'] = '888-000-1111'

print(f"updated dictionary with new pair = {contacts}")

print("---- Example 2: Loop through a dictionary ")
# for loop to print each key in the dictionary
for v in contacts:
    print(v)

# for loop to print each key in the dictionary
for v in contacts:
    print(contacts[v])

# for loop to print each key in the dictionary
for v in contacts:
    print(f'{v} phone number is {contacts[v]}')

print("\n ----- Example 3: items(), keys(), values(), methods in dictionart ")
#items method returns all the key-values pairs in the dictionary
print(f"items in the dictionary {contacts.items()}")
# key method returns all the keys in the dictionary
print(f"all keys in the dictionary {contacts.keys()}")
# values method returns ll the values in the dictionary 
print(f"all values in the dictionary {contacts.values()}")

print("\n ----- Example 3: check if a key is 'in' or not 'in' a dictionary ")
check_name = 'lucy'
check = check_name in contacts 
print(f"is {check_name} in the dictionary? {check}")

print("\n ----- Example 5: Length of a dictionary" )
print(f"contacts has {len(contacts)} key-value pairs")

print("\n ----- Example 6: Remove a pair ")
print(f"original dictonary = {contacts}")
contacts.pop("Mary")
print(f"updated dictionary = {contacts}")

print("\n ----- Example 7: Get method ")
# Get method returns the key-value pair of a key 
print(f"key-value pair = {contacts.get('Bill')}")

print("\n ----- Example 8: updated method ")
# can be used to update a value of a key or to add a new key-value pair 
contacts.update({'Annie' : '718-999-8888'})
print(f"{contacts}")

print("\n ----- EXCERCISE ")







