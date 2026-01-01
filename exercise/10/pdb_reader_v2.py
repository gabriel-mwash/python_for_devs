from typing import TextIO
from io import StringIO


def read_molecule(reader: TextIO) -> list:
    """ read a single molecule from reader and return it, or return None to
    signal eof. the first item in the result is the same of the compound;
    each list contains an atom type and the x, y, and z coordinates of
    the atom
    """

    line = reader.readline()
    if not line:
        return None

    # name of the molecule: "COMPND     name"
    parts = line.split()
    name = parts[1]

    # other lines are either "END" or "ATOM num atom_type x y z'
    molecule = [name]
    
    serial_number = 1

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith("END"):
            reading = False
        else:
            parts = line.split()
            # print(parts[1])
            if (int(parts[1]) == 1) or (type(int(parts[1])) == int):
                molecule.append(parts[2:])
            else:
                print("no serial number given")
            
    return molecule


def read_all_molecules(reader: TextIO) -> list:
    """ Read zero or more molecules from reader, returning a list of the
    molecule information.
    """
    # the list of molecule information
    result = []

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule:    # none is treated as false in an if statement
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == "__main__":
    molecule_file = open("multimol.pdb", "r")
    molecules = read_all_molecules(molecule_file)
    molecule_file.close()
    print(molecules)
