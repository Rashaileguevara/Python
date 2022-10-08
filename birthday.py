#we will provide different out put based on birthday
# 1 - 18 -> important 
# 21, 50 and < 65 -> important 
#others are not important 
age = eval(input("Enter your age: "))

#and if both are true will result true 
#or if either is true result true 
#not converts true condition to false condition and vice versus 
if (age >= 1) and (age <= 18):
    print("Important birthday")
elif (age == 21) or (age == 50):
    print("Important birthday")
elif not (age > 65):
    print("Important birthday")
else:
    print("sorry it is not important")


#if age is both greater than or equal to 1 and less than or equal to 18 it is important 
#if age is either 21 or 50 it is important 
#if age is less than 65 the true is false and vice verse 
#else not important 
