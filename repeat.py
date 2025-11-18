# Variables & Data Types
x = 10              # int
pi = 3.14           # float
name = "Vlad"       # str
is_admin = True     # bool
items = [1, 2, 3]   # list
person = {"age": 25, "city": "Düsseldorf"}  # dict

# Conditions (if / else)
age = 20 

if age >= 18:
    print("Adult")
else: 
    print ("Child")

# Loops (for / while)
items = [10, 20, 30]

# for:
for item in items:
    print(item)
    
# while:
counter = 0

while counter < 10:
    print(counter)
    counter += 1

# Functions
def greet(user_name):
    return f"Hello, {user_name}"
print(greet("Vlad"))

# Lists
numbers = [10, 20, 30]

numbers.append(40) # add 40 into the lists
numbers.remove(20) # remmove 20 from the lists

print(numbers[2])
print(len(numbers)) # show the lenght of lists 

# Dictionaries(dict)
user = {
    "name": "Vlad",
    "age": 26
}

print(user["name"])
user["country"] = "Germany"
print(user["country"])


