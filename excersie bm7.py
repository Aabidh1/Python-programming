weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(height**2)
if bmi < 16 :
    print("You are severely underweight")
elif bmi >= 16 and bmi < 16.9:
    print("You are underweight")
elif bmi >= 17 and bmi < 18.4:
    print("You are mildly underweight")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are normal")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight")
elif bmi >= 30 and bmi < 34.9:
    print("You are moderately obese")
elif bmi >= 35 and bmi < 39.9:
    print("You are severely obese")
else:
    print("You are very severely obese")