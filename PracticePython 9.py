import random

rnd_number = random.randint(1,9)
number = 0
c = 0

while number != rnd_number and number != "exit":

    number = input("Enter a number: ")

    if number.lower() == "exit":
        break

    number = int(number)
    c += 1

    if rnd_number == number:
        print(str(number) + ' is the correct answer!')
        print('Only took you', c, 'tries!')

    elif rnd_number > number:
        print(str(number) + ' is too low of a guess!')
        print('Try again!')

    else:
        print(str(number) + ' is too high of a guess!')
        print('Try again!')