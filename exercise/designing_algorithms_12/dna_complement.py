def dna_compliment(dna: str) -> str:
    """ return the complement of dna"
    >>> dna_compliment("AATTGCCGT")
    'TTAACGGCA'
    """
    
    dna_complement = ""
    for letter in dna:
        if letter == "A":
            dna_complement += "T"
        elif letter == "T":
            dna_complement += "A"
        elif letter == "G":
            dna_complement += "C"
        elif letter == "C":
            dna_complement += "G"
    return dna_complement



if __name__ == "__main__":
    from doctest import testmod
    testmod()
    print(dna_compliment("AATTGCCGT"))




##### -authors code


def complement(sequence: str) -> str:
    """ return the complement of sequence
    >>> complement("AATTGCCGT")
    'TTAACGGCA'
    """

    complement_dict = {"A":"T", "T":"A", "C":"G", "G":"C"}
    sequence_complement = ""

    for char in sequence:
        sequence_complement += complement_dict[char]

    return sequence_complement
