# Initialization

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Creating Functions
def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        position += shift_amount
        encoded_text += alphabet[position]
    print(f"The encoded text is {encoded_text}.")


def decrypt(cipher_text, shift_amount):
    decoded_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        position -= shift_amount
        decoded_text += alphabet[position]    
    print(f"The decoded text is {decoded_text}")


if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
else:
    print("You have made an invalid entry")