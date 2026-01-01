from typing import TextIO
import time_series


def smallest_value(reader: TextIO) -> int:
    """ read and process reader and return the smallest value after the
    time_series header.

    >>> infile = StringIO("Example\\n1\\n2\\n3\\n")
    >>> smallest_value(infile)
    1
    >>> infile = StringIO("Example\\n3\\n1\\n2\\n")
    >>> smallest_value(infile)
    1
    """

    line = time_series.skip_header(reader).strip()

    # now line contains the first data value; this is also the smallest value
    # found so far, because it is the only one we have seen

    smallest = int(line)

    for line in reader:
        value = int(line.strip())

        # if we find a smaller value, remember it.
        
        smallest = min(smallest, value)
        # or
        if value < smallest:
            smallest = value

    return smallest

if __name__ == "__main__" :
    with open("hopedale.txt", "r") as input_file:
        print(smallest_value(input_file))

        
