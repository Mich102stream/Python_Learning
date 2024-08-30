# Description: A simple calculator that takes two numbers and an operation as input and returns the result of the operation.

First = float(input("Enter the first number: ")) # input() method is used to take input from the user.
Second = float(input("Enter the second number: ")) # input() method is used to take input from the user.
calc = input("Enter the operation: ") # input() method is used to take input from the user.

if calc == "+":
    sum = First + Second # if the operation is addition then add the first number to the second number.
elif calc == "-":
    sum = First - Second # if the operation is subtraction then subtract the second number from the first number. 
elif calc == "*":
    sum = First * Second # if the operation is multiplication then multiply the first number by the second number.
elif calc == "/":
    sum = First / Second # if the operation is division then divide the first number by the second number.
else:
    sum = "Invalid operation" # if the operation is not one of the above then print "Invalid operation".

print(sum) # print the result of the operation.
