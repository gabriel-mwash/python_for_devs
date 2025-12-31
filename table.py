def print_table(n: int) -> None:
    """ print the multiplication table for numbers 1 through n inclusive.
    >>> print_table(5)
    """

    # the numbers to include in the table.
    numbers = list(range(1, n + 1))

    # print the header row.
    for i in numbers:
        print("\t" + str(i), end="")

    # end the header row
    print()

    # print each row number and the contents of each row
    for i in numbers:
        print(i, end="")
        for j in numbers:
            print("\t" + str(i * j), end="")

        # end the current row.
        print()

