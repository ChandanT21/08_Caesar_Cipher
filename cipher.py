import string

alphabet = list(string.ascii_lowercase)


def launch():
    mode = input("Type 'encode' to encrypt the message or type 'decode' to decrypt a message.\n").lower()
    if mode == 'encode' or mode == 'decode':
        message = input("Type your message: \n").lower()
        shift_no = int(input("Type the shift number: \n"))
        execute(mode, message, shift_no)
    else:
        print("Incorrect mode selected. Try again.")


def execute(mode, message, shift):
    cipher = ''
    if mode == 'encode':
        cipher = encrypt(message, shift)
    if mode == 'decode':
        cipher = decrypt(message, shift)
    print(f"Here's the {mode}d result:  {cipher}")


def encrypt(message, shift):
    cipher = ''
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            cipher_index = index + shift
            if cipher_index > len(alphabet):
                cipher_index = cipher_index % len(alphabet)
            cipher += alphabet[cipher_index]
        else:
            cipher += letter
    return cipher


def decrypt(message, shift):
    cipher = ''
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            cipher_index = index - shift
            if cipher_index < 0:
                cipher_index = cipher_index % len(alphabet)
            cipher += alphabet[cipher_index]
        else:
            cipher += letter
    return cipher
