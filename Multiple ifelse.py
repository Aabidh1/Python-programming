name = input("Enter your name: ")
age = int(input("Enter your age: "))
photo = input("Do you want a photo ? (yes/no): ")

if age < 18:
    if photo == "yes":
        print("You need to pay 200")
    else:
        print("You need to pay 100")
elif age >= 18 and age < 60:
    if photo == "yes":
        print("You need to pay 250")
    else:
        print("You need to pay 150")
else:
    if photo == "yes":
        print("You need to pay 300")
    else:
        print("You need to pay 250")