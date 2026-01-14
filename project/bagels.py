""" bagels by gabu
a deductive logic game where you must guess a no based on clues
"""

import random
NUM_DIGITS = 3
MAX_GUESSES = 10


def main() -> None:
    print("""Bagles, a deductive logic game.
          I am thinking of a {}-digit no with no repeated digits
          Try to guess what it is. Here are some clues:
          when I say:       that means
          Pico              one digit correct, but wrong position
          Fermi             one digit correct,  right position
          Bagels            no digit correct

          eg if the secrete no is 248 and you guessed 843, the clue would
          be Fermi Pico """.format(NUM_DIGITS))

    while True:
        # stores the secret no the player needs to guess
        secretNum = getSecretNum()
        print(" I have thought of a number. ")
        print("You have {} guesses to get it ". format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ""
            # keep looping until they enter a vlid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}: ".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # we have a correct guess, so break
            if numGuesses > MAX_GUESSES:
                print("you ran out of guesses.")
                print("the answer was {}".format(secretNum))
        print("do you want to play again? (yes or no)")
        if not input("> ").lower().startswith("y"):
            break
    print("Thanks for playing!")


def getSecretNum():
    """ returns a string made up of NUM_DIGITS unque random digits"""
    numbers = list("0123456789")
    random.shuffle(numbers)

    # get the first NUM_DIGITS digits in the list for secret no.
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess, secretNum):
    """ return a string with the pico, fermi, bagels clues for a guess
    and secret number pair."""
    if guess == secretNum:
        return "you got it!"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # a correct digit in the correct place
            clues.append("Fermi")
        elif guess[i] in secretNum:
            # correct digit but wrong place
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
