from typing import TextIO

def skip_header(reader: TextIO) -> None:
    """ skip the header in reader and return the first real piece of data
    """
    # read the descriptor line
    line = reader.readline()

    # find the first non-comment line
    line = reader.readline()
    while line.startswith("#"):
        line = reader.readline()
        
    # now line contains the first real piece of data
    
    return line
