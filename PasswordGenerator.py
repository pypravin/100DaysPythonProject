# Password Generator Project
import random as rand
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
new_letter = ""
new_symbol = ""
new_number = ""
new_pass = " "
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
for char in range(1, nr_letters + 1):
    new_letter = rand.choice(letters)
    new_pass += new_letter
for num in range(1, nr_numbers + 1):
    new_number = rand.choice(numbers)
    new_pass += new_number
for char in range(1, nr_symbols + 1):
    new_symbol = rand.choice(symbols)
    new_pass += new_symbol
hash_pass = new_pass.__hash__()
new_pass = new_pass
print(f"Your new Password is: {new_pass}")
print(f"Your new HashedPassword is:{hash_pass}")

