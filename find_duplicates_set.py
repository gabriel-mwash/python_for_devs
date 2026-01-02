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
                print(L[L.index(num) + 1], "index ", i)
                my_set.add(num)
                i = i + 1
            else:
                i = i + 1
        
    print(my_set)


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    find_dups([1, 2, 7, 6, 3, 7])
