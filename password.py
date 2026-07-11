import random
import string

print("========== PASSWORD GENERATOR ==========")

length = int(input("Enter the password length: "))

print("\nChoose Password Type")
print("1. Easy (Letters)")
print("2. Medium (Letters + Numbers)")
print("3. Strong (Letters + Numbers + Symbols)")

option = input("Enter your choice (1/2/3): ")

password = ""

for i in range(length):

    if option == "1":
        password += random.choice(string.ascii_letters)

    elif option == "2":
        category = random.randint(1, 2)

        if category == 1:
            password += random.choice(string.ascii_letters)
        else:
            password += random.choice(string.digits)

    elif option == "3":
        category = random.randint(1, 3)

        if category == 1:
            password += random.choice(string.ascii_letters)
        elif category == 2:
            password += random.choice(string.digits)
        else:
            password += random.choice("!@#$%^&*()_-+=<>?")

    else:
        print("Invalid choice!")
        exit()

print("\nYour Generated Password is:")
print(password)