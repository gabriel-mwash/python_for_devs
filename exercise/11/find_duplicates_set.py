from typing import Set, List

def find_dups(L: List[int]) -> Set[int]:
    """ Return a set containing integers occuring more than once in the list"
    >>> find_dups([1, 3, 3])
    {3}
    >>> find_dups([1, 2, 2, 7, 6, 3, 7])
    {2, 7}
    """

    my_set = set()
    i = 0
    for num in L:
        while i < len(L):
            if (L.index(num) != len(L) - 1) and num == L[L.index(num) + i]:
                my_set.add(num)
                i = i + 1
            else:
                i = i + 1
        
    print(my_set)





def find_dupsv2(L: List[int]) -> Set[int]:
    """ return the number of duplicates numbers from L
    >>> find_dupsv2([1, 1, 2, 3, 4, 2])
    {1, 2}
    >>> find_dupsv2([1, 2, 3, 4])
    set()
    """

    elem_set = set()
    dups_set = set()

    for entry in L:
        len_initial  = len(elem_set)
        elem_set.add(entry)
        len_after = len(elem_set)
        if len_initial == len_after:
            dups_set.add(entry)
    return(dups_set)

    
if __name__ == "__main__":
    from doctest import testmod
    testmod()
    find_dupsv2([1, 2, 7, 6, 3, 7])
