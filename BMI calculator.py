#it calculates the bmi of a person using formula(weight/(height**2)).
weight=float(input("What is your weight in Kg?"))
height=float(input("What is your height in meters?"))
bmi_0=weight/(height**2)
bmi= round(bmi_0)
if bmi<18.5:
    print(f"Your BMI is {bmi}, you are Underweight")
elif bmi>18.5 and bmi<25:
    print(f"Your BMI is {bmi}, you have a Normal Weight")
elif bmi>25 and bmi<30:
    print(f"Your BMI is {bmi}, you are Overweight")
elif bmi>30 and bmi<35:
    print(f"Your BMI is {bmi}, you are Obese")
else:
    print(f"Your BMI is {bmi}, you are Clinically Obese")