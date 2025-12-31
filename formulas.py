text = ""
while text != "quit":
    text = input("Please enter a chemical forumula(or 'quit to exit): ")
    if text == "quit":
        print("...exiting program")
    elif text == "H2O":
        print("water")
    elif text == "NH3":
        print("Ammonia")
    elif text == "CH4":
        print("methane")
    else:
        print("unknown compound")


while True:
    text = input("Please enter a chemical formula (or 'quit' to exit): ")
    if text == "quit":
        print("...exiting program")
        break
    elif text == "H2O":
        print("water")
    elif text == "NH3":
        print("ammonia")
    elif text == "CH4":
        print("methane")
    else:
        print("unkown compound")



def mystery_function(values):
    result = []
    for sublist in values:
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0, i)

    return result
