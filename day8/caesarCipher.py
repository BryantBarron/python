
from ssl import ALERT_DESCRIPTION_HANDSHAKE_FAILURE
import art

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

""" def cipher_encrypt(message, shift):
    encrypted_message = ""
    for i in message:
        if i == " ":
            encrypted_message += " "
        else:
            letter = alphabet.index(i) + shift
            if(letter >= 26):
                cycle = letter - 26
                shifted_letter = alphabet[cycle]
                encrypted_message += shifted_letter
            else:
                shifted_letter = alphabet[letter]
                encrypted_message += shifted_letter
    
    return encrypted_message

def cipher_decrypt(message, shift):
    decrypted_message = ""
    for i in message: 
        letter = alphabet.index(i) - shift
        if(letter <= 0):
            cycle = letter + 26
            shifted_letter = alphabet[cycle]
            decrypted_message += shifted_letter
        else:
            shifted_letter = alphabet[letter]
            decrypted_message += shifted_letter
    
    return decrypted_message """

def caesar(message, shift, direction):
    final_message = ""
    if direction == "decode":
        shift *= -1
    for char in message:
        if char in alphabet:
            letter = alphabet.index(char)
            shifted_letter = letter + shift
            final_message += alphabet[shifted_letter]
        else:
            final_message += char
    print(f"The {direction}d text is the {final_message}")
        

print(art.logo)
repeat = False
while not repeat:
    direction = input(
        "Would you like to encode, or decode? Type (encode/decode): ")
    shift = int(input("Please enter a number for the number of shifts: "))
    word = input("Please enter the word you would like encode or decoded: ")

    shift = shift % 26
    caesar(word, shift, direction)

    restart = input("Type yes/no if you would like to run again. ").lower()
    if restart == "no":
        repeat = True
        print("GoodBye.")



