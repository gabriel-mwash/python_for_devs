from typing import TextIO
from io import StringIO


def skip_header(reader: TextIO) -> str:
    # read the description line
    line = reader.readline()

    # find the first non-comment line
    line = reader.readline()
    while line.startswith("#"):
        line = reader.readline()

    # now line contains the first real piece of data

    return line

def process_file(reader: TextIO) -> None:
    """ read and print the data from reader, which must start with a single
    description line, then a sequence of lines beginning with #, then a
    sequence of data.
    """

    line = skip_header(reader).strip()
    print(line)

    # read the rest of the data
    for line in reader:
        if not line == " ":
            line = line.strip()
            print(line)
        


def smallest_value(reader: TextIO) -> int:
    """ Read and process reade and return the smallest value after the
    time_series header.

    """
    line = skip_header(reader).strip()

    # now line contains the first data val, this is also the smallest val
    # found so far, coz its the only one we have seen

    smallest = int(line)
    for line in reader:
        value = int(line.strip())

        # if we find a smaller value, remember it.
        if value > smallest:
            continue
        smallest = value
    return smallest

if __name__ == "__main__":
    with open("hopedale.txt", "r") as input_file:
        print(smallest_value(input_file))

