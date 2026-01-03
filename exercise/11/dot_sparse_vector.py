def sparse_dot(vector1, vector2):
    sum_vector = vector1.copy()
    for key in vector2:
        if key in sum_vector:
            sum_vector[key] = sum_vector[key] * vector2[key]
        else:
            sum_vector[key] = vector2[key]
    return sum_vector


if __name__ == "__main__":
    print(sparse_dot({1:3, 3:4}, {2:4, 3:5, 5:6}))



# authors code
def sparse_dot2(vector1, vector2):
    """ (dict of {int: int), dict of {int: int} -> dict of {int: int}
    Return the dot product of sparse vectors in vector1 and vector2
    >>> sparse_dot({1:3, 3:4}, {2:4, 3:5, 5:6})
    20
    """

    dot = 0
    for key1 in vector1:
        if key1 in vector2:
            dot = dot + vector[key1] * vector2[key1]
    return dot
