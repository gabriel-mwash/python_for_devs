def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.
    >>> average(10, 20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """
    return (num1 + num2) / 2

def total_occurences(s1: str, s2: str, ch: str) -> int:
    """Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.

    >>> total_occurences('color', 'yellow', 'l')
    3
    >>> total_occurences('red', 'blue', 'l')
    1
    >>> total_occurences('green', 'purple', 'b')
    0
    """
    return s1.count(ch) + s2.count(ch)
