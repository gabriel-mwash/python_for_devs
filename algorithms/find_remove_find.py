from typing import List, Tuple

def find_two_smallest(L: List[float]) -> Tuple[int, int]:
    """ return a tuple of the indices of the two smallest val in list L.
    >>> items = [809, 834, 447, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> items == [809, 447, 478, 307, 122, 96, 102, 324, 476]
    True
    """
    # get the minimum item in L
    # find the indes of the minimum item
    # remove that item from the list
    # find the index of the new minimum item in the list
    # put the smallest item back in the list
    # if necessary, adjust the second index
    # return the two indices


    # find the index of the minimum and remove that item
    smallest = min(L)
    min1 = L.index(smallest)
    L.remove(smallest)

    #find the index of the new minimum
    next_smallest = min(L)
    min2 = L.index(next_smallest)

    # put samallest back into L
    L.insert(min1, smallest)

    # fix min2 in case it was affected by the removal and reinsertion:
    if min1 <= min2:
        min2 += 1
    return(min1, min2)
    

    
