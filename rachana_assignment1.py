# -*- coding: utf-8 -*-
"""rachana_assignment1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zXkgM8FelT_0p4R-mudoWz1MM8BYjFHt
"""



1. Understanding Variables
a) Define a variable in Python. Provide an example of how to create a variable that stores your name.
 variable is acts as a address for where the data is stored in memory.
 name = "rachana"

b) variables are mutables, they can be changed and reload the values. but constants immutables and they can't be changed.
python don't have any constants.

2.Working with Different Data Types
a) Create variables of the following types in Python:
1)int i = 2
2)float i =0.99
3)name = 'rachana'

b)Write a Python script to display the type of each variable you created.
a = 1
b = 2.3
name = 'rachana'
r = True
print(type(a))
print(type(b))
print(type(name))
print(type(r))

3 Arithmetic Operators
a) Explain the following arithmetic operators with examples:
arthmatic operator : it will do operation like addition,subtaction,multiplication,division.
1. addition arithmatic: it will add number of variables
2. subtraction arithmatic: it will subtract numbers
3. multiplication arithmatic: it will multiply numbers
4. division arithmatic: it will divide two numbers
5. modulus arithmatic: it will give the reminder when it divides the two numbers
a = 10
b = 20
c = a + b
e = a - b
f = a * b
g = a \ b
h = a % b
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)


b) Write a Python script to calculate the area of a rectangle using variables `length` and `width` with
values 5 and 10, respectively. Use the multiplication operator
l = 5
b = 10
area = l * b
print(area)

4.Comparison and Logical Operators (5 Marks)
a) Explain the following comparison operators with examples
1. Equal : it is used to find whether the two variables or numbers are equal or not.
a = 10
b = 10
 if a == b:
  print("a == b ")


2.Not equal(!=): it says that the two numbers are not equal.
a = 10
b = 7
 if a != b:
  print("a is not equal to b ")
3. Greater than (`>`): it used to say which is greater number
a = 10
b = 9
 if a > b:
  print("a is greater than b ")
4. Less than (`<`): it is used to say which is smaller number
a = 10
b = 9
 if a < b:
  print("a is smaller than b ")
5. Greater than or equal to (`>=`): it says that the two numbers are equal are greater
a = 10
b = 10
 if a >= b:
  print("a is greater or equal than b ")
6. Less than or equal to (`<=`):it says that the two numbers are equal are lesser
a = 10
b = 9
 if a <= b:
  print("a is lesser or equal than b ")

5. Write a Python script that asks the user to input two numbers and then:

a)Adds the two numbers and prints the result.
num1 = int(input("enter the num1"))
num2 = int(input("enter the num2"))
result = num1 + num2
print(result)


b)Subtracts the second number from the first and prints the result
num1 = int(input("enter the num1"))
num2 = int(input("enter the num2"))
result = num2- num1
print(result)


c)Multiplies the two numbers and prints the result
num1 = int(input("enter the num1"))
num2 = int(input("enter the num2"))
result = num1 * num2
print(result)


d)Divides the first number by the second and prints the result (handle division by zero).
num1 = int(input("enter the num1"))
num2 = int(input("enter the num2"))
result = num2/num1
print(result)

 






