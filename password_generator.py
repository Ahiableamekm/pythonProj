# This is a biginner joect that will generate password 
# considering a user preference of the number of letters, symbols and numbers 
# that can be in the password

#  import random module to help in randomly selecting characters for the password
import random


#  create a list of alphabets, numbers and symbols from which the password will be generated from.
#  string module can be used instead of manually creating the alphabet list
alphabetsl = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetsu = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', "Z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_']


# print a welcome message to the output
print("Welcome to Pypassword Generator🔐")

#  Ask the user how many letters they want in their password
count_letters = int(input("How many letters do you want in your password?: "))

# Ask the user how many numbers they want in their password
count_numbers = int(input("How many numbers do you want in your password?: "))

# Ask the user how many symbol they want in their password
count_symbols = int(input("How many symbols do want in your password?: "))


# combine both uppercase and lowercase and shuffle them
combine_letters = alphabetsl + alphabetsu
random.shuffle(combine_letters)

# create an empty list to hold the random letters to be selected
password_letter_list = []

# create a loop the numner of letter times to select random letters 
# choice method from the random module can be used instead of randint and indexing
for letter in range(count_letters):
    random_letter_number = random.randint(0, len(combine_letters)-1)
    random_letter = combine_letters[random_letter_number]
    password_letter_list.append(random_letter)


# create an empty list to hold the random numbers to be selected
password_number_list = []

# create a loop to generate the number times to generate a random number for the password
for number in range(count_numbers):
    random_number = random.randint(0, 9)
    password_number_list.append(str(random_number))

# create an empty list to hold the random symbols to be selected
password_symbol_list = []

# create a loop to generate the number times a symbols to be selectd for the password.
for symbol in range(count_symbols):
    random_symbol_letter = random.randint(0, len(symbols)-1)
    random_symbol = symbols[random_symbol_letter]
    password_symbol_list.append(random_symbol)


# combine the random letter, number and symbol list togther and shuffle it
combined_password_list = password_letter_list + password_number_list + password_symbol_list
random.shuffle(combined_password_list)

# join all the letters together with no space in between
password = "".join(combined_password_list)
print(f"Here is your password: {password}")
