import time
import linear_search_while_loop
import linear_search_for_loop
import sentinel_linear_search


from typing import Callable, Any

def time_it(search: Callable[[list, Any], Any], L: list, v: Any) -> float:
    """ Time how long it takes to run function search to find value
    v in list L.
    """

    t1 = time.perf_counter()
    search(L, v)
    t2 = time.perf_counter()
    return (t2 - t1) * 1000.0


def print_times(v: Any, L: list) -> None:
    """Print the no of ms it takes for linear_search to run for list.index,
    the while loop linear search, the for loop and sentinel search
    """

    # Get list.index's running time
    t1 = time.perf_counter()
    L.index(v)
    t2 = time.perf_counter()
    index_time = (t2 - t1) * 1000.0

    # Get the other three running times.
    while_time = time_it(linear_search_while_loop.linear_search, L, v)
    for_time = time_it(linear_search_for_loop.linear_search, L, v)
    sentinel_time = time_it(sentinel_linear_search.linear_search, L, v)


    print("{0}\t{1:.2f}\t{2:.2f}\t{3:.2f}\t{4:.2f}".format(
        v, while_time, for_time, sentinel_time, index_time))



if __name__ == "__main__":
    L = list(range(10000001))
    print_times(10, L)
    print_times(5000000, L)
    print_times(10000000, L)
    
