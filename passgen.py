import random
import string
import pyperclip

def generate_password(length=20):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    generated_password = generate_password()
    
    # Copy the generated password to clipboard
    pyperclip.copy(generated_password)
    
    # Print the generated password
    print("Generated Password:", generated_password)
    
    # Notify the user
    print("Password copied to clipboard.")
