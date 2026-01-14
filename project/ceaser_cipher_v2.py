def encryptionData() -> tuple[str, str, int]:
    "return the mode, message, key"
    while True:
        print("Do you want to (e)ncrypt or (d)crypt")
        response = input("> ").lower()
        if response.startswith("e"):
            mode = "encrypt"
            break
        elif response.startswith("d"):
            mode = "decrypt"
            break
        else:
            print("please enter e to encrypt, or d to decrypt")

    while True:
        print(f"Enter the key (0 to {len(ALPHABET)} to use)")
        key = input("> ")
        if not key.isdecimal():
            continue
        if 0 <= int(key) <= len(ALPHABET):
            key = int(key)
            break
        else:
            continue
    print(f"Enter the message to {mode}")
    message = input("> ")
    return (mode, message, key)


def encrypt(ALPHABET: str, info: tuple) -> str:
    """ encrypt with the given info"""
    message, key = info
    encrypted_message = ""
    for symbol in message.upper():
        position_of_symbol = ALPHABET.find(symbol)
        position_of_cipher = position_of_symbol + key

        if position_of_cipher > len(ALPHABET):
            position_of_cipher = position_of_symbol - len(ALPHABET)
            encrypted_message = encrypted_message + ALPHABET[position_of_cipher]

        encrypted_message = encrypted_message + ALPHABET[position_of_cipher]
    return encrypted_message.upper()


def decrypt(ALPHABET: str, info: tuple) -> str:
    """ decrypt with the given info"""
    message, key = info
    decrypted_message = ""
    for symbol in message.upper():
        position_of_symbol = ALPHABET.find(symbol)
        position_of_cipher = position_of_symbol - key

        if position_of_cipher < 0:
            position_of_cipher = position_of_symbol + len(ALPHABET)
            decrypted_message = decrypted_message + ALPHABET[position_of_cipher]

        decrypted_message = decrypted_message + ALPHABET[position_of_cipher]
    return decrypted_message


# print(encryptionData())

if __name__ == "__main__":
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mode, message, key = encryptionData()
    if mode == "encrypt":
        encrypted_message = encrypt(ALPHABET, (message, key))
        print("the encrypted message is {}".format(encrypted_message))
    else:
        decrypted_message = decrypt(ALPHABET, (message, key))
        print("the decrypted message is {}".format(decrypted_message))
