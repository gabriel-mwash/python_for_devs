def find_largest(n: int, L: list) -> list:
    """ return the n largest values in L in order from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> find_largest(3, L)
    [4, 5, 7]
    """

    copy = sorted(L)
    return copy[-n:]



if __name__ == "__main__":
    from doctest import testmod
    testmod()
