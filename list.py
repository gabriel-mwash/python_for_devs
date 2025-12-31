
def average(L: list) -> float:
    """
   Return the average of the values in L.

    >>> average([1.4, 1.6, 1.8, 2.0])
    1.7
    """
    return
   


def same_first_last(L: list) -> bool:
    """Precondition: len(L) >= 2
    Return True if and only if first item of the list is the same as the last
    >>> same_first_last([3, 4, 2, 8, 3])
    True
    >>> same_first_last(['apple', 'banana', 'pear'])
    False
    >>> same_first_last([4.0, 4.5])
    False
    """
    return L[0] == L[-1]


def is_longer(L1: list, L2: list) -> bool:
    """Return True iff the length of l1 is longer than that of l2.
    >>> is_longer([1, 2, 3], [4, 5])
    True
    >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
    False
    >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
    False
    """
    return len(L1) > len(L2)
