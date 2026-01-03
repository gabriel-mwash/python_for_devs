db_scientists = {
    "Jgoodall" : {"surname"     : "Goodall",
                  "forename"    : "Jane",
                  "born"        : 1934,
                  "died"        : None,
                  "notes"       : "primate researcher",
                  "author"      : ["In the Shadow of Man",
                                   "The Chimpanzees of Gombe"]},
    
    "rfranklin" : {"surname"    : "Franklin",
                   "forename"   : "Rosalind",
                   "born"       : 1920,
                   "died"       : 1957,
                   "notes"      : "contributed to discovery of DNA"},

    "racarson" : {"surname"     : "Carson",
                  "foreman"     : "Rachel",
                  "born"        : 1907,
                  "died"        : 1964,
                  "notes"       : "raised awareness of effects of DDT",
                  "author"      : ["Silent Spring"]}
    }




def db_consistent(scientist_data: dict) -> dict:
    for inner_dictionary in scientist_data.items():
        hd_dict = inner_dictionary[1]
        for inner_dictionary in scientist_data.items():
            if hd_dict != inner_dictionary[1]:
                return false
            else:
                continue




# - authors code
def db_consistent2(dict_of_dict):
    """ return whether all inner dictionaries in dict_of_dict contain the
    same keys

    >>> db_consistent2({"A": {1: "a", 2: "b"}, "B": {2: "c", 3: "d"}})
    False
    >>> db_consistent({"A": {1: "a", 2: "b"}, "B": {2: "c", 1: "d"}})
    True
    """

    inner_keys_list = []
    # build a list of keys
    for key in dict_of_dict:
        inner_keys = list(dict_of_dict[key].keys())
        inner_keys.sort()
        inner_keys_list.append(inner_keys)

    for i in range(1, len(inner_keys_list)):
        # if the no of keys is different
        if len(inner_key_list[0]) != len(inner_key_list[i]):
            return False
        # if the keys don't match
        for j in range(len(inner_keys_list[0])):
            if inner_keys_list[0][j] != inner_keys_list[1][j]:
                return False
    return True
    
