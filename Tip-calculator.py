
#tip-calculator and shows the bill after splitting among people
print("Welcome to the tip calculator")
bill=float(input("What was the total bill? $"))
tip_percentage=int(input("What percentage tip would like to give? 10, 12, or 15?"))
tip_amount=bill*(tip_percentage/100)
total_bill=bill+tip_amount
people=int(input("How many people to split the bill?"))
amount_per_person=total_bill/people
amount_per_person="{:.2f}".format(amount_per_person)
print("Each person should pay:",amount_per_person)
