from typing import TextIO, Any

def hopedale_average(data_file: TextIO) -> int:
##    header = data_file.readline().strip()
##    
##    line = data_file.readline().strip()
##    while line.startswith("#"):
##        line = data_file.readline()
##
    header = data_file.readline()
    comment_line = data_file.readline().strip()
    reading_comment_line = True
    while reading_comment_line:
        if comment_line.startswith("#"):
            print(comment_line)
            comment_line = data_file.readline().strip()
        else:
            reading_comment_line = False
    

    data1 = int(comment_line)

    remaining_data = data_file.readlines()
    counter = 1
    for data in remaining_data:
        data1 += int(data)
        counter += counter
##    print(counter)
##    print(data1)
    print( data1 / counter)


if __name__ == "__main__":
    with open("hopedale.txt", "r") as data_file:
        hopedale_average(data_file)


## authors code

def hopedale_average2(filename: TextIO) -> float:
    """ return the average no of pelts produced per year for the data in hopedale
    """

    with open(filename, "r") as hopedale_file:
        # read the description line.
        hopedale_file.readline()

        # keep reading comment lines until we read the first piece of data
        data = hopedale_file.readline().strip()
        while data.startswith("#"):
            data = hopedale_file.readline().strip()

            # now we have the first piece of data append it to an empty list.
            pelts_list = []
            pelts_list.append(int(data.strip()))

            # read the rest of the data
            for data in hopedale_file:
                pelts_list.append(int(data.strip()))

        return sum(pelts_list) / len(pelts_list)
