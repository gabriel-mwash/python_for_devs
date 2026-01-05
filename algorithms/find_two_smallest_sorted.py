def find_two_smallest(L: list[float]) -> tuple[int, int]:
    """ return a tuple of the indices of two smalles values in list L
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    True
    """

    # sort a copy of L
    # Get the two smallest numbers
    # find their indices in the original list l
    # Return the two indices

    # get a sorted copy of the list so that the two smallest items are at the
    # front
    temp_list = sorted(L)
    smallest = temp_list[0]
    next_smallest = temp_list[1]

    # find their indices in the original list l
    min1 = L.index(smallest)
    min2 = L.index(next_smallest)
    
    # return the two indices
    return (min1, min2)
