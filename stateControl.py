# Python supports module importing. The syntax is as follows:
import random, sys, os, math

# Python also supports multiple imports from a module. The syntax is as follows:
from random import *

# Standard C-based boolean operators apply
# NOTE: Python has strong typing unlike JS, so the === operator does not exist, and 42 == "42" will return false, but 42==42.0 will return true
# Boolean values in Python are capitalized for some reason, so True and False

print(True==True)

# Logical AND and OR are represented by a single ampersand (&) or pipe (|) respectively

print(True | True)
print(True & False)

# Alternatively, you can use the literal words "and" and "or"

print(True or True)
print(True and False)

# If-Else statements are stuctured as follows:
if True==True:
    print("Hooray!")
else:
    print("Boooo")
# IMPORTANT NOTE Python is space sensitive, so if the print statements above were not tabbed in, Python would error and get angry

# Nested If-Else would look something like this:
if True==True:
    if False==False:
        print("Hello!")
    else:
        print("Booo")
else: 
    print("Something else")

# For else-if, Python has the keyword "elif"
if True==False:
    print("WTF")
elif True==True:
    print("Yay!")

# While loops in Python are written with the following structure:
var = 0
while var<3:
    print("While Loop!")
    var+=1
# NOTE: The C Increment "++" and decrement "--" operators do not exist in Python

# Python supports break and continue statements as well
var = 0
while True:
    if var==3:
        break
    else:
        var+=1
        continue

# For loops in Python are written with the following structure:
# This for loop starts at 0 and ends at 2. The equivalent in C would be for(i=0; i<3; i++)
for i in range(3):
    print(str(i))

# This for loop starts at 1 and ends at 2. The equivalent in C would be for(i=1; i<3; i++)
for i in range(1,3):
    print(str(i))

# The third parameter of range is how much it increments each loop. The equivalent in C would be for(i=2; i<6; i+=2)
for i in range(2,6,2):
    print(str(i))

# A way to terminate the Python program before it finishes is by calling sys.exit()
sys.exit()