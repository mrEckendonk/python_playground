# Prints 5 times "This is fun!"

for i in range(5):
  print("This is fun!")

# print is a python function that prints the string that is passed to it.

print("I'm programming in Python!") # text instide ("") is a string.

# Combine strings with + and print them.
name = "Brook"
print ("Hello, " + name + "!")

#  In the following script, change the values of color and thing to have the computer output a different statement than the initial one.

color = "Green"
thing = "grass"
color = "Blue"
thing = "sky"

print(color + " is the color of " + thing)

# Python Can Be Your Calculator
print(4+5)
print(9*7)
print(-1/4)
print(1/3)
print(((2050/5)-32)/9)
# Calculate the power of 2 to the 10th. Below is the code for this.
print(2**10)  # 2*2=4*2=8*2=16*2=32*2=64*2=128*2=256*2=512*2=1024
# Use Python to calculate (((1+2)*3)/4)^5(((1+2)∗3)/4)5
print((((1+2)*3)/4)**5)

ratio = ((1+(5**(1/2)))/2)
print(ratio)

# Define DataTpes
print(type("a"))
print(type(2))
print(type(2.5))

# Variables
# Variables are containers for storing data values.

base = 5    
height = 3  
area = (base*height)/2

print(area)

# Interget and float numbers (Implicit conversion)
print(7+8.5)

# Explicit conversion
base = 6    
height = 3
area = (base*height)/2
print("The area of the triangle is " + str(area))

# Expressions, numbers and Type Conversion
total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))

bill = 47.28
tip = 0.15 * bill
total = bill + tip
share = total/2
print("Each person needs to pay: " + str (share))



def print_seconds(hours, minutes, seconds):
    print(3600*hours+60*minutes+seconds)

print_seconds(1,2,3)

# Return Values
def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2, 30 ,0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

# The Principles of Code Reuse
def month_days(month,days):
    print(month + " has " + str(days) + " days.")
month_days("June","30")
month_days("July","31")

# else Statements
def is_positive(number):
  if number > 0:
    return True
  else:
    return False


# Code Style
# Python is a case sensitive language.
# Refactor the code.

def rectangle_area(base, height):
	z = base*height  # the area is base*height
	print("The area is " + str(z))
rectangle_area(5,6)

# elif Statements
def number_group(number):
   if number > 0:
      return "Positive"
   elif number < 0:
      return "negative"
   else:
      return "zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative


# Conditionals Cheat Sheet
# In earlier videos, we took a look at some of the built-in Python operators that allow us to compare values, and some logical operators we can use to combine values. We also learned how to use operators in if-else-elif blocks. 

# It’s a lot to learn but, with practice, it gets easier to remember it all. In the meantime, this handy cheat sheet gives you all the information you need at a glance. 

# Comparison operators
# a == b: a is equal to b

# a != b: a is different than b

# a < b: a is smaller than b

# a <= b: a is smaller or equal to b

# a > b: a is bigger than b

# a >= b: a is bigger or equal to b

# Logical operators
# a and b: True if both a and b are True. False otherwise.

# a or b: True if either a or b or both are True. False if both are False.

# not a: True if a is False, False if a is True.

# Branching blocks

# In Python, we branch our code using if, else and elif. This is the branching syntax:

# if condition1:
# 	if-block
# elif condition2:
# 	elif-block
# else:
# 	else-block

# Remember: The if-block will be executed if condition1 is True. The elif-block will be executed if condition1 is False and condition2 is True. The else block will be executed when all the specified conditions are false.

x = 0
while x < 5:
  print("Not there yet, x=" + str(x))
  x = x + 1
  # shorthand x += 1
  print("x is now " + str(x))

#   # Python program to check if given  number is power of 2 or not  Function to check if x is power of 2 

#   def is_power_of_two(n):
#   # Check if the number can be divided by two without a remainder
#   while n % 2 == 0:
#     if n == 0 :
#       break;      
#     n = n / 2
# # If after dividing by two the number is 1, it's a power of two
#   if n == 1:
#     return True
#   return False




#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#
  
  

# print(is_power_of_two(0)) # Should be False
# print(is_power_of_two(1)) # Should be True
# print(is_power_of_two(8)) # Should be True
# print(is_power_of_two(9)) # Should be False

# Loops
def factorial(n):
    result = 1
    for x in range(1,n+1):
        result = result * x
    return result

for n in range(1,10):
    print(n, factorial(n))

def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()


#!/bin/python3

import math
import os
import random
import re
import sys



#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#




n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1


smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)


for n in "banana":
    print(n) 

# Slicing!
word = "bananana"
i = word.find("na")

# find domain from email
data = 'From mike.e@vecks.com.br Sat Jan  5 09:14:16 2022'
atpos = data.find('@')
print(atpos)
sspos = data.find(' ', atpos)
print(sspos)
host = data[atpos+1:sspos]
print(host)


# Count down
for i in [5, 4, 3, 2, 1]:
    print(i)
print ('takeoff')