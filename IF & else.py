name = input("What is your name? ")
age = int(input("What is your current age? "))
if age < 18:
    print(f"Sorry {name}, you are not eligible to vote.")
else:
    print(f"Congratulations {name}, you \n are eligible to vote.")