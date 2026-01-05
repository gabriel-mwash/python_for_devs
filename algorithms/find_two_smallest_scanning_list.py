def find_two_smallest(L: list[float]) -> tuple[int, int]:
    """ return a tuple of the indices of the two smallest values in list L
    >>> items = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
    >>> find_two_smallest(items)
    (6, 7)
    >>> find_two_smallest([3, 1])
    (1, 0)
    >>> find_two_smallest([4, 2, 1, 0])
    (3, 2)
    >>> find_two_smallest([6])
    'less or no values in list'
    >>> find_two_smallest([])
    'less or no values in list'
    """

    # keep track of the indices of the two smallest values found so far
    # examine each value in the list in order
    #   update the indices when a new smaller value is found
    # return the two indices

    # set min1 and min2 to the indices of the smallest and next-smallest
    # values of the beginning of l


    if len(L) < 2:
        return "less or no values in list"

    if L[0] < L[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0

    # examine each value in the list in order
    for i in range(2, len(L)):
        if (L[i] < L[min1]) and (L[i] < L[min2]):
            min2 = min1
            min1 = i

        elif L[i] < L[min2]:
            min2 = i
        
    return (min1, min2)
        

if __name__ == "__main__":
    import time
    t1 = time.perf_counter()
    print(find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476]))
    t2 = time.perf_counter()
    print("scanning through list took {:.2f}ms".format((t2 - t1) * 1000))
