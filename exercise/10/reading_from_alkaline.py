with open("alkaline_metals.txt", "r") as input_file:
    contents = input_file.readlines()


nested_list = []
for line in contents:
    name, atomic_num, atomic_weight = line.split()
    nested_list.append([name, [atomic_num, atomic_weight]])

print(nested_list)
    
