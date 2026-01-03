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


def db_headings(scientist_data: dict) -> dict:
    for inner_dictionary in scientist_data.items():
        hd_dict = inner_dictionary[1]
        hd_set = set(hd_dict.keys())
        print(hd_set)
        break



if __name__ == "__main__":
    db_headings(db_scientists)

# authors code --------------

def db_headings2(dict_of_dict):
    """(dict of dict) -> set.
    return a set of the keys in the inner dictionaries in dict_of_dict

    >>> db_headings({"A": {1: "a", 2: "b"}, "B": {2: "c", 3: "d"}})
    {1, 2, 3}
    """
    inner_keys = set()
    for key in dict_of_dict:
        for inner_key in dict_of_dict[key]:
            inner_keys.add(inner_key)
    return inner_keys
