def all_prefixes(string: str) -> set[str]:

    if type(string) != str:
        return "this is not a string"
    
    set_prefix = set()
    for i in range(1, len(string) + 1):
        set_prefix.add(string[:i])

    return set_prefix


if __name__ == "__main__":
    print(all_prefixes("lead"))
        
