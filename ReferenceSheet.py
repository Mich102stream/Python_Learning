# my_name = "Michael"  # test comment
# my_age = 35

# number_x = 10
# number_y = 5


# print("Hello World")

# print("Another line")

# print(24 * 7 / 33)

# print("My name is {} and my Favourite drink is {}".format("Michael", "Coffee"))

# print(f"My name is {my_name} and I am {my_age} years old")

# print("My name is " + my_name + " and I am " + str(my_age) + " years old.")

# my_name = "Michael"
# my_age = 35
# student = True

# if student:
#     print("Hello " + my_name + " and I am " + str(my_age)  + " and I am a student")
# else:
#     print("Hello " + my_name + " and I am " + str(my_age)  + " and I am not a student")
    
    

# Activities


# Activity 1

my_name = "Michael"
my_age = 35
favorite_colour = "Blue"


print(f"My name is  {my_name}   and I am  {my_age}  years old. My favourite colour is  {favorite_colour} .")


# Activity 2

breakfast = "Cereal"
lunch = "Sandwich" 
dinner = "Pasta"

print("Today I had " + breakfast + " for breakfast, " + lunch + " for lunch and " + dinner + " for dinner.")

breakfast = "Toast"
lunch = "Soup"
dinner = "Pizza"

print("Tomorrow I will have " + breakfast + " for breakfast, " + lunch + " for lunch and " + dinner + " for dinner.")


# Activity 3

print("")
print("       |       |     ")
print("       |       |     ")
print("       |       |     ")
print("----------------------")
print("       |       |     ")
print("       |       |     ")
print("       |       |     ")
print("----------------------")
print("       |       |     ")
print("       |       |     ")
print("       |       |     ")
print("")

# Activity 4

space1 = "X"
space2 = "O"
space3 = "X"
space4 = "O"
space5 = "X"
space6 = "O"
space7 = "X"
space8 = "O"
space9 = "X"

print("")
print("       |       |     ")
print(f"   {space1}   |   {space2}   |   {space3}   ")
print("       |       |     ")
print("----------------------")
print("       |       |     ")
print(f"   {space4}   |   {space5}   |   {space6}   ")
print("       |       |     ")
print("----------------------")
print("       |       |     ")
print(f"   {space7}   |   {space8}   |   {space9}   ")
print("       |       |     ")
print("")



# Operators

# print( number_x + number_y )

# print( number_x - number_y )

# print( number_x * number_y )

# print( number_x / number_y )

# print( number_x % number_y )

# if number_x > number_y:
#     print("X is greater than Y")
# else:    
#     print("Y is greater than X")


# Assignment Operators to assign values to variables

i = 10


i = i + 2

print(i)

# += adds the value on the right to the variable on the left

i = 10

i += 4

print(i)


# -= subtracts the value on the right from the variable on the left

i = 10

i -= 4

print(i)

# *= multiplies the value on the right by the variable on the left

i = 10

i *= 4

print(i)

# /= divides the value on the right by the variable on the left

i = 10

i /= 4

print(i)

# %= returns the remainder of the division of the variable on the left by the value on the right

i = 10

i %= 4

# **= raises the variable on the left to the power of the value on the right

print(i)


i = 10

i **= 4

print(i)




# Properties and Methods in Python


# Len property returns the length of a string

print(len("Hello"))  # returns the length of the string which will be 5 characters.

print(len("Hello World"))  # returns the length of the string which will be 11 characters including the space.

print("Hello"[1])   # returns the character at index 1 which is e in this case due to 0 based indexing.


# Methods in Python are functions that are associated with an object.

#"hello".upper() # .upper() method converts all characters in a string to uppercase.

text = "hello world"

print(text.upper())  # returns HELLO WORLD


#"hello".lower()  # .lower() method converts all characters in a string to lowercase.

text = "HELLO WORLD"

print(text.lower())  # returns hello world

#"hello".capitalize()  # .capitalize() method converts the first character of a string to uppercase.

text = "hello world"

print(text.capitalize())  # returns Hello world


#"hello".count()  # .count() method returns the number of times a specified value appears in a string.

text = "hello world"

print(text.count("l"))  # returns 3 as l appears 3 times in the string.

#"hello".find()  # .find() method searches the string for a specified value and returns the position of where it was found.

text = "hello world"

print(text.find("w"))  # returns 6 as w is found at index 6 in the string.

#"hello".replace()  # .replace() method replaces a specified value with another value in a string.

text = "hello world"

print(text.replace("world", "universe"))  # returns hello universe

#"hello".strip() # .strip() method removes any leading or trailing white spaces from a string.

text = " hello world "

print(text.strip())  # returns hello world


# how to use multiple methods in a single line of code

text = " hello world "

print(text.strip().upper())  # returns HELLO WORLD removing the spaces and converting the string to uppercase.

print(text.upper().replace("world","universe"))  # returns HELLO UNIVERSE converting the string to uppercase and replacing world with universe.

print(text.strip().lower())  # returns hello world removing the spaces and converting the string to lowercase.

print(text.strip().capitalize())  # returns Hello world removing the spaces and converting the first character to uppercase.

print(text.strip().count("l"))  # returns 3 as l appears 3 times in the string.

print(text.strip().find("w"))  # returns 6 as w is found at index 6 in the string.

print(text.strip().replace("world", "universe"))  # returns hello universe removing the spaces and replacing world with universe.

print(text.strip().replace("world", "universe").upper())  # returns HELLO UNIVERSE removing the spaces and replacing world with universe and converting the string to uppercase.

print(text.strip().replace("world", "universe").upper().count("l"))  # returns 0 as l does not appear in the string after the replacement and conversion to uppercase.




# Python Syntax

# Python naming convention is called snake_case where all letters are lowercase and words are separated by an underscore.

favourite_drink = "Coffee"
this_number = 3
first_name = "Michael"






# Python If:Else Statements

music = "classical"


if music == "classical":
    print("Oh no it's that classical again")
elif music == "Rock":
    print("I love Rock music")
else:
    print("I don't hear music")
    
# == is used to compare two values and returns True if they are equal and False if they are not equal.

# <= is used to compare two values and returns True if the value on the left is less than or equal to the value on the right.

# >= is used to compare two values and returns True if the value on the left is greater than or equal to the value on the right.



# Activity 1

age = 20

if age > 17:
    print("Yes I can serve you")
else:
    print("You are not old enough")
    

age = 14

if age > 17:
    print("Yes I can serve you")
else:
    print("You are not old enough!")



# and operator is used to combine two conditions and returns True if both conditions are True.


place = "MCR"
weather = "Cloudy"

if place == "MCR" and weather == "Sunny":
    print("check again")
elif place == "MCR" and weather == "Rain":
    print("Obvs")
else:
    print("Why is it not raining")
    
    

# Activity 2 

age = 20
country = "UK"

if age > 17 and country == "UK":
    print("You can drink")
elif age > 21 and country == "USA":
    print("You can drink")
else:
    print("You are not old enough to drink")
    
# This will print You can drink as the age is greater than 17 and the country is UK. But if the country was USA then it would print You are not old enough to drink.


if age > 17 and country.lower() == "uk":
    print("Yes I can serve you")
elif age > 17 and country.lower() != "uk":
    print("Where are you?")
else:
    print("You are not old enough")
    
# .lower() method is used to convert the string to lowercase so that the comparison is case insensitive.



# or operator is used to combine two conditions and returns True if at least one of the conditions is True.


day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("When's the weekend?")
    


# and

# True and True = True
# True and False = False
# False and False = False

# or

# True or True = True
# True or False = True
# False or False = False




# Challenge 1

# Create a variable called Password check how many letters are in the password, if there is less than 8 print "Password is too short" Otherwise print the password.

password = "password"

if len(password) < 8:
    print("Password is too short")
else:
    print(password)
    

# Challenge 2

# Create a variable called num. Check if the variable is divisible by 3 or 5. if it is, print "This number is divisible by 3 or 5" to the console. otherwise print "This number is not divisible by 3 or 5".

num = 15

if num % 3 == 0 or num % 5 == 0:
    print("This number is divisible by 3 or 5")
else:
    print("This number is not divisible by 3 or 5")
    

# Challenge 3

# Create a variable called num. if num is divisible by 3 print "fizz", if it's divisible by 7 print "buzz", if it's divisible by both 3 and 7 print "fizz buzz". Otherwise print num.

num = 21

if num % 3 == 0 and num % 7 == 0:
    print("fizz buzz")
elif num % 3 == 0:
    print("fizz")
elif num % 7 == 0:
    print("buzz")
else:
    print(num)
    

# Challenge 4

# Create a variable called Word that takes a string. Create an if statement that checks if the last letter is the same as the first. if it is, return true, otherwise return false.

word = "Hello"

if word.lower()[0] == word.lower()[-1]:
    print(True)
else:
    print(False)
    
    
# Challenge 5

# Create a variable called time, a variable called place_of_work and a variable called town_of_home. Create an if statement that prints where someone is at times of the day. Eg, if the time is 7 print "I'm at home", if the time is 8 print "I'm commuting", if the time is 9 print "I'm at work".

time = 10

place_of_work = "work"

town_of_home = "Bolton"

if time == 7:
    print("I'm at " + town_of_home)
elif time == 8:
    print("I'm commuting")
else:
    print("I'm at "+ place_of_work)


    
    
# Challenge 6

# Create two variables called num1 and num2. Create an if statement that checks if the results of the sum is even. if it is return a success mssage.

num1 = 10
num2 = 20

if (num1 + num2) % 2 == 0:
    print("Success")
else:
    print("Failure")


# Challenge 7

# Create a variable called num. Check if the number is a palindrome (look the same forward as it does backwards eg. 1001 and 20202).

num = 1007

if str(num) == str(num)[::-1]: # str(num) converts the number to a string and str(num)[::-1] reverses the string and compares it to the original string.
    print("Palindrome")
else:
    print("Not a Palindrome")


# Challenge 8

# Take the string "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi". find the index of the last vowel in the string.

string = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"

last_index = -1

if string.lower().rfind("a") > last_index:
    last_index = string.lower().rfind("a")
if string.lower().rfind("e") > last_index:
    last_index = string.lower().rfind("e")
if string.lower().rfind("i") > last_index:
    last_index = string.lower().rfind("i")
if string.lower().rfind("o") > last_index:
    last_index = string.lower().rfind("o")
if string.lower().rfind("u") > last_index:
    last_index = string.lower().rfind("u")

print(f"The index of the last vowel is {last_index}")