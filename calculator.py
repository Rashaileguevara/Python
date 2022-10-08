#store 2 values and operators
from ast import operator


num1, operator, num2 = input('enter the calculation ').split()
#convert the string to integers
num1 = int(num1)
num2 = int(num2)
#if + then we need an output for addition and the same for other operators 
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1 - num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print ("use + - * or / next time")
#print the result 
