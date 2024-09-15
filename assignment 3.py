# 1.Introduction to Slicing:
# a. Given a string s = "Hello, World!", slice and print the following:
# i. The entire string.
s = "Hello, World!"
print(s[0::1])
# ii. The first 5 characters.
print(s[0:5:1])
# iii. The last 5 characters.
print(s[8:13:1])
# iv. The string excludes the first and last characters.
print(s[1:12:1])
# v. Every second character in the string
print(s[0:13:2])

# 2.Slicing with Negative Indices:
# a. Use negative indices to slice and print the following from the string
s = "Hello, World!"
# 1. The last 3 characters.
print(s[-2-1:])
# 2. All characters except the last 2.
print(s[-13:-2])
# 3. The string reversed.
print(s[::-1])

# Part 2: Advanced Slicing
# 1. Slicing Substrings:
# a. Given a string sentence = "The quick brown fox jumps over the lazy dog", slice and print the following:
# i. The word "quick".
r = "The quick brown fox jumps over the lazy dog"
print(r[4:9:].split(','))
# ii. The word "lazy".
print(r[34:39:])
# iii. The words "brown fox jumps"
print(r[10:25:])

# 2. Step Slicing:
# a. Use step slicing to print the following from the string s:
r = "The quick brown fox jumps over the lazy dog"
# i. Every third character.
print(r[0::3])
# ii. Every third character starting from the second character.
print(r[2::3])
# iii. The string reversed, stepping by 2.
print(r[-1:-57:-2])

# Part 3: Practical Application
# 1. Extracting Information:
# a. Given a string data = "2024-09-01,Sunny,25°C", extract and print
# the following:
data = "2024-09-01,Sunny,25°C"
# i. The date.
print(data[0:10:].split(","))
# ii. The weather condition.
print(data[11:16:].split(","))
# iii. The temperature
print(data[17::].split(","))

# 2. Reformatting Strings:
# i. Given a string phone_number = "(123) 456-7890", reformat it to ‘123-456-7890’
phone_number = "(123) 456-7890"
m = phone_number.replace("(", "").replace(")", "").replace(" ", "")
number = f"{m[:3]}-{m[3:6]}{m[6:]}"
print(number)


# Part 4: Questions based on string methods
# 1. Upper and Lower Case Conversion:
# i. Given a string s = "Hello, World!", perform the following:
s = "Hello, world!"
# b. Convert the string to all uppercase letters.
print(s.upper())
# c. Convert the string to all lowercase letters.
print(s.lower())
# d. Convert the string to title case.
print(s.title())
# e. Capitalize the first letter of the string.
print(r.title())

# 2. Finding Substrings:
#  Given a string s = "The quick brown fox jumps over the lazy dog",
r = "The quick brown fox jumps over the lazy dog"
# perform the following:
# a. Find the position of the substring "fox".
print(r.find("fox"))
# b. Check if the substring "cat" is in the string.
print(r.find("cat"))
#the index of the cat is -1 soo the cat is not present in the sentence.

# 3. Replacing Substrings:
#  Given a string r = "The quick brown fox jumps over the lazy dog",
# perform the following:
r = "The quick brown fox jumps over the lazy dog"
# a. Replace "fox" with "cat".
print(r.replace("fox","cat"))
# b. Replace all spaces with underscores.
print(r.replace(" ","_"))
# c. Split the string into a list of words.
print(r.split(" "))
# d. Split the string by the letter 'o'.
print(r.split("o"))

# 4.Joining Strings:
#  Given a list of words
list = ["The", "quick", "brown", "fox"]
#  perform the following:
# a. Join the words with spaces.
g=" ".join(list)
print(g)
# b. Join the words with hyphens
h = '-'.join(list)
print(h)


