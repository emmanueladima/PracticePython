import random as rd

def guess_number():
    num = str(rd.randint(1000,9999))
    while True:
        user_num = input("Enter a 4 digit number (or type 'exit' to quit): ").lower()
        if user_num == 'exit':
            print(f'The number was {num}. Goodbye!')
            break

        if len(user_num) != 4 or not user_num.isdigit():
            print("Please enter a valid 4-digit number.")
            continue

        cows = 0
        bulls = 0

        for i in range(4):
            if user_num[i] == num[i]:
                cows += 1
            elif user_num[i] in num:
                bulls += 1

        print(f'{cows} cows, {bulls} bulls!')

        if cows == 4:
            print(f"Congratulations! You guessed the number {num}!")
            break       

if __name__ == "__main__":
    guess_number()


