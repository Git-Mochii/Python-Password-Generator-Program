import random

# Define sets of characters to use for random password
numbers = '0123456789' 
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
higher_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols = '!@#$%^&*()_-=+[]{}<>,.?/\\|~'

# Selected options for password generation
use_higher_letters = True
use_lower_letters = True
use_numbers = True
use_symbols = True

# Pool of characters based on selection (Character pool is used for collecting various characters to use in password generation) 
pool = ""
if use_higher_letters: 
    pool += higher_letters
if use_lower_letters:
    pool += lower_letters
if use_numbers:
    pool += numbers
if use_symbols:
    pool += symbols

# Password length + Amount of passwords to generate
password_length = 15
password_generated = 5

# Generate random passwords and print into console 

print("///////////////////////")
print("Generating Passwords...")
print("/////////////////////// \n")

for i in range(password_generated): # Loop through password_generated times to generate password 
    password = "".join(random.choice(pool) # Generate random password based on pool of characters 
for i in range(password_length)) # Loop through password_length times to generate password 
    print(f"Password/s Generated: {password}") # Print password/s to console

print("\n ///////////////////////")
