def merge(L1: list, L2: list) -> list:
    """ Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """

    newL = []
    i1 = 0
    i2 = 0

    # for each pair of items in L1[i1] and L2[i2], copy the smaller into newL
    while not(i1 == len(L1) and i2 == len(L2)):
        # append the smaller of L1[i1] and L2[i2] to newL; if one of the list
        # has no items left, copy from the other one.
        if i2 == len(L2) or (i1 != len(L1) and L1[i1] <= L2[i2]):
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
    return newL
"""
    # for each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while i1 != len(L1) and i2 != len(L2):
        if L1[i1] <= L2[i2]:
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1

        # gather any leftover items from the two sections.
        # note that one of them will be empty because of the loop condition
    newL.extend(L1[i1:])
    newL.extend(L2[i2:])
    return newL
"""
    
        
def merge_sort(L: list) -> None:
    """ Reorder the items in L from smallest to largest.
    >>> L = [3, 4, 7, -1, 2, 5]
    >>> mergesort(L)
    >>> L
    [-1, 2, 3, 4, 5, 7]
    """
    # make a list of 1-item lists so that we can start merging
    workspace = []
    for i in range(len(L)):
        workspace.append([L[i]])

    # the next two lists to merge are workspace[i] and workspace[i + 1]
    i = 0
    # as long as there are at least two more lists to merge, merge them.

    while i < len(workspace) - 1:
        L1 = workspace[i]
        L2 = workspace[i + 1]
        newL = merge(L1, L2)
        workspace.append(newL)
        i += 2

    # copy the result back into L
    if len(workspace) != 0:
        L[:] = workspace[-1][:]
        
        
