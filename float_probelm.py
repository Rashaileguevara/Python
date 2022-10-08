#have the user enter their investment amount and expected interest 
money = input("how much money invest : ")
interest_rate = input('interest rate : ')
money = float(money)
#each year there investment increase by there  investment + there investment * interest rate 
interest_rate = float(interest_rate) * .01
#print out the earning after a 10 year of period 
for i in range(10):
    money = money + (money * interest_rate)
    
print("earning of 10 years period: {:.2f}".format(money))
