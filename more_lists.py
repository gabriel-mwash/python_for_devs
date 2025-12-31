from typing import List

def remove_neg(num_list: List[float]) -> None:
    """ Remove the negative numbers from the list num_list.
    >>> remove_neg([-5, 1, -3, 2])
    [1, 2]
    """
    i = 0
    

    while i < len(num_list) - 1:
        if num_list[i] > 0:
            i = i + 1
        else:
            num_list.remove(num_list[i])
    return num_list
            

    for item in num_list:
        if item < 0:
            num_list.remove(item)

triangle_length = 7
for i in list(range(0, triangle_length)):
    print("T" * i)

