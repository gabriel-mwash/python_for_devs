with open("hopedale.txt", "r") as hopedale_file:

    # Read and skip the description line.
    hopedale_file.readline()

    # keep reading and skipping comment lines until we read the first piece of data
    data = hopedale_file.readline().strip()
    while data.startswith("#"):
        data = hopedale_file.readline().strip()

    # Now we have the first piece of data. Accumulate the total no of pelts
    total_pelts = int(data)

    # Read the rest of the data
    for data in hopedale_file:
        total_pelts = total_pelts + int(data.strip())

print("Total number of pelts: ", total_pelts)



with open("hopedale.txt", "r") as my_file:
    my_file.readline()

    data = my_file.readline().rstrip()
    while data.startswith("#"):
        data = my_file.readline().rstrip()

    print(data)

    for data in my_file:
        print(data.rstrip())
