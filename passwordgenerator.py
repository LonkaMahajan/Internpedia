import secrets
import string
import pyperclip

# Function to generate a secure random password
def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4")
    
    # Define character sets to use
    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)
    
    if not char_sets:
        raise ValueError("At least one character set must be selected")
    
    # Flatten the list of character sets
    all_chars = ''.join(char_sets)
    
    # Generate a password using the secrets module for secure randomness
    password = ''.join(secrets.choice(all_chars) for _ in range(length))
    
    return password

# Function to generate multiple passwords
def generate_multiple_passwords(count=5, length=12):
    passwords = [generate_password(length=length) for _ in range(count)]
    return passwords

# Display passwords in a user-friendly format
def display_passwords(passwords):
    print("Generated Passwords:")
    for idx, password in enumerate(passwords, 1):
        print(f"{idx}: {password}")

# Function to copy password to clipboard
def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("Password copied to clipboard!")

# Main function to handle user input and generate passwords
def main():
    try:
        count =
