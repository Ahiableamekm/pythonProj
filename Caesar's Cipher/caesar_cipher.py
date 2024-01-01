import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(f'{art.logo}')


# def encrypt(plain_text, shift_amount):
#     encoded_text = ''
#     for letter in plain_text:
#         old_position = alphabet.index(letter)
#         new_position = (old_position + shift_amount) % 26
#         encoded_letter = alphabet[new_position]
#         encoded_text += encoded_letter
#     print(f'Your encoded text is {encoded_text}')

# def decrypt(encoded_text, shift_amount):
#     decoded_text =''
#     for letter in encoded_text:
#         old_position = alphabet.index(letter)
#         new_position = (old_position - shift_amount) % 26
#         decoded_letter = alphabet[new_position]
#         decoded_text += decoded_letter
#     print(f'Your decoded text is {decoded_text}')



# if direction =="encode":
#     encrypt(plain_text=text, shift_amount=shift)
# else:
#     decrypt(encoded_text=text, shift_amount=shift)


# Refactor the both encode encrypt and decrypt function to be one function

def caesar_cipher(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction =='decode':
        shift_amount = -shift_amount
    for char in start_text:
        if char in alphabet:
            old_position = alphabet.index(char)
            new_position = (old_position + shift_amount) % 26
            end_text += alphabet[new_position]
        else:
            end_text += char
        
    print(f'Your {cipher_direction}d text is {end_text}')

program_restart = True
while program_restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(start_text=text, shift_amount=shift, cipher_direction=direction)
    go_again = input("Type 'yes' if you want to go again. Otherwise type 'no'").lower()
    if go_again == 'no':
        program_restart = False
        print('Goodbye')
