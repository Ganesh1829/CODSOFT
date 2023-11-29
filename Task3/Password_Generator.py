import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        try:
            password_length = int(input("Enter the length of the password: "))
            if password_length <= 0:
                print("Please enter a valid positive length.")
                continue
            generated_password = generate_password(password_length)
            print(f"Your generated password is: {generated_password}")
            break
        except ValueError:
            print("Please enter a valid number for the password length.")
