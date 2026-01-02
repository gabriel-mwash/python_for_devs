from typing import Tuple, Set, Any

def mating_pairs(set1: Set, set2: Set) -> Tuple[Any]:
    """ Return the tuple pair of popped male and female sets to get a pair
    """
    mate_pair = set()
    while len(set1) and len(set2) != 0:
        mate_pair.add((set1.pop(), set2.pop()))
    return mate_pair


    
## --- solution

def mating_pairsv2(males, females):
    """ return a set of tupes where each tuple contains a male from males and a
    female from females
    >>> mating_pairs({"Anne", "Beatrice", "Cari"}, {"Ali", "Bob", "Chen"})
    {("Cari", "Chen"), ("Beatrice", "Bob"), ("Anne", "Ali")}
    """
    pairs = set()
    num_gerblis = len(males)
    for i in range(num_gerblis):
        male = males.pop()
        female = females.pop()
        pairs.add((male, female),)
    return pairs

if __name__ == "__main__":
    pair = mating_pairsv2({"lion", "Dog", "Tiger"}, {"bitch", "tigress", "lioness"})
    print(pair)
