def min_index(L: list) -> tuple[int, int]:
    """ return a tuple with the min val and its index
    >>> min_index([5, 6, 3, 7, 2, 5, 9])
    (2, 4)
    """
    min_value = L[0]
    min_value_index = L.index(min_value)

    for value in L:
        if value < min_value:
            min_value = value
            min_value_index = L.index(min_value)
    return (min_value, min_value_index)



##if __name__ == "__main__":
##    from doctest import testmod
##    testmod()
##    print(min_index([5, 6, 3, 7, 2, 5, 9]))





## I want to find the max value and its index depending on bool/cond


def min_or_max_index(L: list, condition: bool) -> tuple:
    """ returns a tuple with min or max value with its index depending on condition
    True = min, False = max
    >>> min_or_max_index([5, 6, 3, 7, 2, 5, 9], True)
    (2, 4)
    >>> min_or_max_index([5, 6, 3, 7, 2, 5, 9], False)
    (9, 6)
    """
    current_value = L[0]
    current_value_index = L.index(current_value)

    for value in L:
        if condition:
            if value < current_value:
                current_value = value
                current_value_index = L.index(current_value)
        else:
            if value > current_value:
                current_value = value
                current_value_index = L.index(current_value)

    return (current_value, current_value_index)




if __name__ == "__main__":
    from doctest import testmod
    testmod()
    print(min_or_max_index([5, 6, 3, 7, 2, 5, 9], True))
    print(min_or_max_index([5, 6, 3, 7, 2, 5, 9], False))





## -authors code
def min_or_max_indexv2(L: list, Flag: bool) -> tuple[int, int]:
    """ return the min or max item and its index from L, depending on
    whether flag is True or False
    >>> min_or_max_indexv2([4, 3, 2, 4, 3, 6, 1, 5], True)
    (1, 6)
    >>> min_or_max_indexv2([4, 3, 2, 4, 3, 6, 1, 5], False)
    (6, 5)
    """

    index = 0
    current_value = L[0]

    if flag:
        for i in range(1, len(L)):
            if L[i] < current_value:
                index = i
                current_value = L[i]
    else:
        for i in range(1, len(L)):
            if L[i] > current_value:
                index = i
                current_value = L[i]
    return (current_value, index)

