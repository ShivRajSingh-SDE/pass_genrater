#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password_list= []
for char in range(1, nr_letters + 1):
  random_letter= random.choice(letters)
  password_list += random_letter

for char in range(1, nr_symbols + 1):
  random_symbol= random.choice(symbols)
  password_list+= random_symbol

for char in range(1, nr_numbers + 1):
  random_number= random.choice(numbers)
  password_list+= random_number
print(password_list)

random.shuffle(password_list)
print(password_list)

password= ""

for hard_pass in password_list:
  password += hard_pass

print(password)
  
  


  
 

