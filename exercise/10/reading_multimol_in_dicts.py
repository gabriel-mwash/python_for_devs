from typing import List, Set, Tuple, Dict

Atom = Tuple[str, Tuple[str, str, str]]
CompoundDict = Dict[str, Atom]

def read_molecule(reader: TextIO) -> CompoundDict:
    """ Read a single molecule from reader and return it, or return None to
    signal eof. the first item in the result is the name of the compound; each
    list contains an atom type and the x, y, and z coordinates of the atom

    >>> instring = 'COMPND TEST\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n'
    >>> infile = StringIO(instring)
    >>> read_molecule(infile)
    ["TEST", ["N", "0.1", "0.2", "0.3"], ["N", "0.2", "0.1", "0.0"]]
    """

    # if there isn't another line, we are at the end of file
    line = reader.readline()
    if not line:
        return None

    # name of the molecule: "COMPND     name"
    parts = line.split()
    name = parts[1]

    # other lines are either "END" or "ATOM num atom_type x y z"
    molecule = [name]
    reading = True
    while reading:
        line = reader.readline()
        if line.startswith("END"):
            reading=False
        else:
            parts = line.split()
            molecule.append(parts[2:])
    return molecule

def read_all_molecules(reader: TextIO) -> CompoundDict:
    """ Read zero or more molecules from reader, returning a list of the
    molecule information
    >>> cmpnd1 = "COMPND T1\\nATOM 1 N 0.1 0.2 0.3\\nATOM 2 N 0.2 0.1 0.0\\nEND\\n"
    >>> cmpnd2 = "COMPND T2\\nATOM 1 A 0.1 0.2 0.3\\nATOM 2 A 0.2 0.1 0.0\\nEND\\n"
    >>> infile = StringIO(cmpnd1 + cmpnd2)
    >>> result = read_all_molecules(infile)
    >>> result["T1"]
    [("N", ("0.1", "0.2", "0.3")), ("N", ("0.2", "0.1", "0.0"))]
    >>> result["T2"]
    [("A", ("0.1", "0.2", "0.3")), ("A", ("0.2", "0.1", "0.0"))]
    """

    # the list of molecule information
    result = []

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule: # none is treated as false in an if statement
            result.append(molecule)
        else:
            reading = False
    return result


if __name__ == "__main__":
    molecule_file = open("multimod.pdb", "r")
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)
    
    
