import string

alphabet = list(string.ascii_lowercase)


def launch():
    active = True
    while active:
        mode = input("Type 'encode' to encrypt the message or type 'decode' to decrypt a message.\n").lower()
        if mode == 'encode' or mode == 'decode':
            message = input("Type your message: \n").lower()
            shift_no = int(input("Type the shift number: \n"))
            execute(mode, message, shift_no)
            if (input("Type 'yes' if you want to go again, otherwise type 'no'.\n")) == 'no':
                active = False
        else:
            print("Incorrect mode selected. Try again.")


def execute(mode, message, shift):
    if mode == 'encode':
        cipher = encrypt(message, shift)
        print(f"Here's the encoded result:  {cipher} ")
    if mode == 'decode':
        cipher = decrypt(message, shift)
        print(f"Here's the decoded result:  {cipher}")


def encrypt(message, shift):
    cipher = ''
    for letter in message:
        if letter == " ":
            cipher += " "
        else:
            index = alphabet.index(letter)
            cipher_index = index + shift
            if cipher_index > len(alphabet):
                cipher_index = cipher_index % len(alphabet)
            cipher += alphabet[cipher_index]
    return cipher


def decrypt(message, shift):
    cipher = ''
    for letter in message:
        if letter == " ":
            cipher += " "
        else:
            index = alphabet.index(letter)
            cipher_index = index - shift
            if cipher_index < 0:
                cipher_index = cipher_index % len(alphabet)
            cipher += alphabet[cipher_index]
    return cipher
