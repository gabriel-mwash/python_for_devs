"""
text = ""
while text != "quit":
    text = input("Please enter a chemical forumula(or 'quit to exit): ")
    if text == "quit":
        print("...exiting program")
    elif text == "H2O":
        print("water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("methane")
    else:
        print("unknown compound")


while True:
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("...exiting program")
        break
    elif text == "H2O":
        print("water")
    elif text == "NH3":
        print("ammonia")
    elif text == "CH4":
        print("methane")
    else:
        print("unkown compound")

"""

def mystery_function(values: list) -> list:
    """Return the reverse of list. also that of nested lists within a list
    >>> mystery_function([[3, 5], [1, 0]])
    [[5, 3], [0, 1]]
    >>> mystery_function([[5, 7, 1], [8, 4, 3]])
    [[1, 7, 5], [3, 4, 8]]
    """

    # an empty list
    result = []
    for sublist in values:

        # append the values in the sublist to the list result
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)

    return result


