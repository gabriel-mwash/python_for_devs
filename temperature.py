def convert_to_celsius(fahrenheit: float) -> float:
    """return the number of Celsius degrees equivalent to fahrenheit
    degrees.

    >>> convert_to_celsius(75)
    23.888888889
    """

    return (fahrenheit - 32.0) * 5.0 / 9.0


print(convert_to_celsius(80))
print(convert_to_celsius(78.8))
print(convert_to_celsius(10.4))


def pie_percent(n: int) -> int:
    """Precondition: n > 0

    Assuming there are n people who want to eat pie, return the
    percentate of the pie that each person gets to eat.
    >>> pie_percent(5)
    20
    >>> pie_percent(2)
    50
    >>> pie_percent(1)
    100
    """
    return int(100 / n)

def triple(number: float) -> float:
    """triples the number
    >>> triple(1)
    6
    >>> triple(5)
    15
    """
    return number * 3


def abs_difference(num1: int, num2: int) -> int:
    """absolute value of difference of two numbers
    >>> abs_difference(4, 5)
    1
    >>> abs_difference(20, 11)
    9
    """
    return abs(num1 - num2)


def distance_in_miles(distanceKm: float) -> float:
    """ convert the km distance to miles
    >>> distance_in_miles(69)
    42.8
    >>> distance_in_miles(160)
    100
    """
    return round((distanceKm / 1.6), 2)


def avg_of_3_grades(mark1: int, mark2: int, mark3: int) -> float:
    """ get the average of the 3 marks given
    >>> avg_of_3_grades(20, 10, 30)
    20
    >>> avg_of_3_grades(75, 84, 90)
    83
    """
    return round((mark1 + mark2 + mark3) / 3, 2)


def best_avg(mark1: int, mark2: int, mark3: int, mark4: int) -> float:
    """ return the average of the best three grades
    >>> best_avg(10, 20, 30, 40)
    30
    """
    avg1 = avg_of_3_grades(mark1, mark2, mark3) / 3
    avg2 = avg_of_3_grades(mark1, mark2, mark4) / 3
    avg3 = avg_of_3_grades(mark1, mark3, mark4) / 3
    avg4 = avg_of_3_grades(mark2, mark3, mark4) / 3

    return round(max(avg1, avg2, avg4, avg4), 2)


def weeks_elapsed(day1: int, day2: int) -> int:
    """ (int , int) -> int
    day1 and day2 are days in the same year. Return the no of full weeks
    that have elapsed btw the two days.
    >>> weeks_elapsed(3, 20)
    2
    >>> weeks_elapsed(20, 3)
    2
    >>> weeks_elapsed(8, 5)
    0
    >>> weeks_elapsed(40, 61)
    3
    """
    return (abs(day1 - day2)) // 7



def square(num):
    """ (number) -> number
    return the square of num.
    >>> square(3)
    9
    """
    return num * num 
















    













    
