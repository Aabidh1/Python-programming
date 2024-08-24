print(5+2)
print(5**2)
print(5-2)
print(5/2)
print(5//2) # floor division rounding value
print(5%2) # modulo
print(5*2)
print(round(2.675, 2)) # round to 2 decimal places
#excersie calculate BMI
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight/(height**2)
print("Your BMI is: ", round(bmi))