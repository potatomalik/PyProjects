print('Welcome to the tip calculator.')
bill_amount=float(input("What was the total bill? $"))
tip=int(input('What percentage tip would you like to give? 10, 12, or 15? '))
people=int(input('How many people to split the bill? '))
total=bill_amount+((tip*bill_amount)/100)
pay=total/people
print('Each person should pay: $',round(pay,2))