def bubble_sort(lst: list) -> None:
    # the beginning of the unsorted section. The largest item will be placed here
    beginning = 0

    # keep going until there is only one item to consider
    while beginning < len(lst):
        # sweep through the list.
        for i in range(len(lst) - 1, beginning, -1):
            if lst[i] < lst[i - 1]:
##                tmp = lst[i - 1]
##                lst[i - 1] = lst[i]
##                lst[i] = tmp
                lst[i], lst[i - 1] = lst[i -1], lst[i]
        beginning = beginning + 1
    return lst






def bubble_sort_end(lst: list) -> None:
    """ Reorder items in L from smallest to largest
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> bubble_sort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    >>> bubble_sort([])
    []
    >>> bubble_sort_end([1])
    [1]
    >>> bubble_sort_end([2, 1])
    [1, 2]
    >>> bubble_sort_end([1, 2])
    [1, 2]
    >>> bubble_sort_end([3, 3, 3])
    [3, 3, 3]
    >>> bubble_sort_end([-5, 3, 0, 3, -6, 2, 1, 1])
    [-6, -6, 0, 1, 1, 2, 3, 3]
    """

    # the end of the unsroted section. the largest item will be placed here
    end = len(lst) - 1

    # keep going until there are either 0 or 1 items to consider
    # (the 0 case is for the empty list.)
    while end > 0:
        # sweep through the list.
        for i in range(0, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

        end = end - 1 
    return lst


if __name__ == "__main__":
    my_list = [-5, 0, -6, 2, 3]
    print(bubble_sort_end(my_list))
