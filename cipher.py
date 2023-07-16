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
            active = False
        else:
            print("Incorrect mode selected. Try again.")


def execute(mode, message, shift):
    cipher = ''
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            if mode == 'encode':
                cipher_index = index + shift
            else:
                cipher_index = index - shift
            cipher_index = cipher_index % len(alphabet)
            cipher += alphabet[cipher_index]
        else:
            cipher += letter
    print(f"Here's the {mode}d result:  {cipher}")
