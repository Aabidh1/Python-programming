name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 18:
    bill = 100
    print("You need to pay 100")
elif age >= 18 and age < 60:
    bill = 150
    print("You need to pay 150")
else:
    bill = 200
    print("You need to pay 200")

photo = input("Do you want a photo ? (yes/no): ")
if photo == "yes":
    bill += 50

print(bill , "You need to pay 50 extra for photo")