#if age is 5 go to kindergarten
#ages 6 through 17 goes to grade 1 through 12
#if age is greater than 17 say go to college 
age = eval(input("Enter age: "))
if (age < 5):
    print("Go to young school")
elif (age == 5):
    print("Go to kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to grade {}".format(grade))
else:
    print("Go to college")
