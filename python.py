#ask a user to input there name and assign it to a variable name
name = input ("what is your name ")
#print out hello followed by the name entered 
print("hello ", name)
#ask a user to input 2 values and store them in variable num 1 and num 2
num1, num2 = input("Enter 2 numbers: ").split()
#convert the strings into regulars number integers
num1 = int(num1)
num2 = int(num2)
#add the value entered and stored sum 
sum = num1 + num2
#subtract the value and stored the difference 
difference = num1 - num2
#multiply the value and stored the product 
product = num1 * num2
#divide the value and stored the quotient 
quotient = num1 / num2
#divide the module and stored the reminder 
reminder = num1 % num2
#print the result 
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, reminder))
