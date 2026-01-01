file_name = input("Enter the name of file to backup: ")


with open (file_name, "r") as original_file:
    contents = original_file.readlines()
    print(contents)

with open(file_name + "bak", "a") as backup_file:
    for lines in contents:
        backup_file.write(lines)


    
    
