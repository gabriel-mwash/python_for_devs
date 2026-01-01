with open("file_example.txt", "r") as file:
    contents = file.read()

print(contents)

with open("file_example.txt", "r") as example_file:
    lines = example_file.readlines()

print(lines)


with open("planets.txt", "r") as file:
    planets = file.readlines()


