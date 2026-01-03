def count_duplicates(my_dict: dict) -> int:
    """ Return the number of values that appear two or more times"
    >>> count_duplicates({"R": 1, "G": 2, "B": 2, "Y": 1, "P": 3})
    2
    """
    duplicates = 0
    values = list(my_dict.values())

    for item in values:
        # if an item appears at least 2 times, its a duplicate
        if values.count(item) >= 2:
            duplicates = duplicates + 1

            # remove that item from the list
            num_occurences = values.count(item)
            for i in range(num_occurences):
                values.remove(item)
    return duplicates
    
    
