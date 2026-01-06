def dutch_flag(L: list[str]) -> list[str]:
    """ return a rearrangement of a list whose elements are strings in the order
    of the dutch flag
    >>> dutch_flag(["red", "blue", "green"])
    ['red', 'green', 'blue']
    >>> dutch_flag(["blue", "blue", "red", "green", "red", "green", "blue"])
    ['red', 'red', 'green', 'green', 'blue', 'blue', 'blue']
    """

    dutch_flag = []
    for color in L:
        if color.lower() == "red":
            dutch_flag.append(color)

    for color in L:
        if color.lower() == "green":
            dutch_flag.append(color)

    for color in L:
        if color.lower() == "blue":
            dutch_flag.append(color)

    return dutch_flag



if __name__ == "__main__":
    import time
    t1 = time.perf_counter()
    dutch_flag(["blue", "blue", "red", "green", "red", "green", "blue"])
    t2 = time.perf_counter()
    print("it took the code {}s".format((t2 - t1)))



# authors code
def dutch_flagv2(L: str) -> list[str]:
    """ return color_list rearranged so that 'red' string comes first,
    'green' second, and 'blue' third
    >>> color_list = ["red", "green", "blue", "red", "red", "blue", "red", "green"]
    >>> dutch_flagv2(color_list)
    ['red', 'red', 'red', 'red', 'green', 'green', 'blue', 'blue']
    """

    i = 0

    # the start of the green section
    start_green = 0

    # the index of the first unexamined color
    start_unknown = 0

    # the index of the last unexamined color
    end_unknown = len(color_list) - 1

    print(color_list)
    print('start')

    while start_unknown <= end_unknown:
        # if its red, swap it with the item to the right of the red section
        if color_list[start_unknown] == 'red':
            color_list[start_green], color_list[start_unknown] \
                = color_list[start_unknown], color_list[start_green]
            start_green += 1
            start_unknown += 1

        # if its green, leave it where it is
        elif color_list[start_unknown] == 'green':
            start_unknown += 1

        # if tis blue, swap it with the item to the left of the blue section
        else:
            color_list[start_unknown], color_list[end_unknown] \
                = color_list[end_unknown], color_list[start_unknown]
            end_unknown -= 1

    return color_list

##
##if __name__ == "__main__":
##    import doctest, time
##    doctest.testmod()
##    t1 = time.perf_counter()
##    color_list = ["red", "green", "blue", "red", "red", "blue", "red", "green"]
##    print(dutch_flagv2(color_list))
##    t2 = time.perf_counter()
##    print(f"it took the code {t2 - t1} seconds")

            
