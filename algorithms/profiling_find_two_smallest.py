import time
import find_remove_find
import find_two_smallest_scanning_list
import find_two_smallest_sorted

from typing import Any


def time_find_two_smallest(find_func: callable[[list[float]], Any],
                           lst: list[float]) -> float:
    """ return how many seconds find_func(lst) took to execute
    """

    t1 = time.perf_counter()
    find_func(lst)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0

if __name__ == "__main__":
    # Gather the sea level pressures
    sea_levels = []
    sea_levels_file = open("sea_levels.txt", "r")
    for line in sea_levels_file:
        sea_levels.append(float(line))
    sea_levels.file.close()

    # time each of the approaches
    find_remove_find_time = time_find_two_smallest(
        find_remove_find.find_two_smallest, sea_levels)

    sort_get_minimums_time = time_find_two_smallest(
        find_two_smallest_sorted.find_two_smallest, sea_levels)

    walk_through_time = time_find_two_smallest(
        find_two_smallest_scanning_list.find_two_smallest, sea_levels)

    print('"Find, remove, find" took {:.2f}ms.'.format(find_remove_find_time))
    print('"sort, get minimums" took {:.2f}ms.'.format(sort_get_minimums_time))
    print('"walk through the list" took {:.2f}ms'.format(walk_through_time))
                            


