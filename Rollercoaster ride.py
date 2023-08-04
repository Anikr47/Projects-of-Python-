#on the basis of height we permit who can ride on not, Ticket Fare are charged on the basis of their age.
print("Welcome to rolercoaster ride")
height=int(input("What is your height in cm "))
bill = 0
if height>=120: 
    print("You can ride the rollercoaster")
    age=int(input("What is your age?"))
    if age<12:
     bill=5
     print("Child tickest are $5.")
    elif age<=18:
     bill=7
     print("Youth tickets are $7.")
    else:
       bill = 12
       print("Adult tickets are $12") 
    wants_photo=input("Do you want to take a photo? Y or N: ")
    if wants_photo=="Y":
     bill+=3
    print(f"Your total bill is {bill}")  
else:
    print("You can't ride the rollercoaster")