name = input("what is your name :")
age = int(input("what is your age :"))
if age < 18:
    print("You are not eligible to vote")
elif age >= 18 and age < 21:
    print("You are eligible to vote but not eligible to drink")
else:
    print("You are eligible to vote and drink")
print("Thank you", name)