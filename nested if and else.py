height = float(input("Enter your height in m: "))
if height >= 1.5:
    print("you can ride the rollercoaster.")
    age = int(input("Enter your age: "))
    if age < 12:
        print("price is 50.")
    elif age < 20:
        print("price is 100.")
    elif age < 30:
        print("price is 150.")
    elif age < 60:
        print("price is 200.")
    else:
        print("You are free to go.")
else:
    print("You can't ride the rollercoaster.")
print("Thank you for visiting us.")

#excercise 
Number = int(input("Enter a number: "))
if Number == 1 :
    print("number one")
elif Number == 2:
    print("number two")
elif Number == 3:
    print("number three")
elif Number == 4:
    print("number four")
else :
    print("number not found")