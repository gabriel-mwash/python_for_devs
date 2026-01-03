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
