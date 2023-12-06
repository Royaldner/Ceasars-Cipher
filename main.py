def encryption(letters, shifts):
    result = ""
    for i in range(len(letters)):
        char = letters[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) + shifts - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shifts - 97) % 26 + 97)
        else:
            result += char
    return result


def decryption(letters, shifts):
    result = ""
    for i in range(len(letters)):
        char = letters[i]
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - shifts - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shifts - 97) % 26 + 97)
        else:
            result += char
    return result


def decipher(message):
    shifter = 0
    while shifter <= 25:
        possibles = decryption(message, shifter)
        print("shift", shifter, possibles)
        shifter = shifter + 1

keepRunning = True
while keepRunning == True:
    print("WELCOME TO CRYPTOGRAPHY")
    print("Ceasar's Cipher")
    do = input("type 1 - encrypt\ntype 2 - decrypt\ntype 3 - decipher\nENTER YOUR CHOICE HERE: ")
    if do == "1":
        message = input("Enter a message to Encrypt: ")
        shift = int(input("Enter shift value: "))
        encrypted_message = encryption(message, shift)
        print("Original Message:", message)
        print("Encrypted Message:", encrypted_message)
    elif do == "2":
        message = input("Enter a message to Decrypt: ")
        shift = int(input("Enter shift value: "))
        decrypted_message = decryption(message, shift)
        print("Original Message:", message)
        print("Decrypted Message:", decrypted_message)
    elif do == "3":
        message = input("Enter a message to Decipher: ")
        decipher(message)
    else:
        print("not a valid value")
    reRun = input("Do you want to try again Y/N: ")
    if reRun.capitalize() == "N":
        keepRunning = False








