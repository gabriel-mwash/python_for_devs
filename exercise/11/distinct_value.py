def get_distinct_value(my_dict: dict) -> int:
    """return the distinct value from the keys of the dictionary"
    >>> get_distinct_value({"one": 1, "two": 1, "three": 3})
    3
    """

    values = list(my_dict.values())
    for val in values:
        val_count = values.count(val)
        if val_count == 1:
            return val


if __name__ == "__main__":
    print(get_distinct_value({"red": 1, "green": 1, "blue": 2}))
                    
                
## code answer

def count_values(dictionary):
    """ dict -> int
    Return the number of unique values in dictionary
    >>> count_values({"red": 1, "green": 2, "blue": 2})
    1
    """
    return len(set(dictionary.values()))


if __name__ == "__main__":
    print(count_values({"red": 1, "green": 1, "blue": 2}))            
                
    
