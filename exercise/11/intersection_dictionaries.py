from typing import Any

def dict_intersect(dictionary1: dict, dictionary2: dict) -> dict[Any, Any]:
    """ Return a dictionary containing a key/val pair found in both dict1 and
    dict2
    >>> my_dictionary_1 = {"r": 1, "r": 2, "r": 3}
    >>> my_dictionary_2 = {"r": 1, "r": 3, "r": 4}
    >>> dict_intersect(my_dictionary_1, my_dictionary_2)
    {"r": 1, "r": 3}
    """
    
    final_dictionary = {}
    for key1, val1 in dictionary1.items():
        for key2, val2 in dictionary2.items():
            if (key1, val1) == (key2, val2):
                final_dictionary[key1] = val1
    return final_dictionary




if __name__ == "__main__":
    dict1 = {"one": 1, "two": 2, "three": 3}
    dict2 = {"one": 3, "four": 4, "two": 2}

    my_dictionary_1 = {"r": 1, "j": 2, "k": 3}
    my_dictionary_2 = {"r": 1, "k": 3, "r": 4}

    print(dict_intersect(dict1, dict2))
    print(dict_intersect(my_dictionary_1, my_dictionary_2))


#authors code ____________

def dict_intersect2(dict1, dict2) -> dict[Any, Any]:
    """ Return a new dict that contains only the key/val pairs that
    occur in both dict1 and dict2

    >>> dict_intesect2({"a": 1, "b": 2, "c": 3}, {"a": 1, "d": 2, "b": 2})
    {"a": 1, "b":2}
    """
    intersection = {}
    for (key, value) in dict1.items():
        if key in dict2 and value == dict2[key]:
            intersection[key] = value
    return intersection
