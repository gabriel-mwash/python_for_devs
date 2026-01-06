from typing import Any

def binary_search(L: list, v: Any) -> int:
    """ return the index of the first occurence of value in L, or
    return -1 if value is not in L.
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 1)
    0
    >>> binary_search([1, 3, 4, 4, 5, 7, 9, 10], 4)
    2
    >>> binary_search([1, 3, 4, 4, 5, 7, 10], 5)
    4
    >>> L = [1, 3, 4, 4, 5, 7, 10]
    >>> binary_search(L, 10)
    6
    >>> binary_search(L, -3)
    -1
    >>> binary_search(L, 11)
    -1
    >>> binary_search(L, 2)
    -1
    >>> binary_search([], -3)
    -1
    >>> binary_search([1], 1)
    0
    """

    # mark the left and right indices of the unknown section
    i = 0
    j = len(L) -1

    while i != j + 1:
        m = (i + j) // 2
        if L[m] < v:
            i = m + 1
        else:
            j = m - 1

    if 0 <= i < len(L) and L[i] == v:
        return i
    else:
        return -1

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
