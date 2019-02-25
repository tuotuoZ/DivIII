__author__ = 'tony'
import numpy as np

# name = input("Please enter your name ")
# greeting = "Hello"
# print(greeting + ' ' + name)

splitString = "This string has been\nsplit over\nserveral\nlines"
print(splitString)
a = 12
b = 3
print(a // b)
print(a / b)
print(a % b)
print(splitString[:6])
print(splitString[-4:-2])
print("num"[1])

print("hello " * 5 )
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "January", "March", "May", "April", "May", "June", "July"))

print("""
January: {2}
Feb: {0}
March: {1}
April: {2}
May: {0}


""".format(28, 30 ,31))

for i in range(1, 13):
    print("No. {0:2} squared is {1:2} and cubed is {2:<4}".format(i, i **2, i **3))
for i in range(1, 13):
    print("No. %2d squared is %4d and cubed is %d" %(i, i **2, i **3))

print("Pi is nearly %1.50f" % ( 22 /7))