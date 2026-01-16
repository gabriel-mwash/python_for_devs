""" bitmap message by Gabu
displays a text message according to the provided bitmap image
tags: tiny, beginer, artistic
"""

import sys

# (!) try changing this multiline string to any image you like

# there are 68 periods along the top and bottom of this string:


def replaceBitmap(message: str, bitmapline: str) -> None:
    if message == "":
        sys.exit()
    for bitmapline in bitmapline.splitlines():
        for i, bit in enumerate(bitmapline):
            if bit == " ":
                print(" ", end="")
            else:
                print(message[i % len(message)], end="")
        print()


if __name__ == "__main__":
    print("Enter the message to display with bitmap.")
    message = input("> ")
    with open("./bitmap.txt", "r") as bitmap_file:
        for line in bitmap_file:
            replaceBitmap(message, line)
