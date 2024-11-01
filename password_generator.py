#create a random password generator
import random

name = input("What is your name")
name = name.upper()
name = name.strip()
print('Welcome '+name+' to your passsword generator')
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
number = "1234567890"
symbols = "!@#$%^&*()_+"
password = lower + upper + number + symbols
password_length = int(input('How many characters would you like?'))
password = random.sample(password, password_length )
print ( "Your password is " + "".join(password))
