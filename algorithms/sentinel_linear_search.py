from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """ return the index of the first occurence of value in lst, or
    return -1 if value is not in lst
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """

    # add the sentinel
    lst.append(value)

    i = 0

    # keep going until we find value:
    while lst[i] != value:
        i = i + 1

        # remove the sentinel
    lst.pop()

        # if we reached the end of the list we didn't find value
    if i == len(lst):
        return -1
    else:
        return i
