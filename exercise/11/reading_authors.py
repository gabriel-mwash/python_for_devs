from typing import List, Set


def read_authors_name(file_list: List[str]) -> Set[str]:
    author_list = set()
    for file in file_list:
        with open(file, "r") as current_file:
            author_line = current_file.readline()
            
        line_content = author_line.split()
        author_name = line_content[1]

        author_list.add(author_name)
        return author_list
        
            
