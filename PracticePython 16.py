import string
import random as rd

def generate_password():

    while True:
        user = input('Do you want to generate a password? (yes/no): ').strip().lower()

        if user == 'yes':
            level = input('Choose a password strength (weak, medium, strong): ').strip().lower()

            if level == 'weak':
                chars = string.ascii_lowercase + string.digits
                password_length = rd.randint(3, 8)
            elif level == 'medium':
                chars = string.ascii_letters + string.digits
                password_length = rd.randint(6, 13)
            elif level == 'strong':
                chars = string.ascii_letters + string.digits + string.punctuation
                password_length = rd.randint(10, 20)
            else:
                print("Invalid strength level. Defaulting to strong.")
                chars = string.ascii_letters + string.digits + string.punctuation
                password_length = rd.randint(10, 20)

            print("Generating a password...")
            password = ''.join(rd.choice(chars) for n in range(password_length))
            print("Generated password:", password)
        
        elif user == 'no':
            print("Password generation cancelled. Goodbye!")
            break

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        
generate_password()
