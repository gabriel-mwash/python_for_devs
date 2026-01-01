from typing import TextIO
from io import StringIO

def process_file(reader: TextIO) -> int:
    line = reader.readline()

    line = reader.readline()
    while line.startswith("#"):
        line = reader.readline()

    # now line contains the first real piece of data
    # the largest value seen so far in the current line

    largest = -1

    for value in line.split():
        # remove the trailing period
        v = int(value[:-1])
        if v > largest:
            largest = v

    # check the rest of the lines for larger values
    for line in reader:
        # the largest value seen so far in the current line
        largest_in_line = -1

        for value in line.split():

            # remove the trailing period
            v = int(value[:-1])

            # if we find a larger value, remember it
            if v > largest_in_line:
                largest_in_line = v
        if largest_in_line > largest:
            largest = largest_in_line
    return largest

if __name__ == "__main__":
    with open("lynx.txt", "r") as input_file:
        print(process_file(input_file))

    
