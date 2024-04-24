import string

# Library
alphabet = string.ascii_lowercase
numbers = string.digits
punc = string.punctuation

def start():
    text = input('Insert text to be encrypted: \n')
    cipher = input('Would you like to use the Caesar or Vigenere cipher\n')
    return text,cipher
lib = start()

def direction():
    # Choose if you want the cipher to encrypt or decrypt your message.
    value = input('Input 0 to encrypt, 1 to decrypt:\n')
    if int(value) == 0:
        return 1
    elif (value) == 1:
        return -1
    else:
        print('check your input')
        direction()
dire = direction() 

def caesar(message = lib[0], direction = dire):
    final_message = ''
    step = int(input('Input the step for the cipher: \n'))
    for char in message:
        if not char.isalpha():
            final_message += char
        else:
            char_index = alphabet.find(char)
            new_index = (char_index + step * direction) % len(alphabet)
            new_char = alphabet[new_index]
            final_message += new_char
    print(final_message)

def vigenere(message = lib[0], direction=dire):
    key_index = int(input('Specify Index Number: \n'))
    key = input('Specify custom key: \n')
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        elif char in numbers or char in punc:
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = int(alphabet.index(key_char))
            index = alphabet.find(char)
            new_index = (index + offset * int(direction)) % len(alphabet)
            final_message += alphabet[new_index]
    
    print(final_message)

def choice():
    # Choose the cipher you want to use.
    if lib[1] == 'caesar':
        caesar()
    elif lib[1] == 'vigenere':
        vigenere()
    else:
        print('Check the spelling of your cipher input (Caesar / Vigenere)')
        start()
choose = choice()


start()
