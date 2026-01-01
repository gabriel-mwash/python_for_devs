from typing import TextIO


def skip_header(reader: TextIO) -> None:
    """ Skip the header in reader and return the first real piece of data.
    >>> infile = StringIO("Example\\n# Comment\\n Comment\\nData line\\n")
    >>> skip_header(infile)
    "Data line\\n"
    """
    # read the description line
    line = reader.readline()

    # find the first non-comment line
    line = reader.readline()
    while line.startswith("#"):
        line = reader.readline()

    # now line contains the first real piece of data
    return line
