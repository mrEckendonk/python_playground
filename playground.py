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

# Code Style
# Python is a case sensitive language.
# Refactor the code.

def rectangle_area(base, height):
	z = base*height  # the area is base*height
	print("The area is " + str(z))
rectangle_area(5,6)
