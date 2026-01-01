from typing import TextIO
from io import StringIO
import time_series


def smallest_value_skip(reader: TextIO) -> int:
    """ Read and process reader, which must start with a time_series header.
    Return the smallest value afer the header. skip missing values, indicated by
    a hypen

    >>> infile = StringIO("Example\\n1\\n-\\n3\\n")
    >>> smallest_value_skip(infile)
    1
    """
    line = time_series.skip_header(reader).strip()

    # now line contains the first data value; this is also smallest val
    # found so far, because it is the only one we have seen.
    smallest = int(line)

    for line in reader:
        line = line.strip()
        if line != "-":
            value = int(line)
            smallest = min(smallest, value)
    return smallest

if __name__ == "__main__":
    with open("hebron_missing_val.txt", "r") as input_file:
        print(smallest_value_skip(input_file))

