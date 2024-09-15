 #Assignement2
# Part 1: Lists
# 1. Create and Access Elements:
# o Create a list of 5 fruits.
fruits = ["Berry","Banana","Apple","Orange","Grapes" ]
print(fruits)
# o Access the second and fourth fruit in the list and print them.
print(fruits[1],fruits[3])

# 2. Modify a List:
# o Add a new fruit to the list.
fruits.append("Blue Berry")
print(fruits)
# o Replace the third fruit in the list with "Strawberry."
fruits.remove(fruits[2])
fruits.insert(2,"Strawberry")
print(fruits)
# o Remove the last fruit from the list.
fruits.remove("Blue Berry")
print(fruits)

# 3. List Methods:
# o Sort the list alphabetically.
fruits.sort()
print(fruits)
# o Reverse the order of the list.
print(fruits[::-1])
# o Count how many times "Apple" appears in the list (add "Apple" if necessary)
fruits.append("apple")
print(fruits)
print(fruits.count("apple"))

# Part 2: Tuples
# 1. Create and Access Elements:
# o Create a tuple with 5 numbers: 10, 20, 30, 40, 50.
tuple = (10,20,30,40,50)
print(tuple)
# o Print the first and last number in the tuple.
print(tuple[0],tuple[4])

# 2. Immutable Nature of Tuples:
# o Try changing the second number in the tuple to 25. Observe and note down the error message.
# print(tuple.remove(10))
# AttributeError: 'tuple' object has no attribute 'remove'

# 3. Tuple Operations:
# o Use tuple unpacking to assign the values of the tuple to 5 different variables. Print each variable.
# Create a tuple containing three numbers
tuplex = 4, 8, 3
# Print the contents of the 'tuplex' tuple
print(tuplex)
# Unpack the values from the tuple into the variables n1, n2, and n3
n1, n2, n3 = tuplex
# Calculate and print the sum of n1, n2, and n3
print(n1 + n2 + n3)
# Create a tuple containing three numbers
tuplex = 4, 8, 3
# Print the contents of the 'tuplex' tuple
print(tuplex)
# Unpack the values from the tuple into the variables n1, n2, and n3
n1, n2, n3 = tuplex
# Calculate and print the sum of n1, n2, and n3
print(n1 + n2 + n3)

#  Dictionaries
# 1. Create and Access Elements:
# o Create a dictionary that stores information about a student:
# ▪ Name: "John"
# ▪ Age: 20
# ▪ Subjects: ["Math", "Physics", "Chemistry"]
dict = {"Name": "John", "Age": 20 , "Subjects": ["Math", "Physics", "Chemistry"]}
print(dict)
# o Access the student's age and print it.
print(dict["Name"])
print(dict["Age"])


# 2. Modify the Dictionary:
# o Add a new key-value pair for "Grade" with the value "A".
dict["Grade"] ={"A"}
print(dict)
# o Change the student's age to 21.
dict["Age"] = 21
print(dict)
# o Remove the "Subjects" key from the dictionary
removed= dict.pop('Subjects')
print(dict)

# 3. Dictionary Methods:
# o Print all the keys in the dictionary.
keys = list(dict.keys())
print(keys)
# o Print all the values in the dictionary.
values = list(dict.values())
print(values)
