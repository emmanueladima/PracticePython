number = int(input("Enter a number to check: "))
check = int(input("Enter a number to divide by: "))

if number % 4 == 0:
    print(str(number) + " is a multiple of 4.")

elif number % 2 == 0:
    print(str(number) + " is an even number.")

else:
    print(str(number) + " is an odd number.")

if number % check == 0:
    print(number, "divides evenly by", check)

else:
    print(number, "does not divide evenly", check)