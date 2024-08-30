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



# Python Input function

# input() function is used to take input from the user.

name = input("What is your name? ") # input() function takes a string as an argument which is displayed to the user.

print("Hello " + name) # prints Hello followed by the name entered by the user.

age = input("How old are you? ") # input() function takes a string as an argument which is displayed to the user.

print("You are " + age + " years old") # prints You are followed by the age entered by the user.

birth_year = input("Enter your birth year: ") # This input() function is creating a variable for the year of birth.

age = 2024 - int(birth_year) # This line of code is calculating the age by subtracting the birth year from the current year and converting the result to an integer.

print(age)

# For converting values in variables.

# int() function is used to convert a string to an integer.

# float() function is used to convert a string to a float.

# str() function is used to convert a number to a string.

# bool() function is used to convert a number to a boolean.


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



# Functions in Python

# Functions are blocks of code that are designed to do one job. They are executed when they are called.


# Activity 1

# Write an If Statement that checks if the items on the top row meet the winning condition.

space1 = "X"
space2 = "X"
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

if space1 == space2 == space3:
    print("Winner")
else:
    print("No Winner")

if space1 and space2 and space3 == "X":
    print("Winner")
elif space1 and space2 and space3 == "O":
    print("Winner")
else:
    print("No Winner")


# Activity 2

# Write an If Statement that checks the age of a cinema goers, and display the ticket prices:

age = int(input("How old are you? "))

if age < 18:
    print("Child Ticket price £8")
elif age > 60:
    print("Senior Ticket price £7.50")
else:
    print("Adult Ticket price £10.95")
    


# Functions can be called multiple times and can be reused in different parts of the code.

# function_name(parameters)

# some functions are already defined

# print() function is used to print a message to the console.

# input() function is used to take input from the user.

# len() function is used to return the length of a string.

# lower() method is used to convert a string to lowercase.


# def press_grind_beans():
#     print("Grinding for 20 seconds")

# press_grind_beans()



# Parameters are used to pass information

# def cash_withdrawal(amount, accnum):
#     print(f"Withdrawing £{amount} from account number {accnum}")

# cash_withdrawal(300, 50449921)

# This will print Withdrawing £300 from account number 50449921


# def cash_withdrawal(amount, accnum):
#     print(f"Withdrawing £{amount} from account number {accnum}")

# cash_withdrawal(300, 50449921)
# cash_withdrawal(30, 50449921)
# cash_withdrawal(200, 50449921)

# This will print 3 lines of text with the amount and account number.





# Activity 3

# Create a function that takes two parameters for a coffee order (size, type of drink) and prints them out in a sentence.

def coffee_order(size, drink):
    print(f"You have ordered a {size} {drink}")
    print("    (  )   (   )  )")
    print("     ) (   )  (  (")
    print("     ( )  (    ) )")
    print("     _____________")
    print("    <_____________> ___")
    print("    |             |/ _ \ ")
    print("    |              | | |")
    print("    |              |_| |")
    print(" ___|             |\___/")
    print("/    \___________/    \ ")
    print("\_____________________/")
    
coffee_order("large", "latte")




# Challenge 1

# order_count = 0

# def take_order(topping):
#     global order_count
#     print("Pizza with {}".format(topping))
#     order_count += 1

# take_order("Pineapple")

# Edit the snippet above to include two or more parameters, a running order count that updates when the function is called and change the .format method to f string.

order_count = 0

def take_order(topping, size):
    global order_count
    print(f"Pizza with {topping} {size}")
    order_count += 1

take_order("Pineapple", "large")
take_order("Pepperoni", "small")
take_order("Mushroom", "medium")

print(order_count)

# three parameters

order_count = 0

def take_order(topping, size, price):
    global order_count
    print(f"Pizza with {topping} {size} {price}")
    order_count += 1

take_order("Pineapple", "large", "£10")
take_order("Pepperoni", "small", "£7")
take_order("Mushroom", "medium", "£8")

print(order_count)

# added order count to the print statement

order_count = 0+1

def take_order(topping, size, price):
    global order_count
    print(f"Pizza with {topping} {size} {price} you are order {order_count}")
    order_count += 1

take_order("Pineapple", "large", "£10")
take_order("Pepperoni", "small", "£7")
take_order("Mushroom", "medium", "£8")

print(order_count)


# Challenge 2

# Cash Machine takes an input of pin number and amount to withdraw. Print "Dispensing £{amount}" if the pin is correct and there is enough money and displays the new bank balance.

# def cash_machine(pin, amount):
#     if pin == 1234 and amount <= 100:
#         print(f"Dispensing £{amount}")
#     else:
#         print("Incorrect pin or insufficient funds")

# cash_machine(1234, 50)
# cash_machine(1235, 200)
# cash_machine(5234, 150)
# cash_machine(1234, 150)


pin = 1234
pincode = int(input("Enter your pin: "))
balance = 100
cash_request = int(input("How much would you like to withdraw? "))
new_balance = balance - cash_request


def cash_machine(pin, amount):
    if pincode == pin and amount <= balance:
        print(f"Dispensing £{amount}")
        print(f"Your new balance is £{new_balance}")
    else:
        print("Incorrect pin or insufficient funds")

cash_machine(pin, cash_request)


# Extra Reading - Return

# Return is used to return a value from a function.

# def add(num1, num2):
#     return num1 + num2


# result = add(10, 5)

# print(result)

# # This will print 15 as the function returns the sum of the two numbers.


# def add_up(num1, num2):
#   return num1 + num2


# result = add_up(7, 3) # This will return 10 but without printing it to the console.
# print(add_up(2, 5)) # This will return 7 and print it to the console.


def multiply_by_nine_fifths(celsius):
    return celsius * (9/5)

def get_fahrenheit(celsius):
    return multiply_by_nine_fifths(celsius) + 32

print(f"The temperature is {get_fahrenheit(15)}°F") # This will print The temperature is 59.0°F



# Global and local variables

# Global variables are variables that are defined outside of a function and can be accessed by any function in the code.

# Local variables are variables that are defined inside a function and can only be accessed by that function.

# f = 0

# def some_function():
#     f = 1
#     return f

# print(f) # This will print 0 as the global variable f is accessed.

# print(some_function()) # This will print 1 as the local variable f is accessed.

# print(f) # This will print 0 as the global variable f is accessed.




# Coffee Machine

coffee_is_grinding = False

def press_grind_beans():
    global coffee_is_grinding
    if coffee_is_grinding:
        print("Stopping the grind")
        coffee_is_grinding = False
    else:
        print("Grinding is in progress")
        coffee_is_grinding = True
        
press_grind_beans() # This will print Grinding is in progress
press_grind_beans() # This will print Stopping the grind





# Libraries in Python are collections of functions and methods that allow you to perform many actions without writing your own code.


import random

print(random.random()) # This will print a random number between 0 and 1.

print(random.uniform(1, 10)) # This will print a random number between 1 and 10.

print(random.randint(1, 10)) # This will print a random integer between 1 and 10.

print(random.choice(["rock", "paper", "scissors"])) # This will print a random item from the list.



from random import random, randint, uniform

print(random()) # This will print a random number between 0 and 1.
print(uniform(1, 10)) # This will print a random number between 1 and 10.
print(randint(1, 10)) # This will print a random integer between 1 and 10.













