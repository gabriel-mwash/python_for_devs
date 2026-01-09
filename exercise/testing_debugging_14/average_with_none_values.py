def average(values: list[float]) -> float:
    """ return the average of the no in values. some items in values are
    None, and they are not counted toward the average
    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0
    total = 0

    if len(values) == 0:
        return "empty list"
    

    for value in values:
        if value is not None:
            total += value
            count += 1
    return total / count


if __name__ == "__main__":
    print(average([None, 30, 20]))
