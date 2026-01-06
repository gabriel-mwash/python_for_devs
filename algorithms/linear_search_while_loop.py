from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """ return the index of the first occurence of value in lst, or
    return -1 if value is not in lst.
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    # examine the items at each index i in lst, starting at index 0:
    #   is lst[i] the val we are searching? if so, stop the search.


    i = 0 # the index of the net item in lst to examine

    # keep going until we reach the end of lst or utnil we find val
    while i != len(lst) and lst[i] != value:
        i = i + 1

        # if we fell off the end of list, we didn't find val
    if i == len(lst):
        return -1
    else:
        return i
