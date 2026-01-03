from typing import Dict
vector = Dict[int, int]


def sparse_add(vector1: dict, vector2: dict) -> vector:
    """ return a new dictionary rep the sum of two sparse vectors stored
    as dictionaries
    >>> vector1 = {0:1, 6:3}
    >>> vector2 = {3:2, 4:7}
    >>> sparse_add(vector1, vector2)
    {3:3, 10:10}
    """
    vector1_keys, vector1_values = list(vector1.keys()), list(vector1.values())
    vector2_keys, vector2_values = list(vector2.keys()), list(vector2.values())
    
    sum_dict = dict()
    sum_dict[sum(vector1_keys)] = sum(vector1_values)
    sum_dict[sum(vector2_keys)] = sum(vector2_values)


    for entries in vector1.items():
        entry




    
## authors code

def sparse_add2(vector1, vector2):
    """ (dict of {int: int}, dict of {int: int} -> dict of {int: int})

    return the sum of sparse vectors vector1 and vector2

    >>> sparse_add({1:3, 3:4}, {2:4, 3:5, 5:6})
    {1:3, 2:4, 3:9, 5:6}
    """

    sum_vector = vector1.copy()
    for key in vector2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] + vector2[key]
        else:
            sum_vector[key] = vector2[key]
    return sum_vector



if __name__ == "__main__":
    print(sparse_add2({0:1, 6:3}, {3:2, 4:7}))
