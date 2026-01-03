from typing import Dict

def is_balanced(dictionary: Dict) -> bool:
    """Return key values whose sum is 1.0"
    >>> colors = {"R": 0.1, "G": 0.3, "B": 0.6}
    >>> colors2 = {"R": 0.4, "G": 0.5, "B": 0.2}
    >>> is_balanced(colors)
    True
    >>> is_balanced(colors2)
    False
    """
    values = list(dictionary.values())
    sum_of_values = sum(values)
    if sum_of_values == 1.0:
        return True
    else:
        return False


if __name__ == "__main__":
    from doctest import testmod
    testmod()
    my_dict = {"R": 0.1, "G": 0.3, "B": 0.6}
    print(is_balanced(my_dict))





### - authors code

def is_balanced2(color_to_factor):
    """ (dict of {str: float}) -> bool
    Return True if and only if color_to_factor rep a balanced color
    >>> is_balanced({"R": 0.5, "G": 0.4, "B": 0.7})
    False
    >>> is_balanced("R": 0.3, "G": 0.5, "B": 0.2})
    True
    """

    values = list(color_to_factor.values())
    total = sum(values)
    return total == 1.0
