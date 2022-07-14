#Caesar Cipher: An encryption program
#Encoding Stage
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text, shift_amount):
    encoded_text = ""
    for letter in plain_text:
        position = alphabet.index(letter) # This was used to get the position of each letter in the alphabet
        position += shift_amount
        # As usual I went for the bogus over complex solution
        # The easier way to go if the position is greater than the number of alphabets...
        # ...is to duplicate the alphabets in the list
        if position > len(alphabet):
            new_position = len(alphabet) - alphabet.index(letter) # Used this to catch the extra letters that might remain
            final_position = shift_amount - new_position # Used this to get the letter to be added from the start of the alphabet
            encoded_text += alphabet[final_position]
        else:
            encoded_text += alphabet[position]
    print(f"The encoded text is {encoded_text}.")
    
 
encrypt(plain_text=text, shift_amount=shift)
# A modified version would be made for the less bulky code
# The mod would be used going further