""" ceaser cipher, by gabu
ceaser cipher is a shift cipher that uses addition and subtraction
to encrypt and decrypt letters
"""

try:
    import pyperclip  # pyperclip copies text to clipboard
except ImportError:
    pass  # if pyperclip is not installed,do nothing


SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Ceaser cipher by gabu")
print("the ceaser cipher encrypts letters by shifting them over by a")
print("key number, for example, a key of 2 means the letter A is")
print("encrypted into c, the letter B encrypted into D, and so on")
print()

# let the user entery f they are encrypting or decrypting:
while True:
    print("Do you want to (e)ncrypt or (d)crypt?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("please enter the letter e or d.")


# let the user enter the key to use:
while True:
    maxKey = len(SYMBOLS) - 1
    print("Please enter the key (0 to {}) to use.".format(maxKey))
    response = input("> ").upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# let the user enter the message to encrypt/decrypt
print("Enter the message to {}".format(mode))
message = input("> ")

# caeser cipher only works on uppercase letters
message = message.upper()

# stores the encrypted/decrypted from the message;
translated = ""

# encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        # get the encrypted(or decrypted) no for this symbol
        num = SYMBOLS.find(symbol)  # get the no of the symbol
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

        # handle the wrap-around if num is larger than the length of
        # SYMBOLS or less than 0:
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # add encrypted/decrypted no symbol to translated
        translated = translated + SYMBOLS[num]
    else:
        # just add the symbol without encrypting/decrypting:
        transalted = translated + symbol


# display the encrypted/decrypted string to the screen
print(translated)

try:
    pyperclip.copy(translated)
    print("Full {}ed texte copied to clipboard.".format(mode))
except:
    pass
    # do nothing if pyperclip wasn't installed.
