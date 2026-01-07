from typing import Any

def linear_search_while(L: list, value: Any) -> int:
    """ scan from the end of the list
    """
    i = -1
    while i != -(len(L)):
        if value == L[i]:
            return L.index(L[i])
        else:
            i = i + -1
            

def linear_search_for(L: list, value: Any) -> int:
    for i in range((len(L) - 1), 0, -1):
        if value == L[i]:
            return i
    return -1


def sentinel_search(L: list, value: Any) -> int:
    
    L.insert(0, value)
    print(L)

    i = -1
    while L[i] != value:
        i = -1 + i
        

    L.remove(value)

    if i == -(len(L)):
        return -1
    else:
        return L.index(L[i])
    

if __name__ == "__main__":
    my_list = [4, 5, 6, 7, 2, 1]
    print(linear_search_while(my_list, 6))



## authors code



    
