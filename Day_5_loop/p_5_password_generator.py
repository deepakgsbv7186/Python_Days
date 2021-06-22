#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# use_letter = ""
# use_number = ""
# use_symbol = ""
gen_pass = ""
for letter in range(1, nr_letters+1):
    gen_pass += random.choice(letters)
# print(use_letter)
for number in range(1, nr_numbers+1):
    gen_pass += str(random.choice(numbers))
# print(use_number)
for symbol in range(1, nr_symbols+1):
    gen_pass += random.choice(symbols)
# print(use_symbol)
# gen_pass = f"{use_letter}{use_number}{use_symbol}"
print(gen_pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# length of generated password
len_of_pass = len(gen_pass)
# convert string to list
create_list = list(gen_pass)
# to change to order of password
# use of random.shuffle function
random.shuffle(create_list)
# now traverse each element from list
# and concatenate all
new_password = ""
for each_char in range(0,len_of_pass):
    new_password += create_list[each_char]
# the password haveing random order with letters, numbers and symbols
print(new_password)